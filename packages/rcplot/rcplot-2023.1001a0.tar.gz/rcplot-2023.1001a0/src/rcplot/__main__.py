# __main__.py

from .f1 import plotf1
from .cover_error import plotcover
import argparse
import pandas as pd

def main():
    # parse input arguments
    parser = argparse.ArgumentParser(
        description="Function to classify a user defined number of points from images in a directory"
    )
    parser.add_argument('-m', '--metric', type=str, help='Type of plot to make (either f1 or cover error)',
                        choices=["f1", "cover"], required=True)
    parser.add_argument('-d', '--data', type=str, help='file containing the test data', required=True)
    parser.add_argument('-l', '--labelset', type=str, help='file containing the labelset', required=True)

    args = vars(parser.parse_args())

    df = pd.read_csv(args["data"])
    df.dropna(inplace=True)
    labels_df = pd.read_csv(args["labelset"])

    if args["metric"] == "f1":
        plotf1(df, labels_df)
    elif args["metric"] == "cover":
        plotcover(df, labels_df)

if __name__ == "__main__":
    main()