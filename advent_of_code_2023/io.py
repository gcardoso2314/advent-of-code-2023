def load_and_split_lines(filename: str):
    with open(filename) as f:
        return (line.strip() for line in f.readlines())
