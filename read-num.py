#https://motojapan.hateblo.jp/entry/2018/03/12/094636
import time
import pyocr
from PIL import Image
import pyocr.builders

#img : PIL image
img=Image.open('/home/shelfer/Desktop/KO/foo-triCenter.png')
def get_digit_ocr_info(img):
    result = None
    start_time = time.time()
    #print('******** start convert_image_to_deadline  *********')

    width, height=img.size

    tools = pyocr.get_available_tools()
    tool = tools[0]
    #print(tool)
    langs = tool.get_available_languages()
    #print("support langs: %s" % ", ".join(langs))
    #lang = langs[0]
    lang = 'eng'  #言語設定で、「英語」を選択

    digit_txt = tool.image_to_string(
      img,
      lang=lang,
      builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    #print('TextBuilder', digit_txt)
    print(digit_txt)

    #print('******** end convert_image_to_deadline  *********')
    return digit_txt
get_digit_ocr_info(img)