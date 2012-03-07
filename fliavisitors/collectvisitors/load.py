#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from django.contrib.gis.utils import LayerMapping
from models import CAOPContinente

caop_continente_mapping = {
    'dicofre' : 'DICOFRE',
    'freguesia' : 'FREGUESIA',
    'municipio' : 'MUNICIPIO',
    'distrito' : 'DISTRITO',
    'geometry' : 'MULTIPOLYGON',
}

caop_continente_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                      'data/caop_continente.shp'))

def run(verbose=True):
    lm = LayerMapping(CAOPContinente, caop_continente_shp, 
                      caop_continente_mapping, transform=False,
                      #encoding='iso-8859-1')
                      encoding='utf-8')
    lm.save(strict=True, verbose=verbose)
