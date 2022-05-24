import numpy as np 
import pandas as pd 
from pathlib import Path
from xml.dom.minidom import parse
from shutil import copyfile, move
import os

classes = ['helmet', 'head', 'person']

ANNOTATIONS_PATH = ""
DESTINATION_PATH = ""

def convert_annot(size , box):
    """
    calculate anchor points, height and width of bbox 
    """
    x1 = int(box[0])
    y1 = int(box[1])
    x2 = int(box[2])
    y2 = int(box[3])

    dw = np.float32(1. / int(size[0]))
    dh = np.float32(1. / int(size[1]))

    w = x2 - x1
    h = y2 - y1
    x = x1 + (w / 2)
    y = y1 + (h / 2)

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return [x, y, w, h]


def save_txt_file(img_jpg_file_name, size, img_box):
    """
    Save the txt file with class, x, y, width and height
    """
    save_file_name = DESTINATION_PATH + "/" +  img_jpg_file_name + '.txt'
    
    with open(save_file_name ,'a+') as file_path:
        for box in img_box:
            if box[0] != "person":
                cls_num = classes.index(box[0])

                new_box = convert_annot(size, box[1:])

                file_path.write(f"{cls_num} {new_box[0]} {new_box[1]} {new_box[2]} {new_box[3]}\n")

        file_path.flush()
        file_path.close()
            
            
def get_xml_data(file_path, img_xml_file):
    img_path = file_path + '/' + img_xml_file + '.xml'
    #print(img_path)

    dom = parse(img_path)
    root = dom.documentElement
    img_name = root.getElementsByTagName("filename")[0].childNodes[0].data
    img_size = root.getElementsByTagName("size")[0]
    objects = root.getElementsByTagName("object")
    img_w = img_size.getElementsByTagName("width")[0].childNodes[0].data
    img_h = img_size.getElementsByTagName("height")[0].childNodes[0].data
    img_c = img_size.getElementsByTagName("depth")[0].childNodes[0].data
   
    img_box = []
    for box in objects:
        cls_name = box.getElementsByTagName("name")[0].childNodes[0].data
        x1 = int(box.getElementsByTagName("xmin")[0].childNodes[0].data)
        y1 = int(box.getElementsByTagName("ymin")[0].childNodes[0].data)
        x2 = int(box.getElementsByTagName("xmax")[0].childNodes[0].data)
        y2 = int(box.getElementsByTagName("ymax")[0].childNodes[0].data)
  
        img_jpg_file_name = img_xml_file + '.jpg'
        img_box.append([cls_name, x1, y1, x2, y2])

    # test_dataset_box_feature(img_jpg_file_name, img_box)
    save_txt_file(img_xml_file, [img_w, img_h],img_box)

files = os.listdir(ANNOTATIONS_PATH)

for file in files:
    file_xml = file.split(".")
    get_xml_data(ANNOTATIONS_PATH, file_xml[0])