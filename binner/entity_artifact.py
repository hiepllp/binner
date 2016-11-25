from .entity import Entity
class EntityArtifact(Entity):
  def get_coords(self):
    return dict(x=self.x, y=self.y, z=self.z)
  def to_dict(self):
    return dict(x=self.x, y=self.y, z=self.z)
  
