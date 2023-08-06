#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AFCC Development Team
# License: TBD
# Copyright (c) 2012, TBD

r"""
*********************************************************************
`pyfcst.ips.inout.input` -- Input and Output interface module for IPS
*********************************************************************
"""

import scipy as sp
from libtiff import TIFF
import numpy as np
import array
import os, sys
from PIL import Image



class reader:

    r"""
    Input reader for various file formats.
    Formats currently supported are tiff stacks, sequence of images (png,jpg,gif,tiff), MRC
    fname=None, sequence='no'

    Parameters
    ----------
    fname : string
        Filename to import.
        The supported file formats are::
        1. tiff
        2. mrc
        3. gif
        4. jpg,jpeg
        5. png
        6. python dump file
    sequence : string
        Whether to read a sequence of images or a single image. Default = 'no'.
        Other values are 'yes'.



    Examples
    --------

    >>> import pylab as pl
    >>> import pyfcst as PFC
    >>> import pyfcst.ips.inout as io
    >>> crunch = io.reader(fname='../examples/IPS/fib.tif',loglevel=40)
    >>> image = crunch.getarray()

    .. warning:: This documentation is not yet finished.

    .. todo:: 1. Write VTK reader
              2. Finish documentation

    """
    def __init__(self, fname=None, indent='\t',sequence='no', **kwargs):
        try:

            print ("")
            print("\t Initialize image reader")

            self._image = None
            self._loaded = False

            (path,filename) = os.path.split(fname)
            extension = os.path.splitext(filename)[1]

            self._indent=indent

            if sequence=='no':

                if extension == '.mrc' or extension == '.MRC':
                    print("\t- Detect mrc file")
                    self._image = self.readMRC(fname)

                elif extension.lower() == '.tif' or extension.lower() == '.tiff' or extension.lower() == '.jpg' or extension.lower() == 'jpeg' or extension.lower() == '.png':
                    print("\t- Detect Supported image file/stack")
                    self._image = self.readStack(fname)

                elif extension == '.vti' or extension == '.vtk' or extension == '.vtu':
                    self._logger.error("VTK currently notimplemented")
                    sys.exit("\t=Exiting code execution")

                elif extension == '':
                    print("t- Reading a python dump file")
                    try:
                        f=open(fname)
                        import pickle
                        self._image = pickle.load(f)
                        print ("= Read a file with dimensions = ", np.shape(self._image))
                    except IOError:
                        print (self._indent, "= The file",filename,"could not be found")
                        print (self._indent, "= Please check the filename and try again")
                        self._image = None
                else:
                    self._logger.error("Unsupported filetype passed")

            else:
                self._image = self.readSequence(fname)

            if self._image is None:
                self._loaded = False
            else:
                self._loaded = True
                print ("")
                print (self._indent, " Datatype:      ", self._image.dtype)
                print (self._indent, " Minimum value: ", self._image.min())
                print (self._indent, " Maximum value: ", self._image.max())
                print (self._indent, " Storage requirement (bit): ",sp.log2(self._image.max()-self._image.min()+1))
                print ("")
        except ValueError:
            print (self._indent, "= The file",filename,"could not be read")
            print (self._indent, "= Please check the filename and try again")

    def getarray(self):

        return self._image

    def readStack(self, filename):
        try:
            im=Image.open(filename)
        except IOError:
            print (self._indent, "= The file",filename,"could not be found")
            print (self._indent, "= Please check the filename and try again")
            return None
        if os.path.splitext(filename)[1].lower() == '.tif' or os.path.splitext(filename)[1].lower() == '.tiff':
            tif=TIFF.open(filename)
            tmp = []
            for frame in tif.iter_images():
                tmp.append(frame)
            print("\t  Number of Images "+ str(len(tmp)) )
            print("\t  Image Size       (" + str(tmp[0].shape) + ")")
            image = np.dstack(tmp)
        else:
            image = np.asarray(Image.open(filename))
            print("\t  Number of Images: 1")
            print("\t  Image Size       (" +
                              str(image.shape[0]) +
                              ", " +
                              str(image.shape[1]) +
                              ", 1)")
        return image

    def readSequence(self, filename):

        path,name = os.path.split(filename)
        basename,extension = os.path.splitext(name)
        filenames=[]
        tmp=[]
        self.metaData={}
        try:
            filenames += [each for each in os.listdir(path) if each.endswith(extension)]
            filenames = np.sort(filenames)
            print (self._indent, " Reading files in sequence from the folder: ", path)
            for ii,imname in enumerate(filenames):
                imname=os.path.join(path,imname)
                tmp.append(np.asarray(Image.open(imname)))
                # self.metaData["Slice"+str(ii+1)]=self.readMetaData(imname)


        except IOError:
            print (self._indent, "= Reached end of sequence", basename)
            print (self._indent, "= Read a total of", len(tmp)," images")

        image = np.dstack(tmp)

        return image

    def readMRC(self, filename):

        try:
            f=open(filename,'r')
        except IOError:
            print (self._indent, "= The file",filename,"could not be found")
            print (self._indent, "= Please check the filename and try again")
            self._image = None
            return 0


        header=array.array("i")
        header.fromfile(f,56)


        nx = header[0] #Number of columns in image matrix
        ny = header[1] #Number of rows in image matrix
        nz = header[2] #Number of sections in the image
        typ= header[3] #Type of the Image (type = '1' for 16 bit image and '2' for 32-bit real image)

        #Starting point of image
        nxstart = header[4]
        nystart = header[5]
        nzstart = header[6]

        #Grid size in X,Y,Z
        mx = header[7]
        my = header[8]
        mz = header[9]

        #Cell Size; pixel spacing = xlen/mx, ylen/my, zlen/mz
        xlen = header[10]
        ylen = header[11]
        zlen = header[12]

        #Cell Angles
        alpha = header[13]
        beta = header[14]
        gamma = header[15]

        #Mapping; needs to be set to 1,2,3 for x,y,z respectively
        mapc = header[16]   #map column
        mapr = header[17]   #map row
        maps = header[18]   #map section

        #Pixel Value Statistics
        amin = header[19]   #minimum pixel value
        amax = header[20]   #maximum pixel value
        amean = header[21]  #mean pixel value

        ispg = header[22]   #space group number
        offset = header[23] #Number of bytes added to extended header

        # The further header values can be ignored as they do not provide any relevant information about the image

        if nx > 100000 or nx < 0 or ny > 100000 or ny < 0 or nz > 100000 or nz < 0:
            header.byteswap()   #since data is in little endian format we need to swap the bytes
            nx = header[0]      # Number of columns in image matrix
            ny = header[1]      # Number of rows in image matrix
            nz = header[2]      # Number of sections in the image
            typ= header[3]      # Type of the Image (type = '1' for 16 bit image and '2' for 32-bit real image)



        print (self._indent, "="*50)
        print (self._indent, "= File statistics are as follows: ")
        print (self._indent,"= Number of columns =", nx)
        print (self._indent,"= Number of rows    =", ny)
        print (self._indent,"= Number of slices =", nz)
        print (self._indent,"= Data type identifier =", typ)
        print (self._indent,"= Image size in X =", mx ," angstrom")
        print (self._indent,"= Image size in Y =", my ," angstrom")
        print (self._indent,"= Image size in Z =", mz ," angstrom")
        print (self._indent,"= Minimum pixel value =", amin)
        print (self._indent,"= Maximum pixel value =", amax)
        print (self._indent,"= Extended header byte count = ", offset)
        print (self._indent, "="*50)

        f.seek(1024+offset) #Seeking the start actual data (excluding the header (1024 bytes)+extended header )
        if typ==0:
            datatype="B"
        elif typ==1:
            datatype="h"
        elif typ==2:
            datatype="f"
        elif typ==6:
            datatype="H"

        # Read the file according to the dimensions obtained (nx,ny,nz)
        imsize=nx*ny
        tmp=[]
        for ii in range(nz):
            try:
                a=array.array(datatype)
                a.fromfile(f,imsize)
                #Image.fromarray(image[:,:]).save("EA50" + f"_{ii:3d}.tiff")
                #a=array.array("H")

            except (EOFError):
                print (self._indent,"= End of file reached !! Not enough slices...!!")
                print (self._indent,"= Read a total of ", ii, " slices")
                nz = ii
                break
            tmp.append(np.asarray(np.reshape(a,[nx,ny])))

        image = np.dstack(tmp)
        return image

    def readMetaData(self,filename):
        try:

            f=open(filename)
            tmp=[]
            tmp.append(f.readlines())
            tmp=np.asarray(tmp)
            i1,i2=np.where(tmp=='[System]\r\n')
            print (i1)
            print (i2)
            tmp=np.asarray(tmp[i1,i2:-1]).flatten()
            a=[]
            for item in tmp:
                a.append(item[0:-2])
            tmp=np.asarray(a)
            metaData={}

            for item in tmp:
                if item!='':
                    if item[-1]==']':
                        tag=item[1:-1]
                        metaData[tag]={}


                    else:
                        index=[i for i, ltr in enumerate(item) if ltr == '=']
                        metaData[tag][item[0:index[0]]]=item[index[0]+1:-1]+item[-1]

            for i,item in enumerate(metaData):
                for i,j in metaData[item].iteritems():
                    try:
                        metaData[item][i]=float(j)
                    except ValueError:
                        metaData[item][i]=j
            return metaData

        except IOError:
            return

if __name__ == '__main__':
    im=reader('stack1.tiff').getarray()
