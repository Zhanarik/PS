import os
import argparse
import rasterio
import numpy as np
from glob import glob
from tqdm import tqdm
from shutil import copyfile
from skimage import feature
from functools import partial
from os.path import dirname as up
from skimage.color import rgb2gray
from joblib import Parallel, delayed
from skimage.feature import graycomatrix, graycoprops, local_binary_pattern
root_path = up(up(up(os.path.abspath(__file__))))

np.seterr(divide='ignore', invalid='ignore')

# Bands number is based on
# 1:nm440  2:nm490  3:nm560  4:nm665  5:nm705  6:nm740  7:nm783  8:nm842  9:nm865  10:nm1600  11:nm2200

def ndvi(band4, band8):
    return (band8 - band4)/(band8 + band4)


def fdi(band6, band8, band10):
    l_nir = 833.0
    l_redge = 740.0
    l_swir = 1614.0

    r_acc = band6 + 10 * (band10 - band6) * (l_nir - l_redge) / (l_swir - l_redge)

    return band8 - r_acc

def ndwi(band3, band8):
    return (band3 - band8)/(band3 + band8)


def indices(image):
    output_path = os.path.join(up(up(up(image))), 'indices', '_'.join(os.path.basename(image).split('_')[:-1]))
    output_image = os.path.join(output_path, os.path.basename(image).split('.')[0] + '_si.tif')
    os.makedirs(output_path, exist_ok=True)

    # Copy _conf.tif and _cl.tif for seamless integration with spectral_extraction.py
    src_conf = os.path.abspath(image.split('.tif')[0] + '_conf.tif')
    dst_conf = os.path.join(output_path, os.path.basename(image).split('.')[0] + '_conf.tif')
    copyfile(src_conf, dst_conf)

    src_cl = os.path.abspath(image.split('.tif')[0] + '_cl.tif')
    dst_cl = os.path.join(output_path, os.path.basename(image).split('.')[0] + '_cl.tif')
    copyfile(src_cl, dst_cl)

    # Read metadata of the initial image
    with rasterio.open(image, mode='r') as src:
        tags = src.tags().copy()
        meta = src.meta

    # Update meta to reflect the number of layers
    meta.update(count=8)

    # Write it to stack
    with rasterio.open(output_image, 'w', **meta) as dst:
        with rasterio.open(image, mode='r') as src:
            NDVI = ndvi(src.read(4), src.read(8))
            dst.write_band(1, NDVI)

            FDI = fdi(src.read(6), src.read(8), src.read(10))
            dst.write_band(3, FDI)

            NDWI = ndwi(src.read(3), src.read(8))
            dst.write_band(5, NDWI)


        dst.update_tags(**tags)

def main(options):
    patches = glob(os.path.join(options['path'], 'patches', '*/*.tif'))
    patches = [p for p in patches if ('_cl.tif' not in p) and ('_conf.tif' not in p)]

    for image in tqdm(patches):
        indices(image)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Options
    parser.add_argument('--path', default=os.path.join(root_path, 'data'), help='Path to dataset')
    parser.add_argument('--type', default='indices', type=str, help=' Select between indices or texture or spatial or lbp')
    parser.add_argument('--n_jobs', default= -2, type=int, help='How many cores?')

    args = parser.parse_args()
    options = vars(args)  # convert to ordinary dict

    main(options)
