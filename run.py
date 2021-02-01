import os
import json
import sys

# import the modules under src
import src.data.import_data as import_data
import src.features.build_features as build_features

with open("./config/data_config.json") as f:
    config = json.load(f)
data_path = config["download"]["data_path"]
kallisto_idx_input = config["kallisto_index"]["input"]
kallisto_idx_output = config["kallisto_index"]["output"]
kallisto_output = config["kallisto_align"]["output"]

with open("./config/feature_config.json") as f:
    feature_config = json.load(f)
cts_dir = feature_config["cts_dir"]

def main(target):
    if target == "run.py":
        # import_data.download_seq(data_path)
        # import_data.convert_idx(kallisto_idx_input, kallisto_idx_output)
        import_data.align_kallisto(kallisto_idx_output, data_path, kallisto_output)
        # build_features.make_cts(kallisto_output, cts_dir)



if __name__ == "__main__":
    target = sys.argv[-1]
    main(target)