from binner.entity_artifact import EntityArtifact
class Slot(EntityArtifact):
  fields = frozenset(('x', 'y', 'z'))
  min_x = 0
  max_x = 0
  min_y = 0
  max_y = 0
  min_z = 0 
  max_z = 0
  item_id = ''

  def get_coords(self):
    return self.get_position()


