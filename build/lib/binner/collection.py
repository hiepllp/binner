

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
        self.items[cnt] = self.get_entity()( v )
        self.ids[cnt] = k

        cnt += 1

  def usedsize(self):
    return len(self.used)

  def size(self):
    return len(self.items)

  def last(self):
    return self.items[len(self.items) - 1]

  def first(self):
    self.used.append(self.it)
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
    self.used = []
    self.it = 0
  
  def next(self, safe=False):
    if not safe:
      while self.it in self.used:
        self.it += 1
        if self.it + 1> len(self.items):
          return None

      self.used.append(self.it)
    else:
      if self.it + 1> len(self.items):
        return None
      else:
        self.it += 1
  
    if self.it in self.ids.keys():
      return self.items[self.ids[self.it]]
    else:
      return None

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

    if largest:
      self.used.append(largest.id)

    return largest


  def nextsmallest(self):
    smallest = None 
    curscore = False
    
    for k, i in self.items.iteritems():
      if i in self.used:
        continue

      score = i.w + i.h + i.d

      
      if not curscore is False:
        cursore = score
        smallest = i
        self.used.append(k)
      if score < curscore:
        curscore = score
        smallest = i
        self.used.append(k)


    return smallest

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
    

