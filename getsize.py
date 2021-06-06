#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# get and print folder size with appropriate label (only for folders < 500TB)

import os

def get_size(parent_folder):
    total_size = 0
    for folder, _, files in os.walk(parent_folder):
        for file_ in files:
            fp = os.path.join(folder, file_)
            # skip symbolic links
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def sizelabel(parent_folder='.'):
    sb = get_size(parent_folder)
    d = {'KB': sb*1e-3,
         'MB': sb*1e-6,
         'GB': sb*1e-9,
         'TB': sb*1e-12 }

    for key, value in d.items():
        if value >= 0.5 and value < 500:
            return f'{round(value, 2)} {key}'
    return f'{sb} bytes'


print(sizelabel())

