from pathlib import Path
import rich
from omegaconf import OmegaConf, DictConfig
from datetime import datetime
from typing import Dict, List
import random
import uuid

from usls.src.utils import (
    CONSOLE, IMG_FORMAT, VIDEO_FORMAT, LABEL_FORMAT, 
    gen_random_string, get_common_files, natural_sort
)




def rename(
        directory, 
        *,
        prefix=None,
        with_num=False,
        with_znum=False,
        with_random=False,
        with_uuid=False,
    ):
    # dir will be rename at the same time, but the items in dir will not be renamed.

    # 从0开始编号，bu补0⃣️
    # 添加前缀，后缀（时间，自定义）
    # 从0开始编号，0-10位数，左补0⃣️
    # 随机生成uuid：时间，当前图片名字


    # file list
    f_list = get_common_files(directory)  
    f_list.sort(key=natural_sort)
    
    num_file = len(f_list)
    CONSOLE.log(f"Find {num_file} files (hidden files and non-suffixed files are excluded).")


    # prefix concatenation
    if prefix:
        for x in f_list:
            x.rename(x.with_stem(prefix + '-' + x.stem))


    # uuid4
    if with_uuid:
        random_strings = set()

        while len(random_strings) != num_file:
            random_strings.add(str(uuid.uuid4()))

        for x, x_ in zip(f_list, random_strings):
            x.rename(x.with_stem(x_))


    if with_num or with_znum or with_random:

        # random first
        bits = 16   # 2 bytes
        random_strings = set()
        
        while len(random_strings) != num_file:
            random_strings.add(gen_random_string(bits))
        
        for x, x_ in zip(f_list, random_strings):
            x.rename(x.with_stem(x_))


        # ordered number
        if with_num:  
            idx = 0
            for x in get_common_files(directory):
                x.rename(x.with_stem(str(idx)))
                idx += 1 


        # ordered number - zero_padding
        if with_znum:
            idx = 0
            bits = len(str(num_file))
            for x in get_common_files(directory):
                x.rename(x.with_stem(str(idx).zfill(bits)))
                idx += 1
    

    CONSOLE.log(f"Task Complete ✅")



def run_rename(args: DictConfig):
    # called by run.py
    with CONSOLE.status("[bold green]Renaming...") as status:
        rename(
            directory=args.dir,
            prefix=args.prefix,
            with_num=args.number,
            with_znum=args.zero_number,
            with_random=args.random,
            with_uuid=args.uuid,
        )


