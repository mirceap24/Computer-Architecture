
def little_endian(bs):
    n = 0
    for i, b in enumerate(bs):
        n += (b << (i * 8))
    return n

with open('image-rotate/teapot.bmp', 'rb') as f:
    data = f.read()

assert data[:2] == b'BM'

offset, width, height = little_endian(data[10:14]), little_endian(data[18:22]), little_endian(data[22:26])
print(offset, width, height)

pixels = []
for ty in range(width):
    for tx in range(width):
        sy = tx 
        sx = width - ty - 1 
        n = offset + 3 * (sy * width + sx)
        pixels.append(data[n : n + 3])

with open('out.bmp', 'wb') as f:
    f.write(data[:offset])
    f.write(b''.join(pixels))