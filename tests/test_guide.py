"""Browser regression tests. Run: python -m unittest discover -s tests -v."""
import functools
import http.server
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import threading
import unittest

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class GuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workspace = tempfile.TemporaryDirectory()
        cls.site = Path(cls.workspace.name)
        for name in ['index.html', 'sw.js', 'manifest.webmanifest']:
            shutil.copy2(ROOT / name, cls.site / name)
        shutil.copytree(ROOT / 'icons', cls.site / 'icons')
        handler = functools.partial(QuietHandler, directory=str(cls.site))
        cls.server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}/'
        cls.playwright = sync_playwright().start()
        options = {'headless': True}
        if os.environ.get('GUIDE_TEST_BROWSER'):
            options['executable_path'] = os.environ['GUIDE_TEST_BROWSER']
        cls.browser = cls.playwright.chromium.launch(**options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.workspace.cleanup()

    def setUp(self):
        self.context = self.browser.new_context(viewport={'width': 390, 'height': 844})
        self.page = self.context.new_page()
        self.errors = []
        self.page.on('pageerror', lambda error: self.errors.append(str(error)))
        self.page.goto(self.url)

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [])

    def navigate(self, destination):
        self.page.locator(f'#field-nav label[for="{destination}"]').click()

    def search(self, query):
        self.page.locator('#global-search').fill(query)

    def test_real_model_suggestions_and_dip_shortcut(self):
        self.search('DX6VS')
        names = self.page.locator('#model-suggestions button strong').all_text_contents()
        self.assertIn('DX6VS', names)
        self.assertTrue(all(name.startswith('DX6VS') for name in names))
        self.search('DC4SQA6010')
        self.assertIn('DC4SQA6010A', self.page.locator('#model-suggestions button strong').all_text_contents())
        self.search('DC9VSA2410')
        self.assertEqual(self.page.locator('#model-suggestions button strong').all_text_contents(), ['DC9VSA2410A'])
        self.page.locator('#model-suggestions button').click()
        self.page.locator('[data-model-topic="dip"]').click()
        self.page.wait_for_function("document.querySelector('#sec-dip .section-search').value==='DC9VS'")
        self.assertEqual(self.page.locator('.page-radio:checked').get_attribute('id'), 'page-dip')
        self.assertEqual(self.page.locator('#sec-dip .section-search-count').inner_text(), '1 match')

    def test_search_controls_and_topic_state(self):
        self.navigate('page-fault')
        self.search('termination')
        self.navigate('page-dip')
        self.navigate('page-fault')
        self.assertEqual(self.page.locator('#global-search').input_value(), 'termination')
        self.assertEqual(self.page.locator('#sec-fault-codes .section-search-count').inner_text(), '5 matches')
        self.page.locator('#sec-fault-codes .topic-tab').first.click()
        self.assertEqual(self.page.locator('#global-search').input_value(), '')
        self.assertEqual(self.page.locator('#sec-fault-codes .section-search').input_value(), '')
        self.page.locator('#search-options').click()
        self.assertEqual(self.page.evaluate('document.activeElement.id'), 'global-search')
        for destination in ['page-start', 'page-dip', 'page-ahri']:
            self.navigate(destination)
            self.page.keyboard.press('Control+k')
            self.assertEqual(self.page.evaluate('document.activeElement.id'), 'global-search')
            self.page.keyboard.press('Meta+k')
            self.assertEqual(self.page.evaluate('document.activeElement.id'), 'global-search')
        self.navigate('page-start')
        self.page.locator('.start-btn[data-q="furnace"]').click()
        self.assertEqual(self.page.locator('#global-search').input_value(), 'furnace')

    def test_ahri_field_filter_survives_navigation(self):
        self.navigate('page-ahri')
        self.page.locator('#ahri-outdoor-model').fill('DC9VSA2410')
        self.assertEqual(self.page.locator('#ahri-result-count').inner_text(), '12 matches')
        self.assertEqual(self.page.locator('#global-search').input_value(), 'DC9VSA2410')
        self.navigate('page-start')
        self.navigate('page-ahri')
        self.assertEqual(self.page.locator('#ahri-outdoor-model').input_value(), 'DC9VSA2410')
        self.assertEqual(self.page.locator('#ahri-result-count').inner_text(), '12 matches')
        self.search('DC4SQA6010')
        self.assertEqual(self.page.locator('#ahri-outdoor-model').input_value(), '')
        self.assertEqual(self.page.locator('#ahri-result-count').inner_text(), '2 matches')

    def test_offline_reload_and_manifest(self):
        self.page.evaluate('navigator.serviceWorker.ready')
        self.page.wait_for_function('navigator.serviceWorker.controller!==null')
        manifest = json.loads((self.site / 'manifest.webmanifest').read_text())
        self.assertEqual(manifest['display'], 'standalone')
        session = self.context.new_cdp_session(self.page)
        self.assertEqual(session.send('Page.getAppManifest')['errors'], [])
        keys = self.page.evaluate("caches.keys().then(async keys=>{const cache=await caches.open(keys.find(key=>key.startsWith('daikin-guide-')));return (await cache.keys()).map(request=>new URL(request.url).pathname)})")
        self.assertEqual(set(keys), {'/index.html', '/manifest.webmanifest', '/icons/guide-192.png', '/icons/guide-512.png'})
        self.context.set_offline(True)
        self.page.reload()
        self.navigate('page-ahri')
        self.search('DC9VSA2410')
        self.assertEqual(self.page.locator('#ahri-result-count').inner_text(), '12 matches')
        self.navigate('page-start')
        self.search('DX6VS')
        self.assertGreater(self.page.locator('#start-results .start-hit').count(), 0)
        self.assertEqual(self.page.locator('.ref-card').count(), 113)

    def test_responsive_pages(self):
        for width in [320, 390, 768, 1440]:
            self.page.set_viewport_size({'width': width, 'height': 844})
            for destination in ['page-start', 'page-fault', 'page-dip', 'page-zoning', 'page-catalog', 'page-ahri', 'page-gaps', 'page-sources']:
                self.navigate(destination)
                self.assertFalse(self.page.evaluate('document.documentElement.scrollWidth>innerWidth'), (width, destination))

    def test_saved_release_update_can_activate_offline(self):
        self.page.evaluate('navigator.serviceWorker.ready')
        self.page.wait_for_function('navigator.serviceWorker.controller!==null')
        index = self.site / 'index.html'
        worker = self.site / 'sw.js'
        initial_index, initial_worker = index.read_text(), worker.read_text()
        try:
            index.write_text(initial_index.replace('</head>', '<meta name="test-release" content="updated"></head>', 1))
            worker.write_text(re.sub(r"const CACHE='[^']+'", "const CACHE='daikin-guide-test-update'", initial_worker, count=1))
            self.page.evaluate('navigator.serviceWorker.getRegistration().then(reg=>reg.update())')
            self.page.wait_for_function("!document.querySelector('#update-guide').hidden")
            self.context.set_offline(True)
            self.page.locator('#update-guide').click()
            self.page.wait_for_function("document.querySelector('meta[name=test-release]')?.content==='updated'")
            self.navigate('page-ahri')
            self.search('DC9VSA2410')
            self.assertEqual(self.page.locator('#ahri-result-count').inner_text(), '12 matches')
        finally:
            index.write_text(initial_index)
            worker.write_text(initial_worker)


if __name__ == '__main__':
    unittest.main()
