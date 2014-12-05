"""
Binner: A Shipment Bin Packing API
This is a free program and can be
distributed, copied under the MIT
license

Ongoing development here:
http://github.com/nadirhamid/binner

Written by: Nadir Hamid
"""

import time
import json
import sys
import os
import pprint

try:
	import cherrypy
except:
	pass ## no RuntimeAPI

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

	def get_size():
		return dict(w=self.w, h=self.h)

	def get_position():
		return dict(x=self.x, y=self.y, z=self.z)

"""
Represent a Bin needing
packing. Where attributes are

@attribute w: width
@attribute h: height
@attribute d: dimension
@attribute wg: wg
@attribute id: id

"""
class Bin(Entity):
	fields = frozenset(('w', 'h', 'd', 'max_wg', 'id'))

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
		for i in self.slots:	
			sizes.append(getattr(i, 'max_' + coord))

		return min(sizes)
	
			
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
		for i in self.slots:
			if i.max_y > curr:
				return i 

		return None


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
	def append(self, item, slot):
		assert(slot.item_id == item.id)
		self.items.append(item)
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
		for i in range(0, len(self.items)):
			if self.items[i].id == item.id:
				self.items.pop(self.items[i])
		for i in range(0, len(self.slots)):
			if self.slots[i].item_id == item.id:
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



"""
A slot is space that is currently
occupied within a bin. Slots should
be tied to items. Difference being slots 
are coordinate based
and not size based
"""
class Slot(Entity):
	min_x = 0
	max_x = 0
	min_y = 0
	max_y = 0
	min_z = 0 
	max_z = 0
	item_id = ''

	def get_coords(self):
		return dict(x=self.x,y=self.y,z=self.z)

	

"""
A generic collection
class for the objects of
bin and item type
"""
class Collection(object):
	#used = []
	def __init__(self, args):
		cnt = 0
		self.items = dict()
		self.ids = dict()
		self.used = []
		self.it = 0

		for k,v in args.iteritems():	
			if isinstance(self, ItemCollection):
				self.items[cnt] = Item(v)
				self.obj = Item
			elif isinstance(self, BinCollection):
				self.items[cnt] = Bin(v)
				self.obj = Bin

			self.ids[cnt] = k

			cnt += 1

	def usedsize(self):
		return len(self.used)

	def size(self):
		return len(self.items)

	def last(self):
		return self.items[len(self.items) - 1]

	def first(self):
		return self.items[self.ids[0]]

	def get(self, i):
		return self.items[i]

	def prev(self):
 		if self.it == -1:	
			return None
		else:
			self.it -= 1

		return self.items[self.it]

	def find(self, **attrs):
		pass

	def reset(self):
		self.it = 0
	
	def next(self, safe=False):
		if not safe:
			while self.it in self.used:
				self.it += 1
				if self.it + 1> len(self.items):
					return None

			self.used.append(self.it)
		else:
			if self.it + 1>= len(self.items):
				return None
			else:
				self.it += 1
			
		return self.items[self.ids[self.it]]

	def nextlargest(self, safe=False):
		largest =  None	
		curscore= 0

		for k,i  in self.items.iteritems(): 
			if i.id in self.used:
				continue

			score = i.w + i.h + i.d
			if score > curscore:
				curscore = score
				largest = i
				self.used.append(i.id)

		return largest


	def nextsmallest(self):
		smallest = None 
		curscore = False
		
		for k, i in self.items.iteritems():
			if i in self.used:
				continue

			score = i.w + i.h + i.d

			
			if not 'curscore' is False:
				cursore = score
				smallest = i
				self.used.append(k)
			if score < curscore:
				cursore = score
				smallest = i
				self.used.append(k)


		return smallest

	def smallest(self):
		pass

	def largest(self):
		pass
		

"""
a collection for all
bins.
"""	
class BinCollection(Collection):
	pass

"""
a collection for all
items
"""
class ItemCollection(Collection):
	pass

"""
Represents a single item in
binner. Where attributes are

@attribute w: width
@attribute h: height
@attribute d: dimension
@attribute wg: wg
@attribute id: unique id
"""
class Item(Entity):
	fields = frozenset(('w', 'h', 'd', 'q', 'm ', 'vr', 'wg', 'id'))

	"""
	turn an item horizantal 
        this will only 
        turn height into width and
        vice versa
	"""
	def rotate(self):
              w,h = self.w,self.h
              self.h = w
              self.w = h

              if self.d == w:
	      	self.d = h
	      else:
		self.d = w
                      	

	
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

"""
A Set of algorithms to find
smallestbin size, multi bin packing
and single bin packing

Definitions:
find optimal:
each area in a bin is set as a level whenever
the 'first' item is added to it. As a result
if we have a bin with size: 10, 10, 10 and
item one being 3, 3, 3. The subsequent item
must allocate space proportianate to its relatives
coordinates

TRY to move to x axis as much as possible before
creating another level. Additionally try to rotate
vertically, and horizontal for a optimal fit.

"""
class Algo(object):
	def __init__(self, **args):
		self.binner = Binner()

	"""
	makes sure the leftovr bins and
	items are placed in their
	right object
	
	@param bins: BinCollection
	@param items: ItemCollection
	"""
	def _cleanup(self):
		pass
		
	
	
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
	
	def find_smallest_bin(self, itemcollection, bincollection):
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
				item = itemcollection.next(True) ## safe on

				if item is None:
					break

				curx = 0
				cury = 0
				curd = 0
		
				""" if item.w > curbin.w: """
				""" self.binner.add_lost(item) """
				
				while curbin.occupied(curx + 1, cury + 1, curd + 1, curx + item.w + 1, cury + item.h + 1, item.d + curd + 1):
					b_d = curbin.get_min_level_size('z') 
					b_x = curbin.get_min_level_size('x') 
					b_y = curbin.get_min_level_size('y')
					#m_y = curbin.get_min_y_pos(cury)
					m_y = curbin.slots[0]

					if curx + item.w > curbin.w:
						""" try z now """
						curd += item.d 
						curx = 0
					else: 
						curx += 1


					""" if curd fails and so does  curx """
					""" go up in height make sure y	 """
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
	
	
				print "adding a box at: x: {0}, mx: {1}, y: {2}, my: {3}, z: {4}, mz: {5}".format(curx, curx + item.w, cury, cury + item.w, curd, curd + item.d)

				if last:
					break

				slot = Slot(dict(min_x=curx,
					 min_y=cury, 
					min_z=curd, 
					item_id=item.id,
					max_x=curx + item.w,
					max_y=cury + item.h,
					max_z=curd + item.d
				))

				curbin.append(item, slot)

			curbin.e_time = time.time()
			self.binner.add_bin(curbin)
			
		"""
		to be the smallest bin we
		must allocate all space of the
		bin and be the smallest in size
		"""
		smallest = False
		for i in self.binner.packed_bins:
			if not smallest:
				if len(i.items) + 1 == itemcollection.size():
					self.binner.set_smallest(i)
			if i.get_size() < smallest or not smallest:
				if len(i.items) + 1 == itemcollection.size():
					self.binner.set_smallest(i)

		return self.binner
		
		
	"""
	pack items into a single
	bin

	for single bin packing we merely
	need to operate on one bin. Don't
	accept input bins larger than size one

	@param itemcollection: set of items
    @returns one bin packed with items
	"""
	def single_bin_packing(self, itemcollection,bincollection):
		assert(bincollection.items == 1)

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
				item = itemcollection.next(True) ## safe on

				if item is None:
					break

				curx = 0
				cury = 0
				curd = 0
		
				""" if item.w > curbin.w: """
				""" self.binner.add_lost(item) """
				
				while curbin.occupied(curx + 1, cury + 1, curd + 1, curx + item.w + 1, cury + item.h + 1, item.d + curd + 1):
					b_d = curbin.get_min_level_size('z') 
					b_x = curbin.get_min_level_size('x') 
					b_y = curbin.get_min_level_size('y')
					#m_y = curbin.get_min_y_pos(cury)
					m_y = curbin.slots[0]

					if curx + item.w > curbin.w:
						""" try z now """
						curd += item.d 
						curx = 0
					else: 
						curx += 1


					""" if curd fails and so does  curx """
					""" go up in height make sure y	 """
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
	
	
				print "adding a box at: x: {0}, mx: {1}, y: {2}, my: {3}, z: {4}, mz: {5}".format(curx, curx + item.w, cury, cury + item.w, curd, curd + item.d)

				if last:
					break

				slot = Slot(dict(min_x=curx,
					 min_y=cury, 
					min_z=curd, 
					item_id=item.id,
					max_x=curx + item.w,
					max_y=cury + item.h,
					max_z=curd + item.d
				))

				curbin.append(item, slot)

			curbin.e_time = time.time()
			self.binner.add_bin(curbin)

		return self.binner


	"""
	pack items into multiple
	bins. Bins should follow FIFO
        algorithm

	@param itemcollection: set of items
	@returns bins with items
	"""	
	def multi_bin_packing(self, itemcollection,bincollection,bins=1):
		assert(itemcollection.size() >= bincollection.size())

		curbin = bincollection.first()
		bincollection.it = 1
		first = True
		while curbin != None:
			if not first:
				curbin = bincollection.next()
			first = False

			if curbin is None:
				break

			print "Packing Bin #{0}".format(curbin.id)
			curbin.s_time = time.time()

			while True:
				last = False

				item = itemcollection.nextlargest()

				""" using heuristics, rotate and see if we occupy less room """
				#item.rotate()
				if item is None:
					break

				curx = 0
				cury = 0
				curd = 0
		
				""" if item.w > curbin.w: """
				""" self.binner.add_lost(item) """


				while curbin.occupied(curx + 1, cury + 1, curd + 1, curx + item.w + 1, cury + item.h + 1, item.d + curd + 1):
					b_d = curbin.get_min_level_size('z') 
					b_x = curbin.get_min_level_size('x') 
					b_y = curbin.get_min_level_size('y')
					#m_y = curbin.get_min_y_pos(cury)
					m_y = curbin.slots[0]

					if curx + item.w > curbin.w:
						""" try z now """
						curd += item.d 
						curx = 0
					else: 
						curx += 1


					""" if curd fails and so does  curx """
					""" go up in height make sure y	 """
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
					max_z=curd + item.d
				))

				curbin.append(item, slot)

				#item2 = itemcollection.nextsmallest()
		
			self.binner.add_bin(bin)	
			curbin.e_time = time.time()

		return self.binner	



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
	def add_bin(self, bin):
		self.packed_bins.append(bin)

	"""
	add an item we couldnt
	find a measurement for
	
	@param: item 
	"""
	def add_lost(self, item):
		self.lost_items.append(item)
		
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
		j = json.dumps(dict(lost=self.lost_items,
				    packed=self.packed_bins))

		return j


"""
A API based RPC. Where this program
will act as a RESTful client
responding to requests.
Use CherryPy
to run via HTTP

@methods GET, POST
"""
class RuntimeAPI(object):
	def __init__(self,a):
		pass
		
	@cherrypy.expose
	def smallest(self, **params):
		try:	
			items = json.loads(enumerate_json(cherrypy.request.params['items']))
			bins = json.loads(enumerate_json(cherrypy.request.params['bins']))
			
			return Algo().find_smallest_bin(ItemCollection(items), BinCollection(bins)).smallest()		
		except:
			return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""

	@cherrypy.expose
	def single(self, **params):
		try:
			items = json.loads(enumerate_json(cherrypy.request.params['items']))
			bins = json.loads(enumerate_json(cherrypy.request.params['bins']))
			
			return Algo().single_bin_packing(ItemCollection(items), BinCollection(bins)).smallest()
		except:
			return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""
			
	@cherrypy.expose
	def multi(self, **params):
		try:
			items = json.loads(enumerate_json(cherrypy.request.params['items']))
			bins = json.loads(enumerate_json(cherrypy.request.params['bins']))
			
			return Algo().multi_bin_packing(ItemCollection(items), BinCollection(bins)).smallest()
		except:
			return r"""{"status": "error", 'message="Please add properties 'bins' and 'items' to your JSON objects."}"""
		
	@cherrypy.expose
	def index(self, **params):
			return """<h1>Welcome to the Binner API</1>
			<br>
			to use you go to any of these links:
			<br>
			"""
			
""" for loaded json enumerate it to fit auto increment style ids """
def enumerate_json(json):
        o = []
        c = 0
	for i in json:
            o.append(i)
            c+=1 

        return o


"""
Straight forward command line usage
of program. 
"""
class RuntimeCLI(object):
	def __init__(self, *args):
		a = args

		for _i in range(0, len(a)):
			i = a[_i]
			try:
				j = a[_i + 1]
			except:
				j = a[_i]
				
			if i in ['-bin', '--bins']:
				self.bins = j 
			if i in ['-i', '--items']:
				self.items = j 
			if i in ['-a', '--algorithm']:
				self.algorithm = j
			if i in ['-h', '--help']:
				self._help()
				
	def _help(self):
		print """
usage: binner {web|cli} required_input required_input2
options:

SERVER SPECIFIC
--bins Bins to use
--items Items to pack
--algorithm What algorithm to use
"""
	
	def run(self):
		bins = BinCollection(enumerate_json(json.loads(self.bins)))
		items = ItemCollection(enumerate_json(json.loads(self.items)))

		if self.algorithm == 'multi':
			binner = Algo().single_bin_packing(items, bins)
		elif self.algorithm == 'single':
			binner = Algo().multi_bin_packing(items, bins)
		else:
			binner = Algo().find_smallest_bin(items)

		binner.show()


class Runtime(object):
	def __init__(self, *args):
		a = args
		first = a[0][1]

		if first == 'web':
			cherrypy.quickstart(RuntimeAPI(sys.argv))
		else:
			RuntimeCLI(a[0][2:])

if __name__ == '__main__':
	Runtime(sys.argv)
