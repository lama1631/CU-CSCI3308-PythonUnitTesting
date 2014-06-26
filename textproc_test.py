#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...
    def test_const(self):
        not_text=12345
        self.assertRaises(textproc.TextProcError, textproc.Processor, not_text)

    def test_count(self):
        letters = "abcde"
        ans = textproc.Processor(letters).count()
        self.assertEqual(ans, 5, "Wrong Length")

    def test_count_alpha(self):
        four = "blue123"
        ans = textproc.Processor(four).count_alpha()
        self.assertEqual(ans, 4, "Wrong Length")
        upper = "AaBbCcsdf"
        up = textproc.Processor(upper).count_alpha()
        self.assertEqual(up, 9, "Wrong Length")

    def test_count_numeric(self):
        six = "0123456aada"
        ans = textproc.Processor(six).count_numeric()
        self.assertEqual(ans, 7, "Wrong Length")

    def test_count_vowels(self):
        word = "abcdefghijklmnopqrstuvwxyz"
        ans = textproc.Processor(word).count_vowels()
        self.assertEqual(ans, 5, "Wrong Vowels")
        cap = "AEIOU"
        Cap = textproc.Processor(cap).count_vowels()
        self.assertEqual(Cap, 5, "Wrong Capital Vowels")

    def test_is_phonenumber(self):
        phone = "303-539-2217"
        ans = textproc.Processor(phone).is_phonenumber()
        self.assertTrue(ans)

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
