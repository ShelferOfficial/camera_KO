#https://tsukimitech.com/pyocr-tessractocr/
from PIL import Image
import sys
import pyocr


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("OCRツールが見つかりませんでした")
    sys.exit(1)
tool = tools[0]
print("use tool :", tool.get_name())

langs = tool.get_available_languages()
print(langs)

txt = tool.image_to_string(Image.open('ocr-test.png'), lang="jpn")
txt = txt.replace(' ', '')
print(txt)