from collections import UserList
import power as p

"""Global definition of attributes and gear slots."""
__slots__ = (
    "weapon",
    "head",
    "body",
    "belt",
    "legs",
    "feet",
    "shield",
    "neck",
    "ears",
    "arm",
    "ring1",
    "ring2")

__attributes__ = (
    "weapon_damage",
    "auto_attack",
    "delay",
    "block_strength",
    "block_rate",
    "physical_defense",
    "magical_defense",
    "dexterity",
    "strength",
    "mind",
    "intelligence",
    "vitality",
    "critical",
    "determination",
    "skill_speed",
    "spell_speed",
    "accuracy",
    "parry",
    "piety"
        )

"""Class representing a simple gear element.
"""
class Gear(object):
    def __init__(self, slot, item_id = None, **attributes):
        if item_id is None :
            self.slot = slot
            for att in __attributes__:
                self.__setattr__(att,attributes[att])
        else:
            pass #TODO add fetching gear from xivdb

"""Class representing a complete gear set.
    Can be called by specifying the Lodestone ID for
    the character or by specifying the gear
    for each gear slot.

    Available slots :
    weapon
    head
    body
    belt
    legs
    feet
    shield
    neck
    ears
    arm
    ring1
    ring2
"""
class GearSet(Gear):
    def __init__(self, 
            character_id=None,
            **gears
            ):
        self.gears = {}
        if character_id is None:
            for s in __slots__:
                self.gear[s] = gears[s]
                self.gear[s].slot = s
        else:
            pass #TODO add fetching gearset from Lodestone

        # A GearSet is treated as a Gear, so we update the attributes
        attributes = {} # TODO find an elegant way to do this
        for g in gears:
            pass



class GearSetList(UserList):
    def __init__(self, data=[]):
        super().__init__(data)

    def maxPower(self,job, constraintList=None):
        pass
