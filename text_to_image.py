from PIL import Image, ImageDraw, ImageFont
def getCharsOfName(name):
  name = name.split(' ')
  initials= ""
  for c in name:
    initials += c[0]
  img = Image.new('RGB', (100, 100), color = (63, 38, 29))
  font = ImageFont.truetype(r"C:/Users/System-Pc/Desktop/arial.ttf", 20)
  d = ImageDraw.Draw(img)
  d.text((37,37), initials, fill=(212,241,249),font=font)
  img.save('pil_text.png')

name = input("Enter your name (in two words): ")
getCharsOfName(name)