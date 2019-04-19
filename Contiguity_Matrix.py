#!/usr/bin/env python
# coding: utf-8

from pysal.lib.weights import Queen
import numpy as np
import geopandas as gpd
import json

shp_path = "Cities.shp"
dataframe = gpd.read_file(shp_path)
dataframe.head()
dataframe["city"] = dataframe["GEONAME"] + ", " + dataframe["STATE"]


wq=Queen.from_shapefile("Cities.shp")
d = dataframe[["city"]].to_dict('index')

e = {}
for city_id, neighbor_ids  in wq.neighbors.items():
    neighbors = []
    for neighbor_id in neighbor_ids:
        neighbors.append(d[neighbor_id]["city"])
    e[d[city_id]["city"]] = neighbors

json.dump(e, open("city_neighbors.json", "w" ))
