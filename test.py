import xml.etree.ElementTree as ET
import os
from PIL import Image

xml_path = r"F:\origindata\outputs"
img_path = r"F:\origindata"
img_save_path = r"F:\imgdata"
img_txt_filename = os.path.join(img_save_path, "img.txt")
x = 1
txt_file = open(img_txt_filename, "w")
txt_file.write("1144\n")
txt_file.write("filename x y w h\n")
try:
    for filename in os.listdir(xml_path):
        tree = ET.parse(os.path.join(xml_path, filename))
        root = tree.getroot()
        if not root[1][0].text is None:
            img_name = root[0].text
            img = Image.open(os.path.join(img_path, img_name)).convert("RGB")
            img.save(os.path.join(img_save_path, '{}.jpg'.format(x)))
            x1 = int(root[1][0][0][1][0].text)
            y1 = int(root[1][0][0][1][1].text)
            x2 = int(root[1][0][0][1][2].text)
            y2 = int(root[1][0][0][1][3].text)
            txt_file.write("{0}.jpg {1} {2} {3} {4}\n".format(x, x1, y1, x2 - x1, y2 - y1))
            txt_file.flush()
            print(x1, y1, x2, y2)
            x += 1
finally:
    txt_file.close()
    print(x)
