# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:28:07 2023

@author: turnerp
"""

import pandas as pd
import numpy as np
import pickle
import xmltodict
import os
from glob2 import glob
import tifffile
import json
import scipy
import cv2
from skimage.registration import phase_cross_correlation
from skimage.registration._phase_cross_correlation import _upsampled_dft
import tempfile
import hashlib
from tiler import Tiler, Merger
import datetime
from multiprocessing import Pool
import tqdm
import traceback
from functools import partial
import matplotlib.pyplot as plt



def fix_strain_phenotype(dat):
    
    folder = dat["folder"]
    antibiotic = dat["antibiotic"]
    
    strain = folder.split("_")[2]

    phenotype = "Untreated"  
    
    if antibiotic not in ["None",np.nan, None]:
        if strain == "L11037":
            phenotype = "Treated Resistant"
        if strain == "L484840":
            phenotype = "Treated Sensitive"
        if strain == "L10081":
            phenotype = "Treated Sensitive"
        if strain == "L27336":
            if antibiotic == "Ciprofloxacin":
                phenotype = "Treated Sensitive"
            if antibiotic == "Gentamicin":
                phenotype = "Treated Sensitive"
            if antibiotic == "Ceftriaxone":
                    phenotype = "Treated Resistant"    
    else:
        antibiotic = "None"
    
    dat["strain"] = strain
    dat["phenotype"] = phenotype
    dat["antibiotic"] = antibiotic
    
    return dat

def get_cell_counts(user_metadata, curated = True):
    
    cell_count = user_metadata.copy()
    cell_count = cell_count.drop_duplicates(["folder","segmentation_file"])
    
    if curated:
        cell_count = cell_count[(cell_count["segmentation_curated"] == True)]
    
    cell_count = cell_count[["strain","antibiotic","num_segmentations","user_meta3"]]
    
    cell_count = cell_count.groupby(["strain","antibiotic"]).agg({**{"num_segmentations": lambda x: sum(x)}})
    
    cell_count = cell_count.sort_values(["strain","antibiotic"])
    
    total_cell_count = cell_count["num_segmentations"].sum()
    
    return cell_count, total_cell_count




user_initial = "AF"

user_metadata_path = os.path.join(r"\\physics\dfs\DAQ\CondensedMatterGroups\AKGroup\Piers\AKSEG\Images", user_initial, f"{user_initial}_file_metadata.txt")
user_metadata = pd.read_csv(user_metadata_path, sep="\t", low_memory=False)

# print(user_metadata.columns.tolist())


# xx = user_metadata.to_dict("records")











# antibiotics = user_metadata.antibiotic.drop_duplicates()


# num_curated = user_metadata[["segmentation_file","segmentation_curated","folder"]][user_metadata["segmentation_curated"] == True].drop_duplicates()
# 


# user_metadata = user_metadata.apply(lambda dat: fix_strain_phenotype(dat), axis=1)
# user_metadata.to_csv(user_metadata_path, sep=",", index=False)


# phenotype_data = user_metadata[["strain","antibiotic","phenotype"]].drop_duplicates()
# phenotype_data = phenotype_data.sort_values(["strain","antibiotic","phenotype"])
# conditions = user_metadata[["strain","antibiotic","user_meta3","user_meta4"]].drop_duplicates()

# cell_count, total_cell_count = get_cell_counts(user_metadata, curated = True)



# user_metadata["strain"] = user_metadata["folder"].str.split("_").str[2]
# user_metadata.to_csv(user_metadata_path, sep=",", index=False)


# strains = np.unique(user_metadata["strain"].tolist(), return_counts=True)
# 

# nan_data = user_metadata[user_metadata["strain"].isna()]
# curated_data = user_metadata[user_metadata["segmentation_curated"] == True]



# phenotype_data = user_metadata[["strain","antibiotic","phenotype"]].drop_duplicates()








# with open('user_metadata.pickle', 'wb') as handle:
#     pickle.dump(user_metadata, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('user_metadata.pickle', 'rb') as handle:
#     user_metadata = pickle.load(handle)

# user_metadata.drop(user_metadata.columns[16],axis=1,inplace=True)
# user_metadata.to_csv(user_metadata_path, sep=",", index=False)

# user_metadata = user_metadata.head()

# user_metadata = user_metadata.drop(index=16, axis=1)

# cols = user_metadata.columns