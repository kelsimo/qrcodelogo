import qrcode
from PIL import Image


img = Image.open("csumb.jpg") #allows us to open image
img1 = img.convert("RGBA") #convert to RGBA
img2 = img1.getdata()

newData = []
for item in img2:
        if item[:3] == (255,255,255): #pulls the white
            newData.append((255,255,255,0)) #replaces it with transparent
        else:
            newData.append(item)

img1.putdata(newData)
img1.save("csumb.png", "PNG")

Logo_Link = "csumb.png"
logo = Image.open(Logo_Link)

basewidth = 100 #earlier it was 197

wpercent = basewidth/float(logo.size[0])
hsize = int(logo.size[1]*float(wpercent))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
  error_correction = qrcode.constants.ERROR_CORRECT_H
    )
url = "https://www.youtube.com/watch?v=5dW3ECb-31g"

QRcode.add_data(url)

QRimg = QRcode.make_image(
    fill_color = 'teal', back_color = 'pink').convert('RGB')
diff = (QRimg.size[0]-logo.size[0])//2, (QRimg.size[1]-logo.size[1])//2


QRimg.paste(logo, diff, logo)
QRimg.save("mynewQRcode.png")
img = Image.open("mynewQRcode.png")
img.show()



