import re
import clipboard
import argparse
import sys

def get_args():
    """
    get args
    """
    parser = argparse.ArgumentParser(description='regex cli tool')
    parser.add_argument('-r','--regex',help='Regex with special characters escaped',action='store')
    parser.add_argument('-d','--data',help='If not specified input will be pulled from stdin. If \'c\' is specified clipboard data will be used.',required=False)
    parser.add_argument('-g','--groups',help='List of capture groups to print. Eg: 0,1,2 / 0,2 / 0',required=False)
    args = parser.parse_args()
    return parser.parse_args()


def findall(raw_string,text): 
    """calls findall with regex string passed"""
    finder = re.compile(raw_string)
    return finder.findall(text)



def main_btre():
    args = get_args()
    groups = None
    raw_string=r'{}'.format(args.regex)
    if args.data != None:
        text = args.data
    elif args.data == None:
        text=sys.stdin.read()
        
    elif args.data.lower() == 'c':
        text=clipboard.paste()

    if args.groups != None:
        groups = args.groups.split(',')
    data = findall(raw_string,text)
    printer = []
    if groups != None:
        for each in data:
            data_group = []
            for group in groups:
                if int(group) >=len(each):
                    pass
                else:
                    data_group.append(each[int(group)])
            printer.append(data_group)
            data_group=[]
            if printer != [[]]:
                for each in printer:
                    print(each)
    else:
        for each in data:
            print(each)
            
if __name__ == '__main__':
    main_btre()
