from PIL import Image, ImageDraw, ImageFont
import math
from pathlib import Path

def find_nearest_space(text: list, index: int, s_range: int) -> int:
    index -= 1
    for offset in range(0, s_range//2):
            
            if text[index - offset] == " ":
                return index - offset
            
            elif text[index + offset] == " ":
                 return index + offset
    return 0


def line_split(text: str) -> str:
    words = text.split(" ")
    text_list = list(text)

    if len(words) > 3:

        length = len(text)
        line_len = math.ceil(length / 3)

        br1 = find_nearest_space(text_list, line_len, line_len)
        text_list[br1] = "\n"

        br2 = find_nearest_space(text_list, length - line_len, line_len)
        text_list[br2] = "\n"

        return "".join(text_list)
    
    return "\n".join(words)

# ? colours
white = "#ffffff"
blue = "#489dd6"
overlay_transparency = 175

# ? fonts
f_brigadier = ImageFont.truetype("Assets/Font/BrigadierSansRegular.ttf", 300)
f_calibri = ImageFont.truetype("Assets/Font/calibri-regular.ttf", 40)
f_calibri_bold = ImageFont.truetype("Assets/Font/calibri-bold.ttf", 60)
f_calibri_italic = ImageFont.truetype("Assets/Font/calibri-italic.ttf", 25)

# * text input
custom = True if input("custom linebreaks? [y/n] > ") == "y" else False
if custom:
     no_lines = int(input("number of lines > "))
     title_text = "\n".join([input(f"line {i + 1} > ").strip().upper() for i in range(no_lines)])
else:
    title_text = line_split(input("post title > ").strip().upper())

with_text = input("with [leave blank for none] > ").strip().title()


# * background photo
img = Image.new("RGB", (1080, 1920))
bg = Image.open("Assets/Image/bg.png")
img.paste(bg)
img.paste(bg.transpose(Image.FLIP_TOP_BOTTOM), (0, img.height//2))
img.putalpha(overlay_transparency)
bg.close()

# image center
W_CENTER = img.width//2

# * climbing logo 
# loading and resizing
logo = Image.open("Assets/Image/logo.png")
l_size = (math.floor(logo.width*1.5), math.floor(logo.height*1.5)) 
logo = logo.resize(l_size)

# inserting onto image
l_offset = (W_CENTER) - (logo.width//2)
img.alpha_composite(logo, (l_offset, 100))
logo.close()


# * drawing text
draw = ImageDraw.Draw(img)

# post title
h_title = 850
draw.multiline_text((W_CENTER,h_title+10), title_text, blue, f_brigadier, spacing=50, align="center", anchor="mm")
draw.multiline_text((W_CENTER,h_title), title_text, white, f_brigadier, spacing=50, align="center", anchor="mm")

# "with"
if (with_text):
    h_with = 1000 + (title_text.count("\n") * 150)
    draw.text((W_CENTER, h_with), "With:", white, f_calibri, anchor="mm")
    draw.text((W_CENTER, h_with+50), with_text, white, f_calibri_bold, anchor="mm")

# signature
draw.multiline_text((40, 1850), "2024/25\nUoP Climbing", white, f_calibri_italic, align="left")

img.save("overlay.png")
img.close()

# * adding background photo
bg_photo_name = input("background photo name > ")
if bg_photo_name:
    while True:
        try:
            bg_photo = Image.open("Uploads/" + bg_photo_name)
            break
        except FileNotFoundError:
            print("wrong filename")
            bg_photo_name = input("background photo name > ")

    # scaling so either width or height is 1080/1920
    w_photo, h_photo = 1080, 1920
    w_native, h_native = bg_photo.width, bg_photo.height
    if w_native/9 <= h_native/16:
        h_photo = int(h_native // (w_native/1080))
    elif h_native/16 <= w_native/9:
        w_photo = int(w_native // (h_native/1920))
    bg_photo = bg_photo.resize((w_photo, h_photo))


    # centers and crops photo to 1080x1920
    w_offset = (w_photo-1080)//2
    h_offset = (h_photo-1920)//2
    bg_photo = bg_photo.resize((1080, 1920), box=(w_offset, h_offset, w_photo-w_offset, h_photo-h_offset))

    # adds overlay
    bg_photo.putalpha(255)
    overlay = Image.open("overlay.png")
    bg_photo.alpha_composite(overlay)
    overlay.close()

    bg_photo.save("cover.png")