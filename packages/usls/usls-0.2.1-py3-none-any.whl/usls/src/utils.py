import cv2
from pathlib import Path
import numpy as np
import rich
import shutil
import argparse
import os
from tqdm import tqdm
import sys
import random
import time
import logging
import glob
import re
import rich
from rich.console import Console
from datetime import datetime
import contextlib
import numpy as np
from dataclasses import dataclass
from typing import Union
from PIL import ExifTags, Image, ImageOps
import hashlib
from loguru import logger as LOGGER


CONSOLE = Console()
IMG_FORMAT = ('.jpg', '.jpeg', '.png', '.bmp')
LABEL_FORMAT = ('.txt', '.xml', '.yaml', '.csv')
VIDEO_FORMAT = ('.mp4', '.flv', '.avi', '.mov')
ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'



def natural_sort(x, _pattern=re.compile('([0-9]+)'), mixed=True):
    return [int(_x) if _x.isdigit() else _x for _x in _pattern.split(str(x) if mixed else x)]



def time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_md5(f):
    m = hashlib.md5(open(f,'rb').read())
    return m.hexdigest()


def gen_random_string(length):
    return ''.join(random.choices(ASCII_LETTERS, k=length))


def get_common_files(directory):

    # file list
    f_list = list()
    for x in Path(directory).iterdir():
        if str(x).startswith('.'):   # hidden file, leave it
            continue
        if x.suffix == '':   # no suffix
            if x.is_dir():
                f_list.append(x)    # dir, append
        else:
            f_list.append(x)    # has suffix, append

    return f_list


def verify_images(path, output_dir):
    _check_again = True  # flag

    # PIL check 1st, and restore corrupt JPEG
    try: 
        with Image.open(path) as im:
            im.verify()   # PIL image quality check

            # jpg & jpeg corrupt check
            if im.format.lower() in ('jpeg', 'jpg'):
                with open(path, "rb") as f:
                    f.seek(-2, 2)
                    if f.read() != b'\xff\xd9':     # corrupt JPEG
                        ImageOps.exif_transpose(Image.open(path)).save(path, 'JPEG', subsampling=0, quality=100)
                        CONSOLE.log(f"Corrupt JPEG restored and saved | {path}")
    except OSError:
        CONSOLE.log(f"PIL verify failed! | {path}")
        shutil.move(str(path), str(output_dir))
        _check_again = False  # set flag
        # integrity = False
        return False


    # opencv check again
    if _check_again:
        try:
            if cv2.imread(str(path)) is None:  # get md5 of each image
                shutil.move(str(path), str(output_dir))
                return False
        except Exception as e:
            CONSOLE.log(f"opencv exceptions: {e} | {path}")
            return False

    return True


# img_list & label_list, relative path
def load_img_label_list(img_dir, label_dir, img_format, info=True):
    image_list = [x for x in Path(img_dir).iterdir() if x.suffix in img_format]
    label_list = list(Path(label_dir).glob("*.txt"))
    
    if info:
        rich.print(f"[green]> Images count: {len(image_list)}")
        rich.print(f"[green]> Labels count: {len(label_list)}")
        

    return image_list, label_list



# img_path => label_path(txt)
def get_corresponding_label_path(img_path, output_dir):
    label_name = Path(img_path).stem + '.txt'
    saveout = Path(output_dir) / label_name 
    return str(saveout)


# Check if a point belongs to a rectangle
def is_point_in_rect(x, y, l, t, r, b):
    return l <= x <= r and t <= y <= b


# colors palette
class Colors:
    '''
        # hex 颜色对照表    https://www.cnblogs.com/summary-2017/p/7504126.html
        # RGB的数值 = 16 * HEX的第一位 + HEX的第二位
        # RGB: 92, 184, 232 
        # 92 / 16 = 5余12 -> 5C
        # 184 / 16 = 11余8 -> B8
        # 232 / 16 = 14余8 -> E8
        # HEX = 5CB8E8
    '''

    # def __init__(self, random=0, shuffle=False):
    def __init__(self, shuffle=False):
        # hex = matplotlib.colors.TABLEAU_COLORS.values()
        hex = ('33FF00', '9933FF', 'CC0000', 'FFCC00', '99FFFF', '3300FF', 'FF3333', # new add
               'FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', 
               '1A9334', '00D4BB', '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', 
               '520085', 'CB38FF', 'FF95C8', 'FF37C7')
        
        # shuffle color 
        if shuffle:
            hex_list = list(hex)
            random.shuffle(hex_list)
            hex = tuple(hex_list)

        self.palette = [self.hex2rgb('#' + c) for c in hex]
        self.n = len(self.palette)
        # self.b = random   # also for shuffle color 


    def __call__(self, i, bgr=False):        
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod  
    def hex2rgb(h):  # int('CC', base=16) 将16进制的CC转成10进制 
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4))




def increment_path(path, exist_ok=False, sep='', mkdir=False):
    # Increment file or directory path, i.e. runs/exp --> runs/exp{sep}2, runs/exp{sep}3, ... etc.
    # Usage:
    '''
    save_dir = increment_path(Path(project) / name, exist_ok=False, sep='-')  # increment run
    save_dir.mkdir(parents=True, exist_ok=True)  # make dir 中间目录存在不报错
    '''
    path = Path(path)  # os-agnostic
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')
        dirs = glob.glob(f"{path}{sep}*")  # similar paths
        matches = [re.search(rf"%s{sep}(\d+)" % path.stem, d) for d in dirs]
        i = [int(m.groups()[0]) for m in matches if m]  # indices
        n = max(i) + 1 if i else 2  # increment number
        path = Path(f"{path}{sep}{n}{suffix}")  # increment path
    if mkdir:
        path.mkdir(parents=True, exist_ok=True)  # make directory
    return path





