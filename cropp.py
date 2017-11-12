from PIL import Image

img = Image.open("test.png")
width, height = img.size
area = (0, 0, width/2, height/2)
cropped_img = img.crop(area)
img.show()
cropped_img.show()

def