from PIL import Image, ImageTk


def crop_image(difficulty):
    img = Image.open("test.png")
    blank = Image.open("blank.png")
    original_width, original_height = img.size
    cropped_img = []
    for j in range(difficulty):
        for i in range(difficulty):
            area = (original_width/difficulty*i, original_height/difficulty*j, original_width/difficulty*(i+1), original_height/difficulty*(j+1))
            if i == 0 and j == 0:
                temp = ImageTk.PhotoImage(blank.crop(area))
            else:
                temp = ImageTk.PhotoImage(img.crop(area))
            cropped_img.append(temp)
    return cropped_img