from PIL import Image
image = Image.open('img/first.jpg')
# print(image.size)
# image.show()

image.thumbnail((300,300))
image.save('first_1.jpg')



# im = Image.open('/Users/hayashishifuchi/Desktop/Own_Page/img/service_item.jpg')
# im.save('service_item.png')