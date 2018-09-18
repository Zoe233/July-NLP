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
    return (x.split(" ") for x in iterator)

def create_csv_iter(filename):
    '''
    将CSV文件内容变成生成器，可迭代对象。
    Returns an iterator over a CSV file. Skips the header.
    '''
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header
        next(reader)

        for row in reader:
            yield row

def create_vocab(input_iter, min_frequency):
    '''
    创建词汇表，最低词频由min_frequency确定
    Creates and returns a VocabularyProcessor object with the vocabulary
  for the input iterator.
    '''
    vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(
        FLAGS.max_sentence_len,
        min_frequency=min_frequency,
        tokenizer_fn=tokenizer_fn
    )
    vocab_processor.fit(input_iter)
    return vocab_processor

def transform_sentence(sequence, vocab_processor):
    '''
    Maps a single sentence into integer vocabulary.
    Returns a python array.
    '''
    return next(vocab_processor.transform([sequence])).tolist()

def create_text_sequence_feature(fl, sentence, sentence_len, vocab):
    '''
    Writes a sentence to FeatureList protocol buffer.
    '''
    sentence_transformed = transform_sentence(sentence, vocab)
    for word_id in sentence_transformed:
        fl.feature.add().int64_list.value.extend([word_id])
    return fl


if __name__=='__main__':
    # c = create_csv_iter(TEST_PATH)
    # for i in range(1):
    #     value = c.__next__()


    print("Creating vocabulary...")
    input_iter = create_csv_iter(TRAIN_PATH)
    # train.csv文件的列为['Context', 'Utterance', 'Label'
    input_iter = (x[0] + " " + x[1] for x in input_iter)
    vocab = create_vocab(input_iter, min_frequency=FLAGS.min_word_frequency)
    print(vocab)

