#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import unittest
from process import petition, source, count_answers, less_views, older_newer_answer, higer_reputation
import json

with open('data.json', 'r') as j:
    data = json.loads(j.read())


class TestMyModule(unittest.TestCase):

    def test_petition(self):
        self.assertIsNotNone(petition(source))

    def test_case2(self):
        self.assertIsInstance(count_answers(data), dict)

    def test_case3(self):
        self.assertIsInstance(less_views(data), dict)

    def test_case4(self):
        self.assertIsInstance(older_newer_answer(data), dict)

    def test_case5(self):
        self.assertIsInstance(higer_reputation(data), dict)


if __name__ == "__main__":
    unittest.main()
