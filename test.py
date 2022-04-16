import xml.etree.ElementTree as ET
import os
from PIL import Image

xml_path = r"F:\origindata\outputs"
img_path = r"F:\origindata"
save_path = r"F:\imgdata"
x = 1
for filename in os.listdir(xml_path):
    tree = ET.parse(os.path.join(xml_path, filename))
    root = tree.getroot()
    if not root[1][0].text is None:
        img_name = root[0].text
        img = Image.open(os.path.join(img_path, img_name))
        # img.save(os.path.join(save_path, '{}.jpg'.format(x)))
        x1 = int(root[1][0][0][1][0].text)
        y1 = int(root[1][0][0][1][1].text)
        x2 = int(root[1][0][0][1][2].text)
        y2 = int(root[1][0][0][1][3].text)
        print(x1, y1, x2, y2)
        x += 1
        exit()
print(x)
