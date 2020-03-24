import json
import numpy as np
import cv2

#list of classes
classes = []

def getItem(jsonFile, mode = 1):
    """

    :param jsonFile: contents in json file
    :param mode: whether to operate in train set or test set
    :return:
    """
    boxes = []
    filename = jsonFile['filename']

    #use cv2 to read information of the image
    if mode == 1:
        img = cv2.imread('train\\' + filename)
    else:
        img = cv2.imread('test\\' + filename)
    width = img.shape[1]
    height = img.shape[0]

    regions = jsonFile['regions']
    for i in regions:
        box = []

        #find the index of the class name in the classes
        cls_name = i['region_attributes']['label'].lower()
        if(cls_name in classes):
            id = classes.index(cls_name)
        else:
            classes.append(cls_name)
            id = classes.index(cls_name)
        x = int(i['shape_attributes']['x'])
        y = int(i['shape_attributes']['y'])
        w = int(i['shape_attributes']['width'])
        h = int(i['shape_attributes']['height'])

        #change the parameters in the json to those used in yolov3
        x_center = (x + w / 2) / width
        y_center = (y + h / 2) / height
        w = w / width
        h = h / height

        box.append(id)
        box.append(x_center)
        box.append(y_center)
        box.append(w)
        box.append(h)
        boxes.append(box)

    return filename, boxes


annotation = open("annotation.json")
imgs = json.load(annotation)
n = len(imgs)
print(n)
for i in imgs:
    try:
        try:
            #operate on img if it's in the train set
            filepath = 'train\\'
            mode = 1
            filename, boxes = getItem(imgs[i], mode)
            #ready to output the path of the image to the train.txt
            path_file = open('train.txt', mode = 'a')
        except:
            #operate on img if it's in the test set
            filepath = 'test\\'
            mode = 2
            filename, boxes = getItem(imgs[i], mode)
            # ready to output the path of the image to the valid.txt
            path_file = open('valid.txt', mode = 'a')
        boxes_file = open(filepath + filename[:-4] + ".txt", mode='a')
        path_file.write('data/custom/images/' + filename +'\n')

        #for each image.jpg, output the data of all boxes in the image.txt
        for j in range(len(boxes)):
            content = str(boxes[j][0]) + ' ' + str(boxes[j][1]) + ' ' + str(boxes[j][2]) + ' ' + str(boxes[j][3]) + ' ' + str(boxes[j][4])
            boxes_file.write(content)
            boxes_file.write("\n")
        print(content)
    except:
        continue

#output all class names
cls_names_file = open("classes.names", mode = 'a')
for name in classes:
    cls_names_file.write(name)
    cls_names_file.write("\n")
print(len(classes))
