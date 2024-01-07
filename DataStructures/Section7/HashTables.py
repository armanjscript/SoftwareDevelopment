#preventing collisions in hash ord by multiplying the ordinal numbers

def myhash(item):
    mult=1
    hv=0

    for ch in item:
        hv += mult*ord(ch)
        mult+=1
    return hv 