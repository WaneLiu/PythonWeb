from PIL import Image,ImageDraw,ImageChops
import os

def pretreat_image(image):
	image = image.convert("L")

	image = image2imbw(image,180)

	clear_noise(image, 4)

	box = ( 8, 10, 118, 50)
	return image
# 灰度图像二值化,返回0/255二值图像
def image2imbw(image, threshold):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	image = image.point(table, '1')
	image = image.convert("L")
	return image

# 根据一个点A的灰度值(0/255值),与周围的8个点的值比较
# 降噪率N: N=1,2,3,4,5,6,7
# 当A的值与周围8个点的相等数小于N时,此点为噪点
# 如果确认是噪声,用该点的上面一个点的值进行替换
def get_near_pixel(image, x, y, N):
	pix = image.getpixel((x,y))
	near_dots = 0
	if pix == image.getpixel((x-1, y-1)):
		near_dots += 1
	if pix == image.getpixel((x-1, y)):
		near_dots += 1
	if pix == image.getpixel((x-1, y+1)):
		near_dots += 1
	if pix == image.getpixel((x, y+1)):
		near_dots += 1
	if pix == image.getpixel((x, y-1)):
		near_dots += 1
	if pix == image.getpixel((x+1, y-1)):
		near_dots += 1
	if pix == image.getpixel((x+1, y+1)):
		near_dots += 1
	if pix == image.getpixel((x+1, y)):
		near_dots += 1
	if near_dots < N:
		return image.getpixel((x, y-1))#clear_noise已经把最初四周改成白色
	else:
		return None

# 降噪处理
def clear_noise(image, N):
	draw = ImageDraw.Draw(image)
	#外一圈白色
	Width, Height = image.size
	for x in range(Width):
		draw.point((x, 0), 255)
		draw.point((x, Height-1), 255)

	for y in range(Height):
		draw.point((0, y), 255)
		draw.point((Width-1, y), 255)

	#内部降噪
	for x in range(1, Width-1):
		for y in range(1, Height-1):
			color = get_near_pixel(image, x, y, N)
			if color != None:
				draw.point((x, y), color)


if __name__ == '__main__':
	image = Image.open(r'/Users/liufeng/Downloads/py/validate_pic/0.jpg')
	image = pretreat_image(image)
	image.show()
	image.save(‘D:’)


