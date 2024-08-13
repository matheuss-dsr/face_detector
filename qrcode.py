import qrcode

data = '11971437983'

img = qrcode.make(data)

img.save('C:/Users/Usuario/Desktop/Nova pasta/pix.png')