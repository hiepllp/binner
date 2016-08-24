from binner.collection import Collection
from binner.entity_item import Item
class ItemCollection(Collection):
   def __init__(self,args):
	 super(ItemCollection,self).__init__(args)
   def get_entity(self):
	 return Item
