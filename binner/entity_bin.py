from .entity_object import EntityObject
from .entity_artifact import EntityArtifact
from . import log
class Bin(EntityObject,EntityArtifact):
  fields = frozenset(('w', 'h', 'd', 'max_wg', 'id', 'used'))

  def to_dict(self):
    slots = [] 
    for i in self.slots:
      slots.append(i.to_dict())

    return dict(bin=dict(id=self.id, w=self.w, h=self.h, d=self.d, initial=self.initial),
                            slots=slots)

  """
  how long did it take to satisfy space
  in this box
  """
  def time_taken():
    return e_time - s_time


  """
  weight is the bins weight + each items weight
  """
  def get_weight(self):
    weight = self.w  

    for i in self.items:
      weight += i.w

    return weight


  """
  what is the level size for the y,x, or z axis
  try to get the mininum first
  @param coord: which coordinate
  """
  def get_min_level_size(self, coord):
    sizes = []
    log.debug("Getting min level size for %s"%(coord))
    log.debug("Amount of slots %d"%(len(self.slots)))
    if len( self.slots ) > 0:
	    for i in self.slots:  
	      log.debug("Found slot size")
	      log.debug(i)
	      sizes.append(getattr(i, 'max_' + coord))

	    return min(sizes)
    return 0
  
      
  """
  same as above for max level
  size not min

  @param coord: which coordinate
  """ 
  def get_max_level_size(self, coord):
    sizes = []
    for i in self.slots:  
      sizes.append(getattr(i, 'max_' + coord))

    return max(sizes)


  """
  returns the mininum amount needed
  to be ontop of y and its position 

        @param curr a current level 
  @returns full cooords of y
  """
  def get_min_y_pos(self, curr):
    if len(self.slots)>0:
      for i in self.slots:
        if i.max_y > curr:
          return i 

    return dict(
      min_y=0,
      max_y=0,
      min_x=0,
      max_x=0,
      min_d=0,
      max_d=0
    ) 


  """
  add a new item
  to the bin. if the item
  is over the capacity
  throw an error. Otherwise
  find the optimal location
  for this item to belong

  MAKE sure the slot's item id
        is identical to the item

  @param item: item to add
  """
  def append(self, slot):
    slot.item.used=True
    if self.used!=True:
	self.used=True
    self.slots.append(slot)

  """ where would we need to be to satisfy y, """
  """ in order for our physics to remain real we need """
  """ to make sure the y level is at the right position """
  """ this does not return the optimal location, merely one """
  """ to get a valid y where x would be satisfied  """  
  def get_y_loc(self):
    pass  

  """"
  @param item: item belonging to the bin
  """
  def remove(self, item):
    for i in range(0, len(self.slots)):
      if self.slots[i].item.id == item.id:
        self.slots.pop(self.slots[i])

  """
  is a space in the box occupied?
  
  @param x: x coord
  @param y: y coord
  @param z: z coord
  @param w: items width
  @param h: items height
  @param z: items depth
  """
  def occupied(self, x, y, z, x1, y1, z1):
    occupied = False
  
    for i in self.slots:
      if x in range(i.min_x, i.max_x + 1) \
      and y in range(i.min_y, i.max_y + 1) \
      and z in range(i.min_z, i.max_z + 1):
        return True
      if x1 in range(i.min_x, i.max_x + 1) \
      and y1 in range(i.min_y, i.max_y + 1) \
      and z1 in range(i.min_z, i.max_z + 1):
        return True


    return occupied


  """
  find the level with the least 
  amount of depth remaining
  """
  def get_least_depth(self):
    pass

  """
  get the size of the bin
  w + h + d
  """
  def get_size(self):
    return self.w + self.w + self.d

  """
  space taken is defined
        by leftover coordinates / space
  
  Note: only run this having tried
  to allocate a bin
  
  @returns percentage of space
   occupied
  """
  def space_taken(self):
    pass
  def can_fit( self, item ) :
	 max_x = self.get_max_level_size("x")
	 max_y = self.get_max_level_size("y")
	 max_z = self.get_max_level_size("z")
	 item_max_x = (max_x+item.w)
	 item_max_y = (max_x+item.h)
	 item_max_z = (max_x+item.d)
	 if  (item_max_x > self.w) or (item_max_y > self.h) or (item_max_z > self.d ):
		return False
	 return True

