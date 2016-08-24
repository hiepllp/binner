
"""
Given a set of Bins and Items
find the best estimate according
to the sizes, and area needing to
be traversed
@attributes: defines a set
of longitude, latitude coordinates
with the provided objects 

"""
class Estimate(object):
  fields = frozenset(('f_lng', 'f_lat', 't_lng', 't_lat'))
  def __init__(self, **args):
    pass


