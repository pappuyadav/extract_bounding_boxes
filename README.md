# extract_bounding_boxes
This script will help you extract file id and corresponding bounding boxes for detected objects in YOLOV3/4/5.
Once you have trained and validated your YOLOV3/4/5 model, a predicted.json file is created that includes "filed id"
and relative bounding box coordinates of all the detected objects of choice in all the validation set of images.
This script will help you extract all the bounding box coordinates and corresponding file id based on set confidence
threshold value and write them into a new csv file.
