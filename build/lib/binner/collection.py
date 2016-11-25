

"""
A generic collection
class for the objects of
bin and item type
"""
class Collection(object):
  def __init__(self, args):
    self.items = dict()
    self.tried = []
    self.it = 0
    for k,v in args.iteritems():  
        self.items[k] = self.get_entity()( v )
  def usedsize(self):
    return len(self.used)

  def size(self):
    return len(self.items)

  def last(self):
    return self.items[len(self.items) - 1]

  def first(self):
    return self.items[0]

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
     for k,  item in self.items.iteritems():
	 item.tried=False
     self.it = 0
  
  def next(self, safe=False, mode="NORMAL"):
    if not safe:
      if not (self.it) in self.items.keys():
	 item = None
      else:
         item = self.items[self.it]
         score = item.w+item.h+item.d
         if mode=="NORMAL":
		item.tried=True
         else:
	      item = None
	      for k_a, item_a in self.items.iteritems():
	  	 if item_a.tried or item_a.used:
		    continue
		 item = item_a
		 for k_b, item_b  in self.items.iteritems():
		    if item_b.tried or item_b.used:
		       continue
		    if self.mode_op( item_a, item_b, mode ):
			 item = item_b
	      if item:
		 item.tried=True
	 self.it+=1
		
    else:
      if self.it + 1> len(self.items):
        return None
      else:
        self.it += 1
      item = self.items[ self.it ] 
    return item
  
  def nextlargest_v1(self, safe=False):
    largest =  None 
    curscore= 0

    for k,i  in self.items.iteritems(): 
      if i.id in self.tried:
        continue

      score = i.w + i.h + i.d
      if score > curscore:
        curscore = score
        largest = i

    if largest:
      self.tried.append(largest.id)

    return largest
  def nextlargest_v2(self, safe=False):
	return self.next( safe=safe, mode="LARGEST" )
  def  nextlargest(self, safe=False):
	return self.nextlargest_v2(safe=safe)


  def nextsmallest_v1(self, safe=False):
    smallest = None 
    curscore = False
   
    for k, i in self.items.iteritems():
      if k in self.tried:
        continue

      score = i.w + i.h + i.d

      
      if curscore is False:
        cursore = score
        smallest = i
        self.tried.append(k)
      if score < curscore:
        curscore = score
        smallest = i
        self.tried.append(k)

    return smallest
  def nextsmallest_v2(self, safe=False):
	 return self.next( safe=safe, mode="SMALLEST" )
  def nextsmallest(self, safe=False):
	 return self.nextsmallest_v2(safe=safe)

  def find_smallest_or_largest(type='smallest'):
    curscore = False
    for k, i in self.items.iteritems():
      score = i.w+i.h+i.d
      if curscore is False:
        smallest_or_largest = i
      else:
        if type == 'smallest' and score < curscore:
          smallest_or_largest = i
          curscore = score
        if type == 'largest' and score > curscore:
          smallest_or_largest = i
          curscore = score
    return smallest_or_largest
          

  def smallest(self):
    return self.find_smallest_or_largest('smallest')

  def largest(self):
    return self.find_smallest_or_largest('largest')
  def mode_op(self, item, next_item, mode) :
	 if mode == "SMALLEST" and (next_item.w+next_item.h+next_item.d) < (item.w+item.h+item.d):
		return True
	 if mode == "LARGEST" and ( next_item.w+next_item.h+next_item.d ) > (item.w+item.h+item.d ):
		return True
	 return False
    

