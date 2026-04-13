"""
Alan Alejandro Rodriguez Avalos
Erick Eduardo Rodriguez Gomez 

Exercise5
"""

import unittest

class TestScan(unittest.TestCase):
    def test_subtest(self):
        casos = [
            ('12345', '$7.25'),
            ('23456', '$12.50'),
            ('99999', 'Error: barcode not found'),
            ('', 'Error: empty barcode'),
            ('12345 23456', '$19.75')
        ]

        for input, expected_output in casos:
            with self.subTest(prices=input):
                self.assertEqual(scan(prices), expected_output)