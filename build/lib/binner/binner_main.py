
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

  def __init__(self):
    pass

  """
  add a bin

  @param bin
  """
  def add_bin(self, bin_):
    self.packed_bins.append(bin_)

  """
  add an item we couldnt
  find a measurement for
  
  @param: item 
  """
  def add_lost(self, item):
    self.lost_items.append(item)

  """
  get all the packed bins
  in json ready form
  """
  def get_packed_bins(self):
    bins = []
    for i in self.packed_bins:
      bins.append(i.to_dict())

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
    if self.smallest:
      result =dict(smallest=self.get_smallest().to_dict())
    else:
      result = dict(lost=self.lost_items,
              packed=self.get_packed_bins())

    return result


