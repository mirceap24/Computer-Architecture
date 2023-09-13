import re
import sys

# Dictionary to map hexadecimal digits to their decimal counterparts
d = dict(zip('0123456789abcdef', range(16)))

def xx_to_dec(xx):
    """Convert two-character hexadecimal to its decimal value."""
    return (d[xx[0]] << 4) + d[xx[1]]

def hex_to_rgb(r):
    """Convert hexadecimal color codes to RGB or RGBA format."""
    # Convert the matched hexadecimal color code to lowercase
    hx = r.group(1).lower()
    
    # If the color code is in the short format (e.g., #ABC), expand it to the full format (e.g., #AABBCC)
    if len(hx) in {3, 4}:
        hx = ''.join(x + x for x in hx)
    
    # Extract the decimal values for the red, green, and blue parts of the color
    dec = [xx_to_dec(hx[i: i + 2]) for i in (0, 2, 4)]
    
    # Determine if the output should be in RGB or RGBA format
    if len(hx) == 6:
        label = 'rgb'
    elif len(hx) == 8:
        label = 'rgba'
        # Add the alpha channel if present, normalizing it to a 0-1 range
        dec.append(xx_to_dec(hx[6:]) / 255)
    else:
        # If the hex code doesn't fit known formats, return it as-is
        return f'#{hx}' 

    # Convert the decimal values to a string and return in the appropriate format
    return f'{label}({", ".join(str(d) for d in dec)})'

# Read from stdin, replace all hex color codes with their RGB or RGBA counterparts, and write to stdout
sys.stdout.write(re.sub(r'\#([0-9a-fA-F]+)', hex_to_rgb, sys.stdin.read()))
