'''
Author: Yorai Shaoul
Date: 2023-02-05

Example script for synthesizing data in new camera-models from the TartanAir dataset.
'''

# General imports.
import sys
import numpy as np
from scipy.spatial.transform import Rotation

# Local imports.
sys.path.append('..')
import tartanair as ta

# Create a TartanAir object.
tartanair_data_root = '/media/yoraish/overflow/data/tartanair-v2'
ta.init(tartanair_data_root)

# Create the requested camera models and their parameters.
R_raw_new0 = Rotation.from_euler('y', 90, degrees=True).as_matrix().tolist()

cam_model_0 = {'name': 'pinhole', 
                'raw_side': 'left', # TartanAir has two cameras, one on the left and one on the right. This parameter specifies which camera to use.
               'params': 
                        {'fx': 320, 'fy': 320, 'cx': 320, 'cy': 320, 'width': 640, 'height': 640},
                'R_raw_new': R_raw_new0}

R_raw_new1 = Rotation.from_euler('xyz', [45, 0, 0], degrees=True).as_matrix().tolist()

cam_model_1 = {'name': 'doublesphere',
                'raw_side': 'left',
                'params':
                        {'fx': 250, 
                        'fy':  250, 
                        'cx': 500, 
                        'cy': 500, 
                        'width': 1000, 
                        'height': 1000, 
                        'alpha': 0.6, 
                        'xi': -0.2, 
                        'fov_degree': 195},
                'R_raw_new': np.eye(3).tolist()}

cam_model_2 = {'name': 'radtan', # TUM Fisheye parameters for cam0.
                'raw_side': 'left',
                'params':
                        {
                        'fx': 190.9227077601815,
                        'fy': 190.89761005621563,
                        'cx': 254.9135474328476,
                        'cy': 256.8281792099312,
                        'width': 1000,
                        'height': 1000,
                        'k1': 0.6288947328627524,
                        'k2': 1.0441360489134845,
                        'p1': 0.1,
                        'p2': 0.1},
                'R_raw_new': np.eye(3).tolist()}

ta.customize(env = 'MiddleEastExposure', difficulty = 'easy', trajectory_id = ['P000'], modality = ['image'], new_camera_models_params=[cam_model_1], num_workers = 12, device='cuda') # Or cpu.
