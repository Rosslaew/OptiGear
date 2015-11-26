import ffxiv

"""Function to calculate the power of a gear for job.
"""
def power(gear, job):
    return sum([int(gear.attributes.get(k,0))*v
        for k,v in ffxiv.weights[job].items()])


