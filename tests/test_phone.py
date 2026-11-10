import os
from pathlib import Path
import unittest
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
PAGES=['page-start','page-fault','page-air','page-charge','page-zoning','page-models']
class PhoneLayoutTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.p=sync_playwright().start()
  cls.b=cls.p.chromium.launch(**({'executable_path':os.environ['GUIDE_TEST_BROWSER']} if os.environ.get('GUIDE_TEST_BROWSER') else {}))
 @classmethod
 def tearDownClass(cls):cls.b.close();cls.p.stop()
 def setUp(self):
  self.page=self.b.new_page(viewport={'width':390,'height':844});self.errors=[]
  self.page.set_default_timeout(3000)
  self.page.on('pageerror',lambda e:self.errors.append(str(e)))
  self.page.goto((ROOT/'index.html').as_uri())
 def tearDown(self):self.page.close();self.assertEqual(self.errors,[])
 def test_no_sideways_scroll_on_any_tab(self):
  for name in PAGES:
   self.page.locator(f'#field-nav label[for={name}]').click()
   self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),390,name)
 def test_tab_bar_sits_at_bottom(self):
  box=self.page.locator('#field-nav').bounding_box()
  self.assertGreaterEqual(box['y'],844-110);self.assertGreaterEqual(box['width'],380)
  main=self.page.locator('main#field-content').bounding_box()
  self.assertGreaterEqual(main['x'],0);self.assertLessEqual(main['width'],390)
 def test_desktop_keeps_side_nav(self):
  self.page.set_viewport_size({'width':1440,'height':900})
  box=self.page.locator('#field-nav').bounding_box()
  self.assertLess(box['x'],60);self.assertGreater(box['height'],500)
