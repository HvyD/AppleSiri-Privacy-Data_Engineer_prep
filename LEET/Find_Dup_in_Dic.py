# O(N)

def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out

d = {'hello': 3 , 'world':{'this': 5 , 'is':{'a': 3, 'dict': None}}}
v = flatten(d).values()

if len(set(v))!=len(v):
    print(v)





# List O(log N)


dictionary = {'hello': 3 , 'world':{'this': 5 , 'is':{'a': 3, 'dict': None}}}

def get_dups(a, values=None):
    if values is None: values = []
    if (a in values): return values
    values.append(a)
    if type(a) == dict:
        for i in a.values():
            if (get_dups(i, values=values)):
                return True
    return False

print(get_dups(dictionary))
