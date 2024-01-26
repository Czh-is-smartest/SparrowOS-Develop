from PIL import Image
i = Image.open("cursors.bmp")
for x in range(16):
    print('"', end='')
    for y in range(16):
        if i.getpixel((y, x)) == (0, 0, 0):
            print('*', end='')
        else:
            print('.', end='')
    print('",')