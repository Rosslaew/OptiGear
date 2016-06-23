"""The different slots available in a GearSet.
"""
slots = ( #TODO use the same names as xivsync
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

"""List of all the attributes that an equipment can have.
They are written the same way as in xivdb.
"""
attributes = (
    "damage",
    "magic_damage",
    "auto_attack",
    "delay",
    "block_strength",
    "block_rate",
    "defense",
    "magic_defense",
    "Dexterity",
    "Strength",
    "Mind",
    "Intelligence",
    "Vitality",
    "Critical Hit Rate",
    "Determination",
    "Skill Speed",
    "Spell Speed",
    "Accuracy",
    "Parry",
    "Piety"
)

"""Table of attribute weights for each job.
"""
weights = { 
    "gladiator-paladin" : {
        "damage" : 9.607,
        "Strength" : 1,
        "Critical Hit Rate" : 0.152,
        "Determination" : 0.132,
        "Skill Speed" : 0.104},
    "marauder-warrior" : {
        "damage" : 9.874,
        "Strength" : 1,
        "Critical Hit Rate" : 0.151,
        "Determination" : 0.133,
        "Skill Speed" : 0.122},
    "pugilist-monk" : {
        "damage" : 10.73,
        "Strength" : 1,
        "Critical Hit Rate" : 0.161,
        "Determination" : 0.139,
        "Skill Speed" : 0.112},
    "lancer-dragoon" : {
        "damage" : 10.625,
        "Strength" : 1,
        "Critical Hit Rate" : 0.162,
        "Determination" : 0.139,
        "Skill Speed" : 0.104},
    "rogue-ninja" : {
        "damage" : 10.775,
        "Dexterity" : 1,
        "Critical Hit Rate" : 0.166,
        "Determination" : 0.141,
        "Skill Speed" : 0.074},
    "archer-bard" : {
        "damage" : 11.602,
        "Dexterity" : 1,
        "Critical Hit Rate" : 0.224,
        "Determination" : 0.14,
        "Skill Speed" : 0.111},
    "arcanist-summoner" : {
        "magic_damage" : 11.602,
        "Intelligence" : 1,
        "Critical Hit Rate" : 0.147,
        "Determination" : 0.137,
        "Spell Speed" : 0.119},
    "conjurer-whitemage" : { #TODO WHM
        },
    "arcanist-scholar" : { #TODO SCH
        },
    "darkknight-darkknight" : { #TODO DRK
        },
    "machinist-machinist" : { #TODO MCH
        },
    "thaumaturge-blackmage" : { #TODO BLM
        },
    "astrologian-astrologian" : { #TODO AST
        }
    }

"""The different jobs available."""
jobs = weights.keys()

"""Simplified job names, for use by humans
"""
full_jobs = dict(zip(
    ["SCH", "SMN", "BRD", "AST", "WHM", "DRK", "PLD",
     "DRG", "MCH", "WAR", "MNK", "NIN", "BLM"],
    sorted(jobs))
    )
