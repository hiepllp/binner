from binner.algo import Algo
from binner.entity_slot import Slot
import time
class AlgoSmallest(Algo):
  """
  find the smallest bin
  for a given amount of 
  bins.

  Output SHOULD try to have all
  the items. I.e 

  A bin smaller bin with less items is worse than 
  A bigger bin with more items

  @param itemcollection: set of items

  @returns a Bin object
         whose size is smallest with the most
         amount of items 
  """
  
  def run(self):
    bincollection = self.bins
    itemcollection = self.items
    curbin = bincollection.first()
    first = True
    while curbin != None:
    
      if not first:
        curbin = bincollection.next()
      first = False

      if curbin is None:
        break
      print "Trying to allocate items for bin: {0}".format(curbin.id)

      itemcollection.reset()
      curbin.s_time = time.time()
      while True: 
        last = False
        item = itemcollection.next()
        if item is None:
          break

        curx = 0
        cury = 0
        curd = 0
    
        """ if item.w > curbin.w: """
        """ self.binner.add_lost(item) """
        while curbin.occupied(curx + 1, cury + 1, curd + 1, curx + item.w + 1, cury + item.h + 1, item.d + curd + 1):
          last = False
          b_d = curbin.get_min_level_size('z') 
          b_x = curbin.get_min_level_size('x') 

          b_y = curbin.get_min_level_size('y')
          m_y = curbin.get_min_y_pos(cury)

          if curx + item.w > curbin.w:
            """ try z now """
            curd += item.d 
            curx = 0
          else: 
            curx += 1


          """ if curd fails and so does  curx """
          """ go up in height make sure y  """
          """ is at the proper juxtaposition """
          if curd + item.d > curbin.d:
            cury += m_y.max_y
            curx = m_y.min_x
            curd = m_y.min_z

          """ if were at the top of the box """
          """ we cannot allocate any more space so we can move on """

          if int(cury + item.h) > curbin.h:
            last = True
            break
  
 
        if last: 
          break
        print "adding a box at: x: {0}, mx: {1}, y: {2}, my: {3}, z: {4}, mz: {5}".format(curx, curx + item.w, cury, cury + item.w, curd, curd + item.d)
        slot = Slot(dict(min_x=curx, 
          min_y=cury,
          min_z=curd,
          item_id=item.id,
          max_x=curx + item.w,
          max_y=cury + item.h,
          max_z=curd + item.d))
        curbin.append(item, slot)
        curbin.e_time =time.time()
      self.binner.add_bin(curbin)
      
    """
    to be the smallest bin we
    must allocate all space of the
    bin and be the smallest in size
    """
    smallest = -1 
    if len(self.binner.packed_bins) > 0:
      for i in self.binner.packed_bins:
        if smallest < 0:
          if len(i.items) == itemcollection.size():
            self.binner.set_smallest(i)
            smallest = i.get_size()
        if i.get_size() < smallest:
          if len(i.items) == itemcollection.size():
            smallest = i.get_size()
            self.binner.set_smallest(i)
    else:
      smallest = dict(result="No match found")
      self.binner.set_smallest(smallest)

    return self.binner

