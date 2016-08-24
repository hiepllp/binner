from binner.entity import Entity

class EntityObject(Entity):
   def __init__(self, args=dict()):
      super(EntityObject,self).__init__(args)
      self.initial = dict(
	 w=args['w'],
	 h=args['h'],
	 d=args['d']
	 )
   def get_size(self):
     return dict(w=self.w, h=self.h)
   def to_dict(self):
     return dict(w=self.w, h=self.h, d=self.d)



