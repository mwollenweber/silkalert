import os
import sys
import traceback
import database

from config import *


def getFiles(root='./'):
    files = []
    for root, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(".csv"):
                print(os.path.join(root, file))
                files.append(os.path.join(root, file))

    return files


def main():
    print DATADIR

    #cli-foo

    #initiate database connection

    #find the files

    #ingest!

    #cleanup/delete the files

    #do something useful



if __name__ == "__main__":
    main()