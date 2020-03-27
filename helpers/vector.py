# Import packages
import fiona
import pyproj
import numpy as np

# Import sub-modules for area calculation
from area import area
from helpers import common
from helpers import raster
from functools import partial
from shapely.ops import transform
from shapely.geometry import shape





def open_shape_file(path):
    '''
    ------------------------
    Input: 
    Output:
    ------------------------
    '''
    f = fiona.open(path, 'r')
    
    return(f)


def get_shapes(shape):
    '''
    ------------------------
    Input: 
    Output:
    ------------------------
    '''
    shapes = [feature["geometry"] 
              for feature in shape 
              if feature["geometry"] is not None]
    
    return(shapes)


def get_poly_area(shapes):
    '''
    ------------------------
    Input: 
    Output:
    Source: https://github.com/scisco/area
    ------------------------
    '''
    areas = np.array([area(obj) for obj in shapes]).sum()
    areas = areas/(1000*1000)
    
    return(areas)
    


def calculate_area_proportion(shapes, path):
    '''
    ------------------------
    Input: 
    Output:
    ------------------------
    '''
    vec = vector.get_area(shapes)
    ras = raster.get_area(path)
    proportion = (vec/ras)*100
    
    return(proportion)