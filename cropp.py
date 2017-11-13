from PIL import Image

def crop_image(difficulty):
    img = Image.open("test.png")
    original_width, original_height = img.size
    cropped_img = []
    for i in range(difficulty):
        for j in range(difficulty):
            area = (original_width/difficulty*i, original_height/difficulty*j, original_width/difficulty*(i+1), original_height/difficulty*(j+1))
            cropped_img.append(img.crop(area))
    return cropped_img