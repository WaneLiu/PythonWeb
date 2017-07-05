from PIL import Image
from pytesseract import image_to_string
image = Image.open(r'/Users/liufeng/Downloads/py/validate_pic/0.jpg')
image = image.convert("L")
def initTable(threshold=140):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table
binaryImage = image.point(initTable(), '1')
binaryImage.show()
print(image_to_string(binaryImage, config='-psm 7')