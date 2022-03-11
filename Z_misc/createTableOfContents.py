#!/usr/bin/env python
# https://btmiller.com/2015/03/17/represent-file-structure-as-yaml-with-python.html

import os
import sys
import yaml


def dir_to_dict(path):
    exclude_dir = set(['.c9','.git'])
    exclude_files = set(['.o'])
    directory = {}

    for dirname, dirnames, filenames in os.walk(path):
        dn = os.path.basename(dirname)
        directory[dn] = []

        if dirnames:
            for d in dirnames:
                if d not in exclude_dir:
                    directory[dn].append(dir_to_dict(path=os.path.join(path, d)))

            
            for f in filenames:
                if f.endswith('.py'): #  
                    directory[dn].append(f)
        else:
            # [directory[dn] for files in filenames if not files.endswith('.cpp.o')]
            fnames=[]
            for f in filenames:
                if f.endswith('.py'): # 
                    fnames.append(f)
            directory[dn] = fnames

        return directory

if len(sys.argv) == 1:
    p = os.getcwd()
elif len(sys.argv) == 2:
    p = os.path.abspath(sys.argv[1])
else:
    sys.stderr.write("Unexpected argument {}\n".format(sys.argv[2:]))
# p="/home/ec2-user/environment/"
try:
    with open("{}.yaml".format(os.path.basename(p)), "w") as f:
        try:
            yaml.dump(dir_to_dict(path=p), f, default_flow_style=False)
            print("Dictionary written to {}.yaml".format(os.path.basename(p)))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)