from PIL import Image, ImageDraw, ImageFont

def p1():

 im = Image.open('obrezka.jpg')
 im_crop = im.crop((100, 75, 300, 150))
 im_crop.save('obrezka_pillow_crop.jpg', quality=95)


def p2():

 a = input("Праздник:")
 if a == "День святого валентина":
    filename = "love.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()

 if a == "День рождения":
    filename = "др.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()

 if a == "Новый год":
    filename = "нг.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()

 if a == "8 марта":
    filename = "8.png"
    with Image.open(filename) as img:
        img.load()
    img.show()


def p3():


 image = Image.open("obrezka.jpg")

 font = ImageFont.truetype("arial.ttf", 25)
 drawer = ImageDraw.Draw(image)
 drawer.text((50, 100), "Лена, поздравляю!", font=font, fill='black')

 image.save('new_img.jpg')
 image.show()



p1(), p2(), p3()