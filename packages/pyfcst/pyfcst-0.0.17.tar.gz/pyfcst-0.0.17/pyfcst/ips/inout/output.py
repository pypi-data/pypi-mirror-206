#! /usr/bin/env python
# -*- coding: utf-8 -*-
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AFCC Development Team
# License: TBD
# Copyright (c) 2012, TBD

r"""
***************************************************************************
:mod:`pyfcst.ips.inout.output` -- Input and Output interface module for IPS
***************************************************************************
"""

import numpy as np
import scipy
import os
from PIL import Image


class writer:
    r"""
    Output for various file formats.
    Formats currently supported are tiff stacks, sequence of images (png,jpg,gif,tiff), Legacy VTK, VTI
    data, fname=None, voxelsize = [1,1,1]

    Parameters
    ----------
    data : ndarray
       Numpy array with the data to be exported to the file.
       3D array is expected as input.


    fname : string
        Filename to export.
        The supported file formats are::
        1. tiff
        2. legacy vtk
        3. gif
        4. jpg,jpeg
        5. png
        6. python dump file
        7. vti

     voxelsize: tuple
        Pixel size in X,Y,Z direction
        To be specified as [2,2,2] for a pixel size of 2 in each direction



    Examples
    --------

    >>> import pylab as pl
    >>> import pyfcst as PFC
    >>> import pyfcst.ips.inout as io
    >>> crunch = io.writer(data, filename='../examples/IPS/fib.tif',loglevel=40)



    .. warning:: This documentation is not yet finished.

    .. todo:: 1. Finish documentation

    """
    def __init__(self, data, fname = None, voxelsize=[1,1,1], sequence=False, indent='\t', **kwargs):

        (path,filename) = os.path.split(fname)
        extension = os.path.splitext(filename)[1]
        self._indent=indent
        self._spacing=voxelsize

        if extension == '.tiff' or extension == '.tif' or extension == '.TIFF' or extension == '.TIF':
            self.writeStack(fname, data)
        elif extension == '.vti':
            self.writeVTI(fname, data)
        elif sequence==True:
            self.writeSequence(fname,data)
            print (self._indent, "= The file has been successfully written!")
        elif extension == '.vtk' or extension == '.VTK':
            self.writeVTK(fname,data)
        elif extension == '':
            import pickle
            print (self._indent, "="*50)
            print (self._indent, "=  Writing a python dump file")
            f=open(fname,'w')
            pickle.dump(data,f)
            f.close()


    def writeSequence(self, filename, image):

        basename,extension=os.path.splitext(filename)
        print (self._indent, "="*50)
        print (self._indent, "=  Writing TIFF files")
        print (self._indent, "= - Writing z-slices")
        for ii in range(image.shape[2]):
            Image.fromarray(image[:,:,ii]).save(basename + f"_{ii:03d}.tiff")
        print (self._indent, "= The file has been successfully written!")
        print (self._indent, "-"*50)

    def writeStack(self, filename, image):

        import libtiff as l
        a,b,c = image.shape
        tmp=[]
        for i in range(c):
            tmp.append(np.asarray(image[:,:,i]))
        print (np.shape(tmp))
        print (self._indent, "="*50)
        print (self._indent, "=  Writing TIFF stack")
        tif=l.TIFFimage(np.asarray(tmp,dtype=np.uint8),description='')
        flag=tif.write_file(filename,compression='none')
        if flag==1:
            print (self._indent, "=  Stack written successfully")
        else:
            print (self._indent, "=  Error in writing file")
        print (self._indent, "-"*50)




    def writeVTI(self, filename, image):

        """ Save Image file as VTI file """
        print (self._indent, "="*50)
        print (self._indent, "=  Writing VTI file")
        filename = os.path.splitext(filename)[0]
        print (self._indent, "=\t- Writing Material IDs")
        from pyevtk.hl import imageToVTK
        imageToVTK(filename,pointData=image,spacing=self._spacing)
        print (self._indent, "= The file has been successfully written!")
        print (self._indent, "-"*50)


    def writeVTK(self, filename, image):

        import pyfcst.ips.util as util
        obj = util.GridGenerator(image,filename)
        obj.write()



    def writeCSV(self, filename, image):

        scipy.savetxt(filename,image,delimiter=',')
