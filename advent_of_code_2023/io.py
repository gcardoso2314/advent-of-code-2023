import argparse


def load_and_split_lines(filename: str):
    with open(filename) as f:
        return (line.strip() for line in f.readlines())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    return parser.parse_args()
