import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import json
from collections import OrderedDict


#plot bbox for prediction result, bbox_data includes the dictionary of pred_bboxes with confidence score
def plot_bbox(img_path, bbox_data, result_path="somewhere"):
    image = np.array(Image.open(img_path), dtype=np.uint8)
    fig, ax = plt.subplots(1)
    ax.imshow(image)

    for bbox in bbox_data:
        x1 = bbox['xmin']
        y1 = bbox['ymin']
        x2 = bbox['xmax']
        y2 = bbox['ymax']
        score = bbox['confidence_score']
        rect = patches.Rectangle((x1, y1), x2-x1+1, y2-y1+1, linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect)
        plt.text(x1, y1, score, color='red', verticalalignment='top')

    # plt.show()
    plt.axis('off')
    plt.savefig(result_path, dpi=200, bbox_inches='tight', pad_inches=0.0)
    plt.close()

# json_path = "C:/Users/NExT/Documents/alan_project/0524_food_detection/data/0606_Breakfast__trial0/database/000013.json"
# with open(json_path) as json_file:
#     json_data = json.load(json_file, object_pairs_hook=OrderedDict)
#     pred_bboxes = json_data['prediction'][0]['bbox']
#     img_path = "C:/Users/NExT/Documents/alan_project/0524_food_detection/data/0606_Breakfast__trial0/data/"\
#                + json_data['file_name'] + json_data['img_ext']
#     result_path = "C:/Users/NExT/Documents/alan_project/demo.png"
#     plot_bbox(img_path, pred_bboxes, result_path)