import unittest
import binner
"""
Unit tests for Binner

algorithms tested:

MultiBinPacking
SingleBinPacking
SmallestBinPacking
"""

class BinnerSingleUnitTest(unittest.TestCase):
	def runTest(self):
		binner = Algo().single_bin_packing(items, bins)

class BinnerMultiUnitTest(unittest.TestCase):
	def runTest(self):
		binner = Algo().single_bin_packing(items, bins)

class BinnerOptiUnitTest(unittest.TestCase):
	def runTest(self):
		binner = Algo().single_bin_packing(items, bins)

class BinneItemUnitTest(unittest.TestCase):
	def runTest(self):
		binner = Algo().single_bin_packing(items, bins)
		pass


if __name__ == '__main__':
	item = binner.Item()
        item.w = 200
        item.h = 400
        item.d = 200 

	for i in range(0, 10):
		item.rotate()

		print "New item dimensions: width: {0}, height: {1}, depth: {2}".format(item.w, item.h, item.d)
