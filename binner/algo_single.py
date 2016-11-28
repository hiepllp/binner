from .algo import Algo
from .entity_slot import Slot
from  . import log
import time
class AlgoSingle(Algo):
  """
  pack items into a single
  bin

  for single bin packing we merely
  need to operate on one bin. Don't
  accept input bins larger than size one

  @param itemcollection: set of items
  @returns one bin packed with items
  """
  def run(self):
    log.debug("Entering algorithm SINGLE")
    bincollection = self.bins
    itemcollection =self.items
    assert(len(bincollection.items) == 1)

    curbin = bincollection.next()
    first = True
    
    while curbin != None:
    
      if not first:
        curbin = bincollection.next()
      first = False

      if curbin is None:
        break
      log.info("Trying to allocate items for bin: {0}".format(curbin.id))

      itemcollection.reset()
      curbin.s_time = time.time()
      while True:
        last = False
	item = itemcollection.next()
	if not item:
	    break
	if not curbin.can_fit( item ) :
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
  
 
        log.info( "adding a box at: x: {0}, mx: {1}, y: {2}, my: {3}, z: {4}, mz: {5}".format(curx, curx + item.w, cury, cury + item.w, curd, curd + item.d) )

        if last:
          break

        slot = Slot(dict(min_x=curx,
           min_y=cury, 
          min_z=curd, 
          item=item,
          max_x=curx + item.w,
          max_y=cury + item.h,
          max_z=curd + item.d
        ))

        curbin.append(slot)

      curbin.e_time = time.time()

    return self.binner


