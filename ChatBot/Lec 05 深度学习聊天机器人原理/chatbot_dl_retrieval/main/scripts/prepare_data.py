# -*- coding:utf-8 -*-
import os
import csv
import itertools
import functools
import tensorflow as tf
import numpy as np
import pandas as np

# tf.flags.DEFINE_xxx
# FLAGS=tf.flags.FLAGES
# 添加命令行的可选参数
tf.flags.DEFINE_integer(
    'min_word_frequency', 5, 'Minimum frequency of words in the vocabulary'
)

tf.flags.DEFINE_integer(
    'max_sentence_len', 160, "Maximum Sentence Length"
)

tf.flags.DEFINE_string(
    'input_dir', os.path.abspath('../../ubuntu_dataset'),
    "Input directory containing original CSV data files"
)

tf.flags.DEFINE_string(
    'output_dir', os.path.abspath('../../ubuntu_dataset'),
    'Output directory for TFRecord files'
)

FLAGS = tf.flags.FLAGS

TRAIN_PATH = os.path.join(FLAGS.input_dir, 'train.csv')
VALIDATION_PATH = os.path.join(FLAGS.input_dir, 'valid.csv')
TEST_PATH = os.path.join(FLAGS.input_dir, 'test.csv')

def tokenizer_fn(iterator):
    '''
    将可迭代对象，逐个按空格分词（英文可以），返回的分词存在元组中。
    '''
    return (x.split("") for x in iterator)

def create_csv_iter(filename):
    '''
    返回生成的
    Returns an iterator over a CSV file. Skips the header.
    '''
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header
        next(reader)

        for row in reader:
            yield row




if __name__=='__main__':
    print(FLAGS.min_word_frequency)

