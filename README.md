# hardhat-detector
Custom object detection model for safety helmet detection. Trained with yolov5 model.

This repository is one of my projects during my internship at Brain (Brazilian Artificial Inteligence Nucleus - https://ipfacens.com.br/brain-2/), for research purposes.It was completly implemented with python in jupyter notebook and google colab. 

### Dataset
For this project, it was used two datasets: plus a few images of bald people collected and labeled manually:

<p> https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection </p>
<p> https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release </p>

but, the model presented problems while detecting bald people, therefore, over 200 images were labelled manually and added to the dataset.
The objects were classified between: helmet (0) and no-helmet (1).

The extra scripts were made to convert the annotations to pascal VOC .txt format as it is required for yolov5 model. Besides, as it was used an extra dataset, it was necessary to convert the classes id's and remove a third unwanted class.

### Training

The training was done over yolov5s.pt pre-trained weight with 150 epochs; 100 epochs for the first run (exp20) with the two datasets and 50 for the second (exp23) with the addition of bald people images.

### Results
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/005346_jpg.rf.8bd69fbd424d324d18fe1474a91261ab.jpg">
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/005382_jpg.rf.bad5f80a3fa19ab150532b976adaa2f1.jpg">
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/005385_jpg.rf.aa3ca01ed31ce9c709f480c7b4293342.jpg">
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/005428_jpg.rf.c07893f3665caaac1d1dc732830e7097.jpg">
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/005536_jpg.rf.4b788ae41afe852fe486e343146047d9.jpg">
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/006967_jpg.rf.9bb3ed18c5e660a119ca04271d8fe72c.jpg">
<img src="https://github.com/vitorozaki/hardhat-detector/blob/master/runs/results/007004_jpg.rf.c85aba0ea86d520bed6628bdc78a61cf.jpg">




<p>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="30">
<img src="https://user-images.githubusercontent.com/62910058/170049280-a2dbfb89-c068-421c-80ab-d2fa713f32ca.png" width="30">
<img src="https://user-images.githubusercontent.com/62910058/170049296-ce791ab4-37df-4ab6-b65e-1e0e70fa566e.png" width="30">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width="30">
</p>

## Dataset reference
@article{peng2018detecting,
  title={Detecting Heads using Feature Refine Net and Cascaded Multi-scale Architecture},
  author={Peng, Dezhi and Sun, Zikai and Chen, Zirong and Cai, Zirui and Xie, Lele and Jin, Lianwen},
  journal={arXiv preprint arXiv:1803.09256},
  year={2018}
}
