#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
import itertools, re
import colorama

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

import escapelib
from escapelib import *

class Tests(unittest.TestCase):

	def test_escape(self):
		testVectors = {
			("A", PythonREEscaper): "A",
			("z", PythonREEscaper): "z",
			("9", PythonREEscaper): "9",
			("-", PythonREEscaper): "\\-",
			("+", PythonREEscaper): "\\+"
		}
		for (chall, escaperCtor), resp in testVectors.items():
			with self.subTest(chall=chall, escaperCtor=escaperCtor, resp=resp):
				escaper = escaperCtor()
				actual = escaper(chall)
				self.assertEqual(resp, actual)


if __name__ == "__main__":
	unittest.main()
