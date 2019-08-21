import xml.etree.ElementTree as ET
from collections import OrderedDict
import json

def collect_bboxes(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    bboxes = []
    for obj in root.findall('object'):
        bbox_data = OrderedDict()
        bbox = obj.find('bndbox')
        bbox_data['x1'] = int(float(bbox.find('xmin').text))
        bbox_data['y1'] = int(float(bbox.find('ymin').text))
        bbox_data['x2'] = int(float(bbox.find('xmax').text))
        bbox_data['y2'] = int(float(bbox.find('ymax').text))

        try:
            bbox_data['category'] = obj.find('name').text
        except:
            bbox_data['category'] = '0'
            pass

        bboxes.append(bbox_data)

    bboxes_data = json.dumps(bboxes)
    return bboxes_data