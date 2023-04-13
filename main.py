def p1():
    from PIL import Image

    name = "dr.jpg"
    with Image.open(name) as img:
        img.load()

    img = img.crop((100, 200, 600, 500))
    img.save('newdr.jpg')
    img.show()

def p2():
    from PIL import Image, ImageDraw
    slowar = {"23 февраля": "23f.jpg", "8 марта" : "8m.jpg", "День Рождения" : "dr.jpg", "нг" : "ng.jpg", "9 мая" : "9maya.jpeg"}
    f = str(input("Какой праздник? "))
    file = slowar[f]
    with Image.open(file) as img:
        img.load()
    img.show()


def p3():
    from PIL import Image, ImageDraw, ImageFont

    name = str(input("Ваше имя? "))
    image = Image.open("dr.jpg")

    font = ImageFont.truetype("calibri.ttf", 30)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 20), name + ", поздравляю!", font=font, fill='pink', stroke_width=1, stroke_fill="black")
    image.save('dr_img.png')
    image.show()

p1()
p2()
p3()