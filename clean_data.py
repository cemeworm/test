from PIL import Image
import os
import pytesseract

path = os.path.dirname(__file__)
origin_path = path + '/origin_imgs/'
new_path = path + '/clean_imgs/'

for image in os.listdir(origin_path)[:100]:
    im = Image.open(origin_path+image)
    width,height = im.size

    color_info = im.getcolors(width*height)
    sort_color = sorted(color_info,key = lambda x: x[0],reverse=True)
    char_dict = {}
    for i in range(1,6):
        im2 = Image.new('RGB',im.size,(255,255,255))
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if im.getpixel((x,y)) == sort_color[i][1]:
                    im2.putpixel((x,y),(0,0,0))
                else:
                    im2.putpixel((x,y),(255,255,255))
        im2.save(new_path + str(i)+'-'+image.replace('jpg','tif'))
    print('成功处理图片{}'.format(image))

for image in os.listdir(new_path):
    im2 = Image.open(new_path+image)
    char = pytesseract.image_to_string(im2,config='--psm 10')
    print(char)