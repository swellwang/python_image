# -*-coding:utf-8 -*-
from PIL import Image
import pylab
import os

im = Image.open(r'E:\flower.tif')
im_t = array(im)
#截取区域
#box = (100 , 100 , 400 , 400)
#region = im.crop(box)
#region.show()
#粘贴
#im.paste(region,box)

#色彩分离
#r,g,b = im.split()
#im = Image.merge("RGB",(b,g,r))

#修改拓展名
#out = os.path.splitext('E:\\flower.tif')[0]+'.jpg'
#im.save(out)

#缩略图(改变尺寸)
#im.thumbnail((128,128))
#im.show()
#im.resize((128,128)).show()

#旋转
#im.transpose(Image.ROTATE_180).show()
#im.rotate(45).show()

#x=[100,100,200,200]
#y=[200,500,200,500]
#plot(x,y,'go')
#plot(x[:2],y[:2])
#axis('off')
#show()

#轮廓和直方图
#figure()
#contour(im_t,origin='image')
#axis('equal')
#axis('off')
#figure()
#hist(im_t.flatten(),128)


#交互式标注
#imshow(im_t)
#x=ginput(3)
#print 'you clicked:',x
