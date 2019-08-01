from PIL import Image
import numpy as np


def to_int(arr):
    if isinstance(arr, list):
        ans = []
        for a in arr:
            ans.append(int(a))
        return ans
    else:
        return int(arr)

def visualize_bbox(img, bbox_list, color):
    def relocate(x, t):
        x = max(0, x)
        x = min(t-1, x)
        return x

    pixdata = img.load()
    (w, h) = img.size

    for [x1, y1, x2, y2] in bbox_list:
        for i in range(x1, x2+1):
            for j in range(3):
                pixdata[relocate(i, w), relocate(y1+j, h)] = color
                pixdata[relocate(i, w), relocate(y2-j, h)] = color

        for i in range(3):
            for j in range(y1, y2+1):
                pixdata[relocate(x1+i, w), relocate(j, h)] = color
                pixdata[relocate(x2-i, w), relocate(j, h)] = color

    return img

def visualize_bboxes(sk_image, bboxes, color):
    def relocate(x, t):
        x = max(0, x)
        x = min(t-1, x)
        return x
    color = np.array(color)
    (height, width, _) = sk_image.shape
    for [x1, y1, x2, y2] in bboxes:
        sk_image[y1:y2, relocate(x1-3, width):relocate(x1+3, width)] = color
        sk_image[y1:y2, relocate(x2-3, width):relocate(x2+3, width)] = color

        sk_image[relocate(y1-3, height):relocate(y1+3, height), x1:x2] = color
        sk_image[relocate(y2-3, height):relocate(y2+3, height), x1:x2] = color

    return sk_image

def compute_IoU(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / (boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou

def get_bbox_image(image, bbox, padding=0.2):
    (w, h) = image.size
    w_box = bbox[2] - bbox[0] + 1
    h_box = bbox[3] - bbox[1] + 1
    w1 = max(0, bbox[0] - int(padding * w_box))
    w2 = min(w, bbox[2] + int(padding * w_box))
    h1 = max(0, bbox[1] - int(padding * h_box))
    h2 = min(h, bbox[3] + int(padding * h_box))

    bbox_image = image.crop((w1, h1, w2, h2))
    return bbox_image


def compute_single_precision_recall(gt_bboxs, pred_bboxs, threshold = 0.5):
    if len(gt_bboxs) == 0:
        return 0, 1
    if len(pred_bboxs) == 0:
        return 1, 0

    tp = 0
    for pred_id, pred_bbox in enumerate(pred_bboxs):
        for gt_id, gt_bbox in enumerate(gt_bboxs):
            if compute_IoU(gt_bbox, pred_bbox) >= threshold:
                tp += 1
                break

    precision = tp / len(pred_bboxs)
    recall = tp / len(gt_bboxs)

    return precision, recall

def average(value_list):
    if len(value_list) == 0:
        return 0
    return round(sum(value_list) / len(value_list), 4)





