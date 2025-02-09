import images
def grayscale_luminosity(image:images.Image):
    """Converts the argument image to grayscale based on luminosity."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def grayscale_average(image:images.Image):
    """Converts the argument image to grayscale based on average."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            avg = int((r + g + b) / 3)
            image.setPixel(x, y, (avg, avg, avg))
n=input("""Select file to compare:
1. 1.gif (red/blue/green stripes)
2. Smokey.gif""")
if n=='2':
    FILE='Smokey.gif'
else:
    FILE='1.gif'
image0=images.Image(FILE)
image1=image0.clone()
image2=image0.clone()
grayscale_luminosity(image1)
grayscale_average(image2)
x=image1.getWidth()
y=image1.getHeight()

image3=images.Image(x*2,y*2)
for xd in range(x):
    for yd in range(y):
        (r1,g1,b1)=image1.getPixel(xd,yd)
        (r2,g2,b2)=image2.getPixel(xd,yd)
        image3.setPixel(xd,yd,(r1,g1,b1))
        image3.setPixel(xd+x,yd,(r2,g2,b2))
image3.draw()