import argparse
import csv
import os
import sys
import traceback
import config
import database

from models import topTalkerFlowModel

class silkIngest():
    def __init__(self, root='/tmp/silkweb/'):
        print "INIT"
        self.db = topTalkerFlowModel()
        self.root = root
        self.fileList = []

    def getFiles(self):
        outlist = []
        root = self.root

        for root, dirs, files in os.walk(root):
            for file in files:
                if file.endswith(".csv") is True:
                    #print(os.path.join(root, file))
                    outlist.append(os.path.join(root, file))

        self.fileList = outlist
        return outlist

    def ingestFiles(self):
        for f in self.getFiles():
            self.ingestFile(f)

    def ingestFile(self, filename):
        direction = None

        try:
            if filename.find("IN") >= 0:
                direction = "IN"

            else:
                direction = "OUT"

            #get date and hour from filename
            offset = filename.find("/silkweb/")
            offset += 9
            date = filename[offset:offset + 10]
            offset += 11
            hour = filename[offset: offset+2]

            with open(filename, 'rb') as csvfile:
                flowReader = csv.reader(csvfile, delimiter='|',  quoting=csv.QUOTE_NONE)
                for row in flowReader:
                    address = row[0].strip()
                    count = row[1].strip()
                    percent = row[2].strip()

                    print "%s, %s, %s, %s, %s, %s" % (date, hour, direction, address, count, percent)
                    self.db.insert(date, hour, direction, address, count, percent)

            os.remove(filename)

        except OSError:
            traceback.print_exc(file=sys.stdout)

        except:
            traceback.print_exc(file=sys.stdout)

def main():

    #cli-foo
    parser = argparse.ArgumentParser(prog='template', usage='%(prog)s [options]')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--version', action='version', version='%(prog)s -1.0')
    parser.add_argument('--debug', '-D', type=bool, dest='DEBUG', default=False)
    args = parser.parse_args()
    DEBUG = args.DEBUG

    mySilkIngest = silkIngest()

    #initiate database connection

    mySilkIngest.ingestFiles()

    #cleanup/delete the files

    #do something useful



if __name__ == "__main__":
    main()
