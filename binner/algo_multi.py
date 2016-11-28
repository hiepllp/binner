
from .algo import Algo 
from .entity_slot import Slot
from . import log

import time
class AlgoMulti(Algo):
  """
  pack items into multiple
  bins. Bins should follow FIFO
        algorithm

  @param itemcollection: set of items
  @returns bins with items
  """ 
  def run(self):
    log.debug("Entering Algorithm MULTI")
    itemcollection = self.items
    bincollection = self.bins
    assert(itemcollection.size() >= bincollection.size())

    curbin = self.get_next_bin()
    bincollection.it = 1
    first = True
    while curbin != None:
      if not first:
        curbin = self.get_next_bin()
      first = False

      if curbin is None:
        break

      log.info("Packing Bin #{0}".format(curbin.id))
      curbin.s_time = time.time() 
      itemcollection.reset()
      while True:
        last = False
  	item = itemcollection.nextlargest()
	if not item:
	    break

        """ using heuristics, rotate and see if we occupy less room """
        #item.rotate()
	if not curbin.can_fit( item ):
	   continue

        curx = 0
        cury = 0
        curd = 0
   
        """ if item.w > curbin.w: """
        """ self.binner.add_lost(item) """
        while curbin.occupied(curx + 1, cury + 1, curd + 1, curx + item.w + 1, cury + item.h + 1, item.d + curd + 1):
          b_d = curbin.get_min_level_size('z') 
          b_x = curbin.get_min_level_size('x') 
          b_y = curbin.get_min_level_size('y')
          m_y = curbin.get_min_y_pos(cury)
          #m_y = curbin.slots[0]

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
  
        log.info("adding a box at: x: {0}, mx: {1}, y: {2}, my: {3}, z: {4}, mz: {5}".format(curx, curx + item.w, cury, cury + item.w, curd, curd + item.d))


        slot = Slot(dict(min_x=curx,
           min_y=cury, 
          min_z=curd, 
          item=item,
          max_x=curx + item.w,
          max_y=cury + item.h,
          max_z=curd + item.d
        ))

        curbin.append(slot)

        #item2 = itemcollection.nextsmallest()
    
      curbin.e_time = time.time()

    return self.binner  


	   
