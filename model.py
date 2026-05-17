"""Model training on the leipzig corpora"""
import random
import pandas as pd


def open_training_data():
    df_devel = pd.read_csv('data/devel.tsv', sep='\t', names=['true', 'false'])
    return df_devel

def split_data(devel):
    pass

def prepare_training_data():
    devel = open_training_data()

    return devel

def train_model():
    pass

def evaluate_model(filename):
    with open(filename + ".output", 'w') as out:
        for line in open(filename):
            out.write(line.split('\t')[0])
            out.write('\n')

if __name__ == '__main__':
    print(open_training_data())