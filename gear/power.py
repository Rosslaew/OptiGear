import ffxiv

"""Function to get the weight of the attributes
of a certain job.
"""
def weights(job):
    return ffxiv.weights[job]

"""Function to calculate the power of a gear for job.
"""
def power(gear, job):
    return sum([getattr(a,k)*v
        for k,v in weights(job).items()])


