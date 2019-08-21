import glob
from PIL import Image
import os
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import json
import skimage
import numpy as np
from collections import OrderedDict




def to_int(arr):
    ans = []
    for a in arr:
        ans.append(int(a))
    return ans


def get_gt_bbox(xml_path):
    bbox_list = []
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for obj in root.findall('object'):
        food_name = obj.find('name')
        bbox = obj.find('bndbox')
        xmin = bbox.find('xmin').text
        ymin = bbox.find('ymin').text
        xmax = bbox.find('xmax').text
        ymax = bbox.find('ymax').text

        bbox_list.append([[food_name.text], to_int([xmin, ymin, xmax, ymax])])
    return bbox_list

def get_bbox_from_xml(xml_path):
    json_data = OrderedDict()
    bbox_list = []
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for obj in root.findall('object'):
        recognition_id = obj.find('name')
        bbox = obj.find('bndbox')
        xmin = bbox.find('xmin').text
        ymin = bbox.find('ymin').text
        xmax = bbox.find('xmax').text
        ymax = bbox.find('ymax').text

        bbox_data = OrderedDict()
        bbox_data['x1'] = int(xmin)
        bbox_data['y1'] = int(ymin)
        bbox_data['x2'] = int(xmax)
        bbox_data['y2'] = int(ymax)
        bbox_data['recognition_id'] = recognition_id.text

        bbox_list.append(bbox_data)
    json_data['annotation'] = bbox_list
    return json.dumps(json_data)

def collect_bbox_coordinate(bboxes_data):
    bboxes = []
    for bbox_data in bboxes_data:
        x1 = int(bbox_data['x1'])
        x2 = int(bbox_data['x2'])
        y1 = int(bbox_data['y1'])
        y2 = int(bbox_data['y2'])
        bboxes.append([x1, y1, x2, y2])

    return bboxes

def visualize_bboxes(skimage_, bboxes, colors=None):
    if colors == None:
        colors = [[255, 0, 0] for _ in range(len(bboxes))]
    sk_image = np.copy(skimage_)
    def relocate(x, t):
        x = max(0, x)
        x = min(t-1, x)
        return x
    color = np.array(colors)
    (height, width, _) = sk_image.shape
    for bbox_id, [x1, y1, x2, y2] in enumerate(bboxes):
        sk_image[y1:y2, relocate(x1-3, width):relocate(x1+3, width)] = color[bbox_id]
        sk_image[y1:y2, relocate(x2-3, width):relocate(x2+3, width)] = color[bbox_id]

        sk_image[relocate(y1-3, height):relocate(y1+3, height), x1:x2] = color[bbox_id]
        sk_image[relocate(y2-3, height):relocate(y2+3, height), x1:x2] = color[bbox_id]

    return sk_image

def visualize_xml_annotation(image_path, xml_path, result_path):
    bbox_list = get_gt_bbox(xml_path)
    red_bboxes, blue_bboxes = [], []
    RED = [255, 0, 0]
    BLUE = [0, 0, 255]

    for bbox in bbox_list:
        if bbox[0][0] == '0':
            red_bboxes.append(bbox[1])
        else:
            blue_bboxes.append(bbox[1])

    sk_image = skimage.io.imread(image_path)
    if sk_image.shape[2] == 4:
        # sk_image = skimage.color.rgba2rgb(sk_image)
        RED.append(255)
        BLUE.append(255)

    sk_image = visualize_bboxes(sk_image, red_bboxes, RED)
    sk_image = visualize_bboxes(sk_image, blue_bboxes, BLUE)
    # print(type(sk_image), sk_image.shape)
    pil_image = Image.fromarray(np.uint8(sk_image)).convert('RGB')
    pil_image.save(result_path)


def visualize_json_annotation(image_path, bboxes_data):
    bboxes = []
    for bbox_data in bboxes_data:
        x1 = bbox_data['x1']
        x2 = bbox_data['x2']
        y1 = bbox_data['y1']
        y2 = bbox_data['y2']

        bboxes.append([x1, y1, x2, y2])

    sk_image = skimage.io.imread(image_path)
    RED = [255, 0, 0]
    if sk_image.shape[2] == 4: RED.append(255)
    sk_image = visualize_bboxes(sk_image, bboxes, RED)
    pil_image = Image.fromarray(np.uint8(sk_image)).convert('RGB')
    return pil_image


