# hardhat-detector
Custom object detection model for safety helmet detection. Trained with yolov5 model.

This repository is one of my projects during my internship at Brain (Brazilian Artificial Inteligence Nucleus - https://ipfacens.com.br/brain-2/).
It was completly implemented with python in jupyter notebook and google colab. 
For this project, it was used two datasets plus a few images collected and labeled manually:

<p> https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection </p>
<p> https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release </p>

The extra scripts were made to convert the annotations to pascal VOC .txt format as it is required for yolov5 model. Besides, as it was used an extra dataset, it was necessary to convert the classes id's and remove a third unwanted class.

