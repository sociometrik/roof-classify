import rasterio
import argparse
import os

from rasterio.merge import merge
from rasterio.plot import show
from helpers import common
from helpers import vector
from helpers import raster


def get_image_list(path, extension, chunksize):
    """
    ------------------------
    Input: 
    Output:
    ------------------------
    """
    images = [img for img in common.get_matching_s3_keys(path, extension)]
    images = [images[x : x + chunksize] for x in range(0, len(images), chunksize)]

    return images


def open_image_list(images):
    """
    ------------------------
    Input: 
    Output:
    ------------------------
    """
    files = []

    for f in images:
        src = raster.get_image(f)
        files.append(src)

    return files


def get_mosaic(files):
    """
    ------------------------
    Input: 
    Output:
    ------------------------
    """

    print(files)
    mosaic, out_trans = merge(files)

    for f in files:
        f.close()

    return (mosaic, out_trans)


def write_mosaic(mosaic, out_trans, out_meta, out_fp):
    """
    ------------------------
    Input: 
    Output:
    ------------------------
    """
    out_meta.update(
        {"driver": "GTiff", "height": mosaic.shape[1], "width": mosaic.shape[2], "transform": out_trans, "compress": "lzw",}
    )

    with rasterio.open(out_fp, "w", **out_meta, BIGTIFF="IF_NEEDED") as dest:
        dest.write(mosaic)


def main():
    """
    ------------------------
    Input: 
    Output:
    ------------------------
    """
    chunksize=10
    extension='.tif'
    path = common.get_s3_paths("Bing Gorakhpur", "Bing maps imagery_Gorakhpur")


    images = get_image_list(path, extension, chunksize)
    for count, element in enumerate(images):
        
        print(count)
        files = open_image_list(element)
        out_meta = files[0].meta.copy()

        mosaic, out_trans = get_mosaic(files)
        out_fp = "chunk_{}.tif".format(count)
        write_mosaic(mosaic, out_trans, out_meta, out_fp)


if __name__ == "__main__":
    main()
