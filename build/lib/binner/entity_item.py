from .entity_object import EntityObject
from .entity_artifact import EntityArtifact
class Item(EntityObject,EntityArtifact):
  fields = frozenset(('w', 'h', 'd', 'q', 'm ', 'vr', 'wg', 'id'))

  """
  turn an item horizantal 
        this will only 
        turn height into width and
        vice versa
  """
  def rotate(self):
    w,h = int(self.w),int(self.h)
    self.h = int(w)
    self.w = int(h)

    if self.d == w:
      self.d = int(h)
    else:
      self.d = w
  def to_dict(self):
	return EntityObject.to_dict(self)

