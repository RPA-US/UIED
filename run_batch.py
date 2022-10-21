import multiprocessing
import glob
import time
import json
import os
from tqdm import tqdm
from os.path import join as pjoin, exists, isfile
import cv2

import detect_compo.ip_region_proposal as ip
import detect_merge.merge as merge

def resize_height_by_longest_edge(img_path, resize_length=800):
    org = cv2.imread(img_path)
    height, width = org.shape[:2]
    if height > width:
        return resize_length
    else:
        return int(resize_length * (height / width))


if __name__ == '__main__':
    # initialization
    input_img_root = 'D:\\Repos\\Nueva carpeta\\Basic_exp\\scenario_0\\Basic_50_Balanced'
    output_root = './prediction/output/'
    cnn_type = 'custom-v2'

    os.makedirs(pjoin("", output_root), exist_ok=True)
    
    if input_img_root[-1] != "/":
        input_path_batch = input_img_root + "/"

    images_names = [f for f in os.listdir(input_path_batch) if isfile(pjoin(input_path_batch, f))]
    input_imgs = [pjoin(input_path_batch, f) for f in os.listdir(input_path_batch) if isfile(pjoin(input_path_batch, f))]

    key_params = {
        'min-grad': 3,
        'ffl-block': 5,
        'min-ele-area': 25, 
        'merge-contained-ele': True,
        'max-word-inline-gap': 10, 
        'max-line-gap': 10
    }

    is_ip = True
    is_clf = True
    is_ocr = True
    is_merge = True

    # Load deep learning models in advance
    compo_classifier = None
    if is_ip and is_clf:
        classifier = {}
        from cnn.CompDetCNN import CompDetCNN
        classifier['Elements'] = CompDetCNN(cnn_type=cnn_type)
    ocr_model = None
    if is_ocr:
        import detect_text.text_detection as text

    # set the range of target inputs' indices
    # num = 0
    # start_index = 30800  # 61728
    # end_index = 100000
    index = 0
    for input_img in input_imgs:
        #  resized_height = resize_height_by_longest_edge(input_img)
        # index = input_img.split('/')[-1][:-4]
        # if int(index) < start_index:
        #     continue
        # if int(index) > end_index:
        #     break

        if is_ocr:
            text.text_detection(input_img, output_root, show=False)

        if is_ip:
            ip.compo_detection(input_img, output_root, key_params,
                        classifier=classifier, show=False, cnn_type=cnn_type)
        if is_merge:
            compo_path = pjoin(output_root, 'ip', str(images_names[index]) + '.json')
            ocr_path = pjoin(output_root, 'ocr', str(images_names[index]) + '.json')
            merge.merge(input_img, compo_path, ocr_path, output_root, is_remove_top=key_params['remove-top-bar'], show=True)

        index += 1
        # num += 1
