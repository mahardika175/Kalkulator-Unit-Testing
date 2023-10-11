import unittest
from unittest.mock import patch
from tugas7 import operasi_matematika

class TestOperasiMatematika(unittest.TestCase):
    # [PENJUMLAHAN]
    @patch('builtins.input', side_effect = ['1', '2', '5'])
    def test_penjumlahan(self, input):
        result = operasi_matematika()
        self.assertEqual(result, 7)
        
    # [PENGURANGAN]
    @patch('builtins.input', side_effect = ['2', '2', '1'])
    def test_pengurangan(self, input):
        result = operasi_matematika()
        self.assertEqual(result, 1)

    # [PERKALIAN]
    @patch('builtins.input', side_effect = ['3', '2', '5'])
    def test_perkalian(self, input):
        result = operasi_matematika()
        self.assertEqual(result, 1) # ini salah, hasil seharusnya 10

    # [PEMBAGIAN]
    @patch('builtins.input', side_effect = ['4', '10', '2'])
    def test_pembagian(self, input):
        result = operasi_matematika()
        self.assertEqual(result, 5)
        
if __name__ == '__main__':
    unittest.main()