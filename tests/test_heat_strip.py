import os
from pathlib import Path
import unittest
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
class HeatStripAndR32ChartTests(unittest.TestCase):
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
 def air(self):self.page.locator('#field-nav label[for=page-air]').click()
 def set(self,model,kw,volt,cfm):
  self.page.locator('#hs-model').select_option(model);self.page.locator('#hs-kw').select_option(kw)
  self.page.locator('#hs-volt').select_option(volt);self.page.locator('#hs-cfm').fill(cfm)
 def test_rise_and_minimum_pass(self):
  self.air();self.assertTrue(self.page.locator('#heat-strip-check').is_visible())
  self.set('AMST36CU1300','10','230','1200')
  # 10 x 3412 x .96 / (1.08 x 1200) = 25.3
  self.assertEqual(self.page.locator('#hs-rise').inner_text(),'25 °F')
  self.assertEqual(self.page.locator('#hs-min').inner_text(),'1,170 CFM')
  self.assertIn('at or above',self.page.locator('#hs-min-note').inner_text())
 def test_below_minimum_and_voltage(self):
  self.air();self.set('AMST60DU1300','25','208','1800')
  self.assertEqual(self.page.locator('#hs-min').inner_text(),'1,930 CFM')
  self.assertIn('BELOW',self.page.locator('#hs-min-note').inner_text())
  # 25 x 3412 x .87 / (1.08 x 1800) = 38.2
  self.assertEqual(self.page.locator('#hs-rise').inner_text(),'38 °F')
 def test_kit_not_listed(self):
  self.air();self.set('AMST24BU1300','19','230','900')
  self.assertEqual(self.page.locator('#hs-min').inner_text(),'Not listed')
 def test_reverse_airflow_estimate(self):
  self.air();self.set('AMST36CU1300','10','230','')
  self.page.locator('#hs-reverse summary').click();self.page.locator('#hs-measured').fill('25')
  # 10 x 3412 x .96 / (1.08 x 25) = 1213
  self.assertEqual(self.page.locator('#hs-est').inner_text(),'1,213 CFM')
 def test_use_tap_from_lookup(self):
  self.air();self.page.locator('#ag-family').select_option('amst');self.page.locator('#ag-model').select_option('AMST30BU1300')
  self.page.locator('#hs-kw').select_option('15');self.page.locator('#hs-use-tap').click()
  self.assertEqual(self.page.locator('#hs-model').input_value(),'AMST30BU1300')
  self.assertEqual(self.page.locator('#hs-cfm').input_value(),self.page.locator('#ag-cfm').inner_text().replace(',',''))
  self.assertEqual(self.page.locator('#hs-min').inner_text(),'1,050 CFM')
 def test_no_sideways_scroll_on_phone(self):
  self.air();w=self.page.evaluate('document.getElementById("heat-strip-check").scrollWidth-document.getElementById("heat-strip-check").clientWidth')
  self.assertLessEqual(w,0)
 def test_r32_dfve_chart_present_with_a2l_rows(self):
  card=self.page.locator('#dfve-r32-chart')
  self.assertEqual(card.count(),1)
  text=card.evaluate('e=>e.textContent')
  for code in ['A0','AF','A1','b3','b9','9b','TSTAT ID NO COM','BLOWN FUSE','Ventilate the room first']:
   self.assertIn(code,text)
  self.assertIn('not the manual’s exact wording',text)
 def test_amst30_t9_shown(self):
  text=self.page.locator('#reference-67').evaluate('e=>e.textContent')
  self.assertNotIn('NOT SHOWN',text);self.assertIn('Table 9, p.13',text);self.assertIn('only T1 and T6-T9',text)
 def test_dmvt_r32_chart_present(self):
  card=self.page.locator('#dmvt-r32-chart');self.assertEqual(card.count(),1)
  text=card.evaluate('e=>e.textContent')
  for s in ['HTR TOO LARGE','NO HTR MATCH','MTR LCKD ROTOR','LOW ID AIRFLOW','dF','100 CFM','not the manual’s exact wording']:
   self.assertIn(s,text)
  self.assertNotIn('AF and A1 runs together',self.page.locator('#dfve-r32-chart').evaluate('e=>e.textContent'))
