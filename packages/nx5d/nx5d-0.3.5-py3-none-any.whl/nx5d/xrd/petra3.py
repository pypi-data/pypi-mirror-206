#!/usr/bin/python

import numpy as np

''' Valid at one point in history
'''
P08Experiment = {
    'goniometerAxes': ('y-', 'x+', 'z+'),
    'detectorTARAxes': ('y-', None, None),
    'imageAxes': ('x-', 'z-'),
    'imageSize': (516, 1554),
    'imageCenter': (90, 245),
    'imageDistance': 950,
    'imageChannelSize': (0.055, 0.055),
    'sampleFaceUp': 'z+',
    'beamDirection': (1, 0, 0),
    'sampleNormal': (0, 0, 1),
    'beamEnergy': 9000,
    'goniometerAngles': {
        'theta': '@/fio/data/om',
        'phi': np.array([0]*61), #'@/fio/data/phi',
        'chi': np.array([90]*61)
    },
    'detectorTARAngles': {
        'azimuth': '@/fio/data/tt_position'
    }
}
