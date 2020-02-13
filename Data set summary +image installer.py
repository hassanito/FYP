import os
os.chdir("C:\\Users\\hassan\\Desktop\\fyp")
import urllib.request

class Product:
    def __init__(self,ID,images):
        self.product_ID = ID
        self.product_images_URL = images
        self.number_of_images = len(images)
filepath = 'C:\\Users\\hassan\\Desktop\\fyp\\productsImagesURLs.txt'
products ={}
#products is a hashmap with key=ID and value = list of url images of product Id
with open(filepath) as fp:
   line = fp.readline()
   cnt = 0
   lines = []
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       lines.append(line)
       id = lines[cnt][:14]
       url = lines[cnt][15:]
       if(id in products):
           products[id].append(url)
       else:
           products[id] = [url]
       cnt += 1


products_objects = {}
#products_objects is a hashmap with key =ID and value = object Product with ID
for product in products.keys():
    p = Product(product,products[product])
    products_objects[product]=p

#products_objects_number_images is a hashmap with key = ID
products_objects_number_images = {}
for id in products_objects:
    products_objects_number_images[id]=products_objects[id].number_of_images
#counts the objects with the number of images
stats = {}
for id in products_objects_number_images:
    number = products_objects_number_images[id]
    if(number in stats):
        stats[number] = stats[number]+1
    else:
        stats[number]=1



def image_installer(url,picture_filename):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'whatever')
    filename, headers = opener.retrieve(url, picture_filename)

