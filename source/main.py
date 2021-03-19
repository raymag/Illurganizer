#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil

def only_files_shall_pass(file):
    if os.path.isdir(file):
        return False
    return True

allFolderFiles = os.listdir('.')
print("All Files", allFolderFiles)
folderFiles = list(filter(only_files_shall_pass, allFolderFiles))
folderFiles.sort()
print("Only files", folderFiles)

def get_clean_filename(filename):
    filename = filename.split('.')
    return ['.'.join(filename[:-1]), filename[-1]]

for filename in [get_clean_filename(f) for f in folderFiles]:
    if filename[0] not in allFolderFiles:
        try:
            print("Creating folder [{}]".format(filename[0]))
            os.mkdir(filename[0])
        except:
            print("Can't create folder:", filename[0])
    full_filename = '.'.join(filename)
    print('Moving', full_filename, 'to', '[{}]'.format(filename[0]))
    shutil.move(full_filename, os.path.join(filename[0], full_filename))
