# -*- codeing = utf-8 -*-
# @Time : 2024/10/9 17:42
# @Author : Luo_CW
# @File : config.py
# @Software : PyCharm
import argparse
import os.path
def parsers():
    parser = argparse.ArgumentParser(description="TextCNN model of argparse")
    parser.add_argument("--train_file", type=str, default=os.path.join("data", "train.txt"))
    parser.add_argument("--dev_file", type=str, default=os.path.join("data", "dev.txt"))
    parser.add_argument("--test_file", type=str, default=os.path.join("data", "test.txt"))
    parser.add_argument("--classification", type=str, default=os.path.join("data", "class.txt"))
    parser.add_argument("--data_pkl", type=str, default=os.path.join("data", "dataset.pkl"))
    parser.add_argument("--class_num", type=int, default=10)
    parser.add_argument("--max_len", type=int, default=38)
    parser.add_argument("--embedding_num", type=int, default=100)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--learn_rate", type=float, default=1e-3)
    parser.add_argument("--num_filters", type=int, default=2, help="卷积产生的通道数")
    parser.add_argument("--save_model_best", type=str, default=os.path.join("model", "best_model.pth"))
    parser.add_argument("--save_model_last", type=str, default=os.path.join("model", "last_model.pth"))
    args = parser.parse_args()
    return args