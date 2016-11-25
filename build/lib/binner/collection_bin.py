from .collection import Collection
from .entity_bin import Bin

class BinCollection(Collection):
   def __init__(self,args):
	 super(BinCollection,self).__init__(args)
   def get_entity(self):
	 return Bin
