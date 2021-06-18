from PIL import Image, ImageDraw, ImageFont
from os import path


memefolder='images'
memename='vegeta.jpg'
outputname='memev.png'
memeimage=path.join(memefolder, memename)
memeresult=path.join(memefolder, outputname)

text1="cuando comparas tu programa \n en codingame:"
text2="Esos insectos siempre \n van un paso adelante"

textsize=50
origen1=(50, 25)
origen2=(50, 360)

#Loads font and defines size
comicFont = ImageFont.truetype('/usr/share/fonts/opentype/comic-neue/ComicNeue_Bold.otf', textsize)

#Opens meme image
meme = Image.open(memeimage).convert('RGB')
canvas = ImageDraw.Draw(meme)

#write Text replace TODO with loop

canvas.text(origen1, text1, font=comicFont, fill ="green")
canvas.text(origen2, text2, font=comicFont, fill ="green")

#Show image and save it
meme.show()
meme.save(memeresult)