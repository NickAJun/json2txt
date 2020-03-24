# json2txt
If you want to use your own dataset to train on Pytorch YOLOv3, however your annotation is saved as a json file, you can use this little python program to transform it to the form of txt files. The results would be one txt file with data of the boxes for each image, a classes.names, a train.txt and a valid.txt.

Some pre-operations: 
Name the train set directory "train" where you put all train set images.
Name the test set directory "test" where you put all valid set images.
Name the annotation json file "annotation.json"
Put json2txt.py and annotation.json in the same directory with train directory and test directory.
