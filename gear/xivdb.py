from urllib import request
import json
import ffxiv

"""Function that puts all the attributes on the same level instead of differentiating
base attributes and parametric attributes.
Also filters out the unimportant data.
"""
def flatten(data):
    # We get the data at the first level of imbrication.
    flat = dict(filter(
            lambda kv: type(kv[1]) is not dict and type(kv[1]) is not list,
            data.items()))

    # We get the base attributes
    flat.update(data["attributes_base"])

    # We then add the parametric attributes (Strength, ...)
    flat.update({d["name"] : d["value"] for d in data["attributes_params"]})

    # And finally we add the classes and jobs list
    flat["classjobs_list"] = [d["abbr"]
            for d in data["classjobs"] ]

    return flat

"""A function fetching a list of gear from xivdb matching certain conditions.
"""
def findGear(**conditions):
    pass

"""Obtain a gear data based on its id.
"""
def getId(item_id, cache={}):
    # The id should be a number.
    assert(type(item_id) == int)
    
    # Checks the cache first
    if item_id in cache :
        return cache[item_id]
    else:
        rawdata = request.urlopen("http://api.xivdb.com/item/"+str(item_id)).read()
        data = flatten(json.loads(rawdata.decode()))
        cache[item_id] = data
        return data

