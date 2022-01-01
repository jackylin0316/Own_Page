from PIL import Image
img = Image.open('./img/service_item.png')
img.putalpha(64)  # Half alpha; alpha argument must be an int
img.save('item.png')



# im = Image.open('/Users/hayashishifuchi/Desktop/Own_Page/img/service_item.jpg')
# im.save('service_item.png')