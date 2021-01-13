import os
import json
import sys

# import the modules under src
import src.data.import_data as import_data

with open("./config/data_config.json") as f:
    config = json.load(f)
data_path = config["download"]["data_path"]
kallisto_idx_input = config["kallisto_index"]["input"]
kallisto_idx_output = config["kallisto_index"]["output"]

def main(target):
    if target == "run.py":
        # import_data.download_seq(data_path)
        import_data.convert_idx(kallisto_idx_input, kallisto_idx_output)


if __name__ == "__main__":
    target = sys.argv[-1]
    main(target)