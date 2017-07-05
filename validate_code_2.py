from PIL import Image,ImageDraw,ImageChops
import os
from validate_code_1 import *
#分割图片，获取单个字符的图片。二值图片的分隔
def cut_one_char(image):
	#再次降噪 N=4
	clear_noise(image, 4)
	CharWidth = 25
	CharHeight = 26
	Width, Height = image.size
	#find the first column , have black blot 
	x = find_first_column(image)

	box = (x, 0, x+CharWidth, Height)
	image2 = crop_white(image, box)
	y = find_first_row(image2)
	#切割出一个字符
	box = (x, y, x + CharWidth, y + CharHeight)
	image_char = crop_white(image, box)
	#剩下的图片
	if x + CharWidth > Width:
		image_residue = None
	else:
		box = (x + CharWidth, 0, Width, Height)
		image_residue = crop_white(image, box)
	return [image_char, image_residue]

# 没有字符W的情况下,切割的都比较好.
# 出现W的概率为1-(1-1/36)^4≈10.66%
# 这样一来准确率无法超过90%
# 这里处理4个字符的情况
def cut_all_char(image):
	image_char1, image = cut_one_char(image)
	image_char2, image = cut_one_char(image)
	image_char3, image = cut_one_char(image)
	image_char4, image = cut_one_char(image)
	return [image_char1, image_char2, image_char3, image_char4]

# 如果box超出原图范围,默认会以黑色填充
# 因此为了让图片超出部分以白色填充,进行反色处理,最后再反色回来
def crop_white(image, box):
	image = ImageChops.invert(image)
	image = image.crop(box)
	return ImageChops.invert(image)

# 找出image上出现黑点的第一列
def find_first_column(image):
	Width, Height = image.size
	for x in range(Width):
		for y in range(Height):
			if image.getpixel((x, y)) == 0:
				return x

	#如果没有黑点返回第一列
	return 0


def find_first_row(image):
	Width, Height = image.size
	for y in range(Height):
		for x in range(Width):
			if image.getpixel((x, y)) == 0:
				return y

	return 0

if __name__ == '__main__':
	image = Image.open(r'/Users/liufeng/Downloads/py/validate_pic/0.jpg')
	image = pretreat_image(image)
	image_char_list = cut_all_char(image)
	image_char_list[0].show()




