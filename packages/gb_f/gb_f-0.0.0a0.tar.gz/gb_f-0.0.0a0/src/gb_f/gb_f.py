import json
import argparse

parser = argparse.ArgumentParser(prog="gb_f")
parser.add_argument("-a","--add",action="store")
parser.add_argument("-r","--remove",action="store")
parser.add_argument("-l","--list",action="store_true")
args = parser.parse_args()

if args.add is None:
    pass
else:
    with open('data.json') as infile:
        data = json.load(infile)
        infile.close()
        data.append(args.add)
    with open('data.json','w') as outfile:
        json.dump(data, outfile)
        outfile.close()
if args.remove is None:
    pass
else:
    with open('data.json') as infile:
        data = json.load(infile)
        infile.close()
        data.remove(args.remove)
    with open('data.json','w') as outfile:
        json.dump(data, outfile)
        outfile.close()
if args.list == False:
    pass
else:
    with open('data.json') as infile:
        data = json.load(infile)
        infile.close()
        for i in data:
            print(i)
