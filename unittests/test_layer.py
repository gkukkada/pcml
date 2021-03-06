"""
Copyright (c) 2014 High-Performance Computing and GIS (HPCGIS) Laboratory. All rights reserved.
Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.
Authors and contributors: Eric Shook (eshook@kent.edu); Zhengliang Feng (odayfans@gmail.com, zfeng2@kent.edu)
"""
from pcml import *
from pcml.util.Messaging import PCMLNotImplemented
from pcml.util.LayerBuilder import lst_to_layer
from numpy.ma import allequal
import numpy as np
import unittest

class TestLayer(unittest.TestCase):
    def setUp(self):
        # Basic layer from origin to h X w
        self.layer1=Layer(0,0,100,100,"Layer One")
        # Layer that overlaps the origin including negative coordinates
        self.layer2=Layer(-10,-10,20,20,"Layer Two")
        # Layer that is entirely negative
        self.layer3=Layer(-100,-100,10,10,"Layer Three")
        # Layer that is entirely positive 
        self.layer4=Layer(100,100,10,10,"Layer Four")

        # Layer that has floating point y,x,h,w 
        self.layer5=Layer(-1.2,-3.4,5.6,7.8,"Layer Five")

    # Test the return from repr for example layers 
    def test_layer_repr(self):
        layer1_test = "<Layer: (%f,%f) [%f,%f] : %s>" % (0,0,100,100,"Layer One")
        layer2_test = "<Layer: (%f,%f) [%f,%f] : %s>" % (-10,-10,20,20,"Layer Two")
        layer3_test = "<Layer: (%f,%f) [%f,%f] : %s>" % (-100,-100,10,10,"Layer Three")
        layer4_test = "<Layer: (%f,%f) [%f,%f] : %s>" % (100,100,10,10,"Layer Four")
        layer5_test = "<Layer: (%f,%f) [%f,%f] : %s>" % (-1.2,-3.4,5.6,7.8,"Layer Five")
        self.assertEqual(layer1_test,repr(self.layer1))
        self.assertEqual(layer2_test,repr(self.layer2))
        self.assertEqual(layer3_test,repr(self.layer3))
        self.assertEqual(layer4_test,repr(self.layer4))
        self.assertEqual(layer5_test,repr(self.layer5))


    # Test the defaults for one layer - logic applies to all so only need to test one
    def test_layer_defaults(self):
        self.assertEqual(self.layer5.y, -1.2)
        self.assertEqual(self.layer5.x, -3.4)
        self.assertEqual(self.layer5.h, 5.6)
        self.assertEqual(self.layer5.w, 7.8)
        self.assertEqual(self.layer5.title, "Layer Five")
        self.assertEqual(self.layer5._data, None)
        self.assertEqual(self.layer5.data_structure, Datastructure.array)
        self.assertEqual(self.layer5.data_type, None)
        self.assertEqual(self.layer5.nodata_value, None)
        self.assertEqual(self.layer5.cellsize, None)
        self.assertEqual(self.layer5.nrows, None)
        self.assertEqual(self.layer5.ncols, None)
       
    # Ensure no negative or zero heights or widths are accepted 
    def test_layer_initialization(self):
        with self.assertRaises(PCMLInvalidInput):
            failedlayer=Layer(0,0,-10,1,'f')
        with self.assertRaises(PCMLInvalidInput):
            failedlayer=Layer(0,0,1,-10,'f')
        with self.assertRaises(PCMLInvalidInput):
            failedlayer=Layer(0,0,0,1,'f')
        with self.assertRaises(PCMLInvalidInput):
            failedlayer=Layer(0,0,1,0,'f')


    # FIXME: Tests to be written
    '''
    duplicate
    decomposition
    rowdecomposition
    __add__
    __mul__
    '''
