#!/usr/bin/env python
# coding: utf-8

# ## Problem 2: Points to map
#  
# In this problem we continue to learn how to turn latitude and longitude coordinates in to geometries.
# 


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# YOUR CODE HERE 1 to read data
# Read the CSV file
data = pd.read_csv('data/some_posts.csv')

# Create an empty column
data['geometry'] = None
# Create coords to store the lons and lats
coords = []
for i in range(len(data)):
  # Set the lats and lons to the coords
  coords.append([data['lat'][i], data['lon'][i]])
# Update geometry with the coords
data['geometry'] = coords

# CODE FOR TESTING YOUR SOLUTION

# Check the result
print("Number of rows:", len(data))


# CODE FOR TESTING YOUR SOLUTION

# Check the result
print(data['geometry'].head())


# YOUR CODE HERE 2
import geopandas as gpd
from pyproj import CRS

# Convert DataFrame into a GeoDataFrame
# Create an empty GeoDataFrame
geo = gpd.GeoDataFrame()

# Create an empty list
points = []
for i in range(len(data)):
  # Store each coordinate to the points
  points.append(Point(data['geometry'][i]))

# Update geo
geo['geometry'] = points

# For problem 3, we need useid and timestanp
data_geo_useid = gpd.GeoDataFrame(data['userid'])
data_geo_ts = gpd.GeoDataFrame(data['timestamp'])

geo['userid'] = data_geo_useid
geo['timestamp'] = data_geo_ts

#print(geo)

# Set the crs as 4326
geo.crs = CRS.from_epsg(4326).to_wkt()

# Specify the file path
fp = 'Kruger_posts.shp'
# Save the data
geo.to_file(fp)

# CODE FOR TESTING YOUR SOLUTION

# Check the geodataframe head
print("Number of rows:", len(geo))
print(geo.head())


# CODE FOR TESTING YOUR SOLUTION

# Check that the output file exists
import os
assert os.path.isfile(fp), "output shapefile does not exist"


# **Finally:** 
# - **Create a simple map of the points** using the `plot()` -funtion. 

# YOUR CODE HERE 3
geo.plot()

# Well done! Now you can move on to Exercise_9_problem_3.

def func5():
    return data

def func6():
    return geo


