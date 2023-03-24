#https://gangannikki.hatenadiary.jp/entry/2019/07/30/190000
import pyocr as ocr
import pyocr.builders
from PIL import Image, ImageDraw

def main():
#	img_path = "../画像/ocr_test.png"
	img = Image.open("/home/shelfer/Desktop/KO/textbox-png.png")

	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("No OCR tool found")
		sys.exit(1)

	tool = tools[0]
	res = tool.image_to_string(img, lang="jpn",
							builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6))
	
	#  画像内に矩形を描画
	draw = ImageDraw.Draw(img)
	for box in res:
		print(box)
		draw.rectangle(box.position, outline=( 255, 0, 0))
	
	img.save("/home/shelfer/Desktop/KO/textbox-png.png")

if __name__ == '__main__':
	main()