from .entity_artifact import EntityArtifact
class Slot(EntityArtifact):
  fields = frozenset(('x', 'y', 'z'))
  min_x = 0
  max_x = 0
  min_y = 0
  max_y = 0
  min_z = 0 
  max_z = 0
  item = None

  def to_dict( self ):
	return dict(
		item=self.item.to_dict(),
		id=self.id,
		min_x=self.min_x,
		max_x=self.max_x,
		min_y=self.min_y,
		max_y=self.max_y,
		min_z=self.min_z,
		max_z=self.max_z )
  def get_coords(self):
    return self.get_position()


