from PIL import Image

with open("config.cfg") as fp:
    name, low, high = fp.read().split()
    
image = Image.open(name)

h = image.height
w = image.width

low = int(low)
high = int(high)

px = image.load()
for i in range(w):
    for j in range(h):
        val = sum(px[i, j])/3
        if val < low:
            px[i, j] = (0, 0, 0)
        elif val > high:
            px[i, j] = (255, 255, 255)
        else:
            if (i+j)%2:
                px[i, j] = (0, 0, 0)
            else:
                px[i, j] = (255, 255, 255)
                

image = image.resize((w//5, h//5))
image = image.resize((w, h), Image.NEAREST)
image.save("out.jpg")
