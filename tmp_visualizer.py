'''
    Author: Ze Ma
    E-mail: maze1234556@sjtu.edu.cn
    Jan. 26, 2020
'''
import argparse

# import vision essentials
import cv2
import numpy as np
import tensorflow as tf

# # import Network
# from network_CPN101 import Network

# # pose estimation utils
# from HPE.dataset import Preprocessing
# from HPE.config import cfg
# from tfflat.base import Tester
# from tfflat.utils import mem_info
# from tfflat.logger import colorlogger
# from nms.gpu_nms import gpu_nms
# from nms.cpu_nms import cpu_nms

# import GCN utils
from graph import visualize_pose_matching
from graph  .visualize_pose_matching import *

# import my own utils
import sys, os, time
sys.path.append(os.path.abspath("./graph/"))
from utils_json import *
from visualizer import *
from utils_io_folder import *

flag_visualize = True
flag_nms = False #Default is False, unless you know what you are doing




if __name__ == '__main__':




    image_folder = "data/Data_2018/posetrack_data/images/val/"
    detections_openSVAI_folder = "data/Data_2018/posetrack_data/DeformConv_FPN_RCNN_detect//"

    output_json_folder = "data/Data_2018/posetrack_results/lighttrack/results_openSVAI/"

    visualize_folder = "data/Data_2018/posetrack_results/lighttrack/visualize/"
    output_video_folder = "data/Data_2018/videos/"

    det_file_paths = get_immediate_childfile_paths(detections_openSVAI_folder)

    for det_file_path in det_file_paths:




        json_name = os.path.basename(det_file_path)
        output_json_path = os.path.join(output_json_folder, json_name)

        video_name = json_name.split(".")[0]
        image_subfolder = os.path.join(image_folder, video_name)

        visualize_subfolder = os.path.join(visualize_folder, video_name)
        output_video_path = os.path.join(output_video_folder, video_name+".mp4")

        # visualization
        
        # create_folder(visualize_folder)
        # show_all_from_standard_json(output_json_path, classes, joint_pairs, joint_names, image_folder, visualize_folder, flag_track = True)
        # print("Pose Estimation Finished!")

        img_paths = get_immediate_childfile_paths(visualize_subfolder)
        make_video_from_images(img_paths, output_video_path, fps=10, size=None, is_color=True, format="XVID")

    print("Finished video {}".format(output_video_path))
