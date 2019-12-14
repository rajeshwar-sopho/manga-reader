import os
import sys

import requests
import shutil
from helpers import fix_name

try:
    # path to the saving directory
    os.chdir(sys.argv[3])
except Exception as e:
    print(e, 'occured!')
    print('Seems like url files are missing for this manga!')
    exit

############## helpers ##############

# parse file to get newline seperated content
def parse_file(working_path):
    ret_list = list()

    if not os.path.isfile(working_path):
        print(f'{working_path} does not exists please re-run the download_url_files.py!')
        exit

    with open(working_path, 'r') as f:
        ret_list = f.read().split('\n')
    # last element of ret_list is always ""
    ret_list.pop(-1)
    return ret_list

# saves the image present at the url
def save_image(url, out_file):
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        # save the image
        with open(out_file, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        log_file.write(f'<<<DOWNLOADED>>> {url}')
        log_file.write(f'<<<STORED AT>>> {out_file}\n')
        print(f'<<<DOWNLOADED>>> {out_file}')
    else:
        log_file.write(f'<<<FAILED :: {res.status_code}>>> {url}')
        print(f'<<<FAILED>>> {out_file}')

# get chapters to download
def ch_downloads():
    # file starting form first chapter
    all_chs = parse_file('chapter_names.txt')

    # chapters in range of start and end
    start, end = sys.argv[1], sys.argv[2]

    if start != 'pass' and end != 'pass':
        print(f'returning chapters from {start} to {end}')
        return all_chs[int(start) - 1:int(end) - 1]
    else:
        # else just download the latest chapter
        return [all_chs[-1]]

############## end-helpers ##############

# paths to chapters for download
save_dir_list = ch_downloads()

for save_dir in save_dir_list:
    # logging details of download
    if os.path.isfile(save_dir + '\\download-logs.txt'):
        # if log file already there
        log_file = open(save_dir + '\\download-logs.txt', 'a+')
    else:
        log_file = open(save_dir + '\\download-logs.txt', 'w+')

    # list of urls from website using javascript in chrome devtools console
    url_list = parse_file(save_dir + '\\urls.txt')

    for i, url in enumerate(url_list):
        # fix name for storing in windows
        filename, file_extension = os.path.splitext(url)
        out_file = save_dir + '\\' + str(i) + file_extension

        # if download is restarted after getting aborted
        if os.path.isfile(out_file):
            # if file is already downloaded skip over it
            continue
        else:
            save_image(url, out_file)

    log_file.close()