from collections import UserList
import ffxiv
import power as p

"""Class representing a simple gear element.
"""
class Gear(object):
    """Gear(slot, item_id, **attributes)

    slot : in which slot of the gearset is this precise gear, as defined
           in ffxiv.slots.
    item_id : identifier from xivdb.com. Will load the gear
              from there if provided
    attributes : the attributes of the gear as defined in ffxiv.attributes.
    """
    def __init__(self, slot, item_id = None, **attributes):
        if item_id is None :
            self.slot = slot
            for att in ffxiv.attributes:
                self.__setattr__(att,attributes[att])
        else:
            pass #TODO add fetching gear from xivdb

"""Class representing a complete gear set.
    Can be called by specifying the Lodestone ID for
    the character or by specifying the gear
    for each gear slot, as defined in ffxiv.slots.
"""
class GearSet(Gear):
    """GearSet(character_id, **gears)

    character_id : provide to load gearset from Lodestone.
    gears : pairs slot=Gear
    """
    def __init__(self, 
            character_id=None,
            **gears
            ):
        self.gears = {}

        # If we do not fetch the gearset from Lodestone
        if character_id is None:
            for s in ffxiv.slots:
                g = gears.get(s)
                assert(g is None or g.slot == s)
                self.gear[s] = g
        else:
            pass #TODO add fetching gearset from Lodestone

        # A GearSet is treated as a Gear, so we update the attributes
        attributes = { k : sum(
            [getattr(g,k,default=0) 
                for g in self.gears.values() if g is not None
            ], start=0)
            for k in ffxiv.attributes}
        super().__init__(None,*attributes)

"""List of GearSets to compare.
"""
class GearSetList(UserList):
    """GearSetList(data)

    data : an iterable of gearsets
    """
    def __init__(self, data=[]):
        super().__init__(data)

    """maxPower(job,consraintList)
    Returns the best gearset for job given a list of constraints.
    """
    def maxPower(self,job, constraintList=None):
        pass
