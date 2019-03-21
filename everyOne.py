# -*- coding: utf-8 -*- 

import os
import os.path

# This folder is custom
rootdir = 'D:\\ExtraApp\\NoteBook'
for parent, dirnames, filename in os.walk(rootdir):
    # Case1: traversal the directories
    # for dirname in dirnames:
    #     # print("Parent folder:", parent)
    #     print("Dirname:", filename)
    # Case2: traversal the files
    # for filename in filenames:
    #     print("Parent folder:", parent)
    #     print("Filename:", filename)
    
