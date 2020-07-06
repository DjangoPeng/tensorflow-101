import os
import cv2
import random
import numpy as np
import shutil


class Dataset(object):
    """
    读取分类数据集类
    """

    def __init__(self, root_dir, train_ratio=0.9, target_num=500):
        """
        构造函数
        :param root_dir: 数据集根路径
        :param train_ratio: 训练集比例
        :param target_num: 类别最低图像数量
        """
        self.root_dir = root_dir
        self.target_images_num = target_num

        # 定义 train、val路径
        self.train_target = os.path.join(root_dir, "train")
        self.val_target = os.path.join(root_dir, "val")

        # 如果存在则移除
        if os.path.exists(self.train_target):
            shutil.rmtree(self.train_target)

        if os.path.exists(self.val_target):
            shutil.rmtree(self.val_target)

        self.train_images = {}
        self.val_images = {}

        self.train_num = 0
        self.val_num = 0
        self.images_num = 0
        self.train_ratio = train_ratio

        # 提取类别列表
        self.class_list = list(
            filter(
                lambda x: not x.startswith(".")
                and os.path.isdir(os.path.join(self.root_dir, x)),
                os.listdir(self.root_dir),
            )
        )
        # 排序
        self.class_list.sort()

        # 创建 train、val 目录
        os.makedirs(self.train_target)
        os.makedirs(self.val_target)

        # 记录类别列表和字典文件
        self.class_index_list = []
        self.class_dict = {}
        for class_index, class_name in enumerate(self.class_list):
            self.class_dict[class_name] = class_index
            self.class_index_list.append(class_index)

        self.class_nums = len(self.class_list)

        for class_name in self.class_list:
            # 获取当前类别下全部原始样本
            class_path = os.path.join(self.root_dir, class_name)
            images_list = list(
                filter(lambda x: not x.startswith("."), os.listdir(class_path))
            )

            # 记录原始样本总数量
            self.images_num += len(images_list)

            # 按照比例随机抽取训练集样本
            train_samples = random.sample(
                images_list, int(len(images_list) * self.train_ratio)
            )
            val_samples = list(set(images_list) - set(train_samples))

            self.train_num += int(len(train_samples))
            self.val_num += int(len(val_samples))

            # 创建训练、测试数据集目录
            train_target_class_path = os.path.join(self.train_target, class_name)
            os.makedirs(train_target_class_path)

            val_target_class_path = os.path.join(self.val_target, class_name)
            os.makedirs(val_target_class_path)

            # 加入当前类别下的原始训练集样本路径
            self.train_images[class_name] = []
            for image_name in train_samples:
                image_path = os.path.join(class_path, image_name)
                target_image_path = os.path.join(train_target_class_path, image_name)

                # 复制样本
                shutil.copyfile(image_path, target_image_path)
                self.train_images[class_name].append(target_image_path)

            # 加入当前类别下的原始测试集样本路径
            self.val_images[class_name] = []
            for image_name in val_samples:
                image_path = os.path.join(class_path, image_name)
                target_image_path = os.path.join(val_target_class_path, image_name)

                # 复制样本
                shutil.copyfile(image_path, target_image_path)
                self.val_images[class_name].append(target_image_path)
