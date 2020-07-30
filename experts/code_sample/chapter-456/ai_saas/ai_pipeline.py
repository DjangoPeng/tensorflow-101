#!/usr/bin/env python
# coding: utf-8

# ### 加载检测器 detector

# import keras
import keras

# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input

# import miscellaneous modules
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time
import pandas as pd
import tensorflow as tf

inference_model_save_path = "../models/RetinaNet/retinanet_inference.h5"

def run(image_path):
    detector = models.load_model(inference_model_save_path, backbone_name='resnet50')

    # detector.summary()


    # ### 加载检测 类别名称 detector_class_name


    df = pd.read_csv("../data/baijiu/class.csv", header=None)

    # load label to names mapping for visualization purposes
    detector_class_name = df[0].values.tolist()


    # ### 加载分类模型 ResNet


    classifier = tf.keras.models.load_model("../models/ResNet50/ResNet50_classified.h5")


    # classifier.summary()


    # ### 加载类别名称文件


    with open("../models/ResNet50/ResNet50_classified_class.txt", "r+") as f:
        classifier_class_name = eval(f.read())


    classifier_class_name[:10]


    # ## 检测+分类

    def load_image(img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_tensor = image.img_to_array(img)                    
        img_tensor = np.expand_dims(img_tensor, axis=0)         
        img_tensor /= 255.                                      

        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

        return img_tensor


    # test_image_path = 'test_1.jpg'
    test_dir = "test/"

    # 读取图像
    input_image = read_image_bgr(image_path)

    # 预处理
    input_image = preprocess_image(input_image)
    input_image, scale = resize_image(input_image)

    # 计时开始
    start = time.time()
    # 商品检测
    boxes, scores, labels = detector.predict_on_batch(np.expand_dims(input_image, axis=0))

    # 图像尺寸矫正
    boxes /= scale

    # 分类结果画图，重新读取原图
    draw = read_image_bgr(image_path).copy()
    draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

    # 记录分类结果
    idx = 0
    predict_list = []

    # 商品识别和可视化
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        # 过滤小于0.5检测框
        if score < 0.5:
            break
        # 分类框颜色（复用RetinaNet可视化模块，颜色类别可能不够用）
        color = label_color(label)
        b = box.astype(int)
        # 检测框中的SKU小图
        cropped = draw[b[1]:b[3], b[0]:b[2]]
        if cropped is not None:
            sku_image_path = f"test/{idx}.jpg"
            # 保存SKU小图结果
            cv2.imwrite(sku_image_path, cropped)    
            # 商品识别
            img_tensor = load_image(sku_image_path)
            # 商品识别
            pred = classifier.predict(img_tensor)
            sku_id = np.argmax(pred)
            sku_name = classifier_class_name[sku_id]
            sku_score = np.max(pred)
            predict_list.append(sku_name)
            # 打印识别结果
            print(f"{sku_id} {sku_name} {sku_score}")
            # 在货架图中可视化分类结果
            caption = "{} {:.3f}".format(sku_id, sku_score)
            draw_caption(draw, b, caption)
            draw_box(draw, b, color=label_color(sku_id))

            idx+=1

    print("processing time: ", time.time() - start)
    plt.figure(figsize=(25, 45))
    plt.axis('off')
    plt.imshow(draw)
    plt.show()

    return predict_list

