"""
Represent traits to get
information on an item, or bin
"""

class Entity(object):
  def __init__(self, args=dict()):
    for k,v in args.iteritems():
      setattr(self, k, v)
    self.slots = []
    self.items = []
