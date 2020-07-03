import os
import sys
import random
import shutil
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description="Split dataset.")

    parser.add_argument(
        "--data_dir", help="Root of original data.", required=True, type=str
    )
    parser.add_argument(
        "--ratio", help="Val data ratio. Default value: 0.1", default=0.1, type=float
    )

    return parser.parse_args(args)


def main(args=None):
    # parse arguments
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    data_dir = args.data_dir
    val_ratio = args.ratio

    train_dir = os.path.join(data_dir, "train")
    val_dir = os.path.join(data_dir, "val")

    if os.path.exists(train_dir):
        shutil.rmtree(train_dir)
    if os.path.exists(val_dir):
        shutil.rmtree(val_dir)

    if os.path.exists(os.path.join(data_dir, "train_data.csv")):
        os.remove(os.path.join(data_dir, "train_data.csv"))
    if os.path.exists(os.path.join(data_dir, "val_data.csv")):
        os.remove(os.path.join(data_dir, "val_data.csv"))
    if os.path.exists(os.path.join(data_dir, "class.csv")):
        os.remove(os.path.join(data_dir, "class.csv"))

    image_name_list = list(
        filter(
            lambda x: not (x.startswith(".") or x.endswith("xml") or x.endswith("csv")),
            os.listdir(data_dir),
        )
    )
    images_num = len(image_name_list)

    os.makedirs(train_dir)
    os.makedirs(val_dir)

    val_list = random.sample(image_name_list, int(val_ratio * images_num))
    train_list = list(set(image_name_list) - set(val_list))

    for train_image_name in train_list:
        train_image = os.path.join(data_dir, train_image_name)
        shutil.copy(train_image, train_dir)
        label_path = os.path.splitext(train_image)[0] + ".xml"
        shutil.copy(label_path, train_dir)

    for val_image_name in val_list:
        val_image = os.path.join(data_dir, val_image_name)
        shutil.copy(val_image, val_dir)
        label_path = os.path.splitext(val_image)[0] + ".xml"
        shutil.copy(label_path, val_dir)


if __name__ == "__main__":
    main()
