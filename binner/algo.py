from .binner_main import Binner
from . import log
"""
A Set of algorithms to find
smallestbin size, multi bin packing
and single bin packing

Definitions:
find optimal:
each area in a bin is set as a level whenever
the 'first' item is added to it. As a result
if we have a bin with size: 10, 10, 10 and
item one being 3, 3, 3. The subsequent item
must allocate space proportianate to its relatives
coordinates

TRY to move to x axis as much as possible before
creating another level. Additionally try to rotate
vertically, and horizontal for a optimal fit.

"""
class Algo(object):
  def __init__(self, args, bins, items):
    self.binner = Binner(args, bins, items )
    self.args = args
    self.bins = bins
    self.items = items

  def get_next_bin(self):
	 if self.args.multi_use_smallest_bins:
		return self.bins.nextsmallest()
	 return self.bins.next()
  def run( self ):
	 pass
