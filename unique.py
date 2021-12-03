#!encoding=utf-8

#域复杂性要求，默认是打开的，不能设置纯数字或者纯字母，必须要有数字加大小写
import argparse
import os


def valid(line):
    if len(line) < 8:
        return False

    if line.isdigit():
        return False
    if line.isalpha():
        return False
    flag11=False
    flag22=False
    for x in line:
        flag1=x.isdigit()
        if flag1:
            flag11=True

        flag2=x.isalpha()
        if flag2:
            flag22=True

    if flag11 and flag22:
        return True
    return False


def unique(inputfile,outputfile):
    summary=[]
    with open(inputfile,'r') as f:
        for x in f.readlines():
            line=x.strip("\n")
            flag=valid(line)
            if flag:
                summary.append(line)
            continue
    with open(outputfile,'w+') as output:
        output.writelines('\n'.join(summary))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='summary to unique ')
    parser.add_argument(
        '--summaryfile',
        help='read summary text',required=True)
    parser.add_argument(
        '--uniquefile',
        help='save unique file',required=True)
    args = parser.parse_args()
    unique(args.summaryfile,args.uniquefile)