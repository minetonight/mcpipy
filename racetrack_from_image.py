# http://effbot.org/imagingbook/image.htm#tag-Image.Image.load

from PIL import Image

track_image = Image.open("racetrack-martincho_out_thick.png")
width, height = track_image.size
pixels = track_image.load();

print width
print height

for x in range(width):
    for y in range(height):
        print(pixels[x, y],)
        #if pixels[x, z][3] > 0:
            #mc.setBlock(x, 80, z, Block.GRAVEL)
    print ("\n")

# for x in 