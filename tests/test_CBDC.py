import unittest
from src.CBDC import CBDC

class TestCBDC(unittest.TestCase):
    def test_CBDC_creation(self):
        cbdc = CBDC('Digital Dollar', 1.0, 'USA')
        self.assertEqual(cbdc.name, 'Digital Dollar')
        self.assertEqual(cbdc.value, 1.0)
        self.assertEqual(cbdc.country, 'USA')

if __name__ == '__main__':
    unittest.main()