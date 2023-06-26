# Basic imports
import pandas as pd
import numpy as np

from datetime import datetime
from pydantic import BaseModel
import re

from sklearn.base import BaseEstimator, TransformerMixin


class PricePerSqftTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['sqft_price'] = (X.price/(X.sqft_living + X.sqft_lot)).round(2)
        return X
    

class HouseCenterDistanceTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):

        X['delta_lat'] = np.absolute(47.62774- X['lat'])
        X['delta_long'] = np.absolute(-122.24194-X['long'])
        X['center_distance']= ((X['delta_long']* np.cos(np.radians(47.6219)))**2 
                                    + X['delta_lat']**2)**(1/2)*2*np.pi*6378/360
        return X
    

class HouseWaterfrontDistanceTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        def house_beach_promenade_distance(long, lat, ref_long, ref_lat):
            delta_long = long - ref_long
            delta_lat = lat - ref_lat
            delta_long_corr = delta_long * np.cos(np.radians(ref_lat))
            return ((delta_long_corr)**2 +(delta_lat)**2)**(1/2)*2*np.pi*6378/360
        
        water_list= X.query('waterfront == 1')
        water_distance = []
        for idx, lat in X.lat.iteritems():
            ref_list = []
            for x,y in zip(list(water_list.long), list(water_list.lat)):
                ref_list.append(house_beach_promenade_distance(X.long[idx], X.lat[idx],x,y).min())
            water_distance.append(min(ref_list))
        
        X['water_distance'] = water_distance
        return X
    
    