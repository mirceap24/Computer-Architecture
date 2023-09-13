"""
1. Read from stdin, search/replace hex, write to stdout 
2. Convert hex to rgb form to cover simple.css 
3. Fix advanced.css 
"""

import re
import sys 

d = dict(zip('0123456789abcdef', range(16)))


def xx_to_dec(xx):
    return (d[xx[0]] << 4) + d[xx[1]]


def hex_to_rgb(r):
    hx = r.group(1).lower()
    if len(hx) in {3, 4}:
        hx = ''.join(x + x for x in hx)
    dec = [xx_to_dec(hx[i: i + 2]) for i in (0, 2, 4)]
    if len(hx) == 6:
        label = 'rgb'
    elif len(hx) == 8:
        label = 'rgba'
        dec.append(xx_to_dec(hx[6:]) / 255)
    else:
        return f'#{hx}' 
    return f'rgb({" ".join(str(d) for d in dec)})'

sys.stdout.write(re.sub(r'\#([0-9a-fA-F]+)', hex_to_rgb, sys.stdin.read()))