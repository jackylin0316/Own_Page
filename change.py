from PIL import Image
image = Image.open('img/TSLA_1.jpg')
print(image.size)
image.show()

# image.thumbnail((600,600))
# image.save('first_1.jpg')



# im = Image.open('/Users/hayashishifuchi/Desktop/Own_Page/img/service_item.jpg')
# im.save('service_item.png')