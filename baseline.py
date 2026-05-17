"""Baseline provided by the course lecturers"""
def prepare_training_data():
    pass

def train_model():
    pass

def evaluate_model(filename):
    with open(filename + ".output", 'w') as out:
        for line in open(filename):
            out.write(line.split('\t')[0])
            out.write('\n')
