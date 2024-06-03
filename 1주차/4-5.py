def cntCroatia(_str):
    croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
    for cr in croatia:
        _str = _str.replace(cr, '#')
    return len(_str)

_str = input()
print(cntCroatia(_str))
