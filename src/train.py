import argparse

from model import NoiseRobustCNN
from utils import load_traces


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    traces = load_traces(args.config)
    model = NoiseRobustCNN()
    print("calibrating", len(traces), "sensor traces")


if __name__ == "__main__":
    main()
