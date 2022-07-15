

from unicodedata import category

categories =       {'ignored-regions': 0, 'pedestrian': 1, 'people': 2, 'bicycle': 3, 'car': 4, 'van': 5, 'truck': 6,
                    'tricycle': 7, 'awning-tricycle': 8, 'bus': 9, 'motor': 10, 'others': 11}


categories = {value:key for key, value in categories.items()}

print(categories)


def writetxt(lines, filename):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

def readtxt(filname):
    with open(filname) as f:
        lines = f.readlines()
    data = []
    for i in lines:
        # print(i)
        # print(i.split('\n')[0].split(','))

        if len(i.split('\n')[0].split(',')) == 9:
            x,y,w,h,cla,cat,_,_,_ =  i.split('\n')[0].split(',')

        if len(i.split('\n')[0].split(',')) == 8:
            x,y,w,h,cla,cat,_,_ =  i.split('\n')[0].split(',')


        x,y,w,h,cla,cat = int(x), int(y), int(w), int(h),int(cla), int(cat)
        # print(i.split('\n')[0])
        # print(x,y,w,h,cla,cat)
        # print('-----------------')
        if cla == 1:
            if cat == 1 or cat == 2:
                data.append(f'{categories[cat]} 0.00 0 0.00 {x} {y} {x+w} {y+h} 0.00 0.00 0.00 0.00 0.00 0.00 0.00')
            
    if len(data) == 0:
        return None
    return data

print()

import os
from glob import glob
import shutil
main_path = 'D:\\projects\\Detect\\visdrone\\data\\train\\'
path = main_path + 'annotations'

all_files = os.listdir(path)

for f in all_files:
    d = readtxt(os.path.join(path,f))

    if d != None:
    # print(d)
        print('current file',f)
        writetxt(d, os.path.join('D:\\projects\\Detect\\DetectTech\\DetectTech\\scripts\\data', 'labels',f))
        print('written to',  os.path.join('D:\\projects\\Detect\\DetectTech\\DetectTech\\scripts\\data\\labels',f))
        img_path = 'D:\\projects\\Detect\\DetectTech\\DetectTech\\scripts\\data\\images'
        shutil.copyfile(os.path.join(main_path, 'images', f.split('.')[0] + '.jpg'), os.path.join(img_path, f.split('.')[0] + '.jpg'))

