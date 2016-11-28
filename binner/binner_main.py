
import json
"""
Base of Binner takes a set of 
arguments as bin sizes, items. Items
need to have the following traits 

This object should be used for output
of stats: including (for each bin):
Packed Items:
Space Taken:
Weight Taken:
The Packing Time:

"""
class Binner(object):
  lost_items = []
  lost_bins = []
  packed_bins = []
  smallest = {} ## only available when algorithm find_smallest is ran

  def __init__(self, args, bins, items ):
	self.args =  args
	self.bins = bins
	self.items = items

  """
  add a bin

  @param bin
  """
  def add_bin(self, bin_):
	 pass

  """
  add an item we couldnt
  find a measurement for
  
  @param: item 
  """
  def add_lost(self, item):
	 pass

  """
  get all the packed bins
  in json ready form
  """
  def get_packed_bins(self):
    bins = []
    for bin_key,bin in self.bins.items.iteritems():
      if bin.used:
         bins.append(bin.to_dict())

    return bins
    
  """
  sets the smallest bin having
  all the items per the allocation
  
  """
  def set_smallest(self, bin):
    self.smallest = bin
    
  """
  get the smallest bin out of a 
  set of bins
  """
  def get_smallest(self):
    return self.smallest

  """
  show the output
  having finished the
  algorithm
  """
  def show(self):
    from . import log
    if self.args.algorithm == "smallest":
      smallest = self.get_smallest()
      if smallest:
           result =dict(smallest=self.get_smallest().to_dict())
      else:
	   result = dict(smallest=False)
    else:
      lost_items = []
      for k, item in self.items.items.iteritems():
	  if not item.used:
	      lost_items.append( item.to_dict() )
      log.debug("Result for PACKED items")
      result = dict(lost=lost_items,
              packed=self.get_packed_bins())

      log.debug( result )
	

    return result


