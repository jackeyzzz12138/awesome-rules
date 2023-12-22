import yaml
import sys

def convert_to_yaml(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    data = {'payload': []}
    for line in lines:
        line = line.strip()
        data['payload'].append(line)

    with open(output_file, 'w') as f:
        yaml.dump(data, f)

input_file = sys.argv[1]
output_file = sys.argv[2]

convert_to_yaml(input_file, output_file)