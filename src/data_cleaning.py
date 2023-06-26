# Basic imports
import pandas as pd
import numpy as np

from datetime import datetime
from pydantic import BaseModel
import re

from sklearn.base import BaseEstimator, TransformerMixin




class BathBedRatioOutlierTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
    
        X["bath_bed_ratio"] = X["bathrooms"] / X["bedrooms"]
        for idx, ratio in enumerate(X["bath_bed_ratio"]):
            if ratio >= 2:
                X.drop(idx, inplace=True)
            elif ratio <= 0.10:
                X.drop(idx, inplace=True)
        return X
    


class SqftBasementTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):

        X["sqft_basement"] = X["sqft_basement"].replace("?", np.nan)
        X["sqft_basement"] = X["sqft_basement"].astype(float)
        X["sqft_basement"] = X["sqft_living"] - X["sqft_above"]
        return X
    

class FillMissingsViewWFTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X["view"] = X["view"].fillna(0)
        X["waterfront"] = X["waterfront"].fillna(0)
        return X
    

class CalculateLastChangeTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
            last_known_change = []
            for idx, yr_re in X.yr_renovated.items():
                if str(yr_re) == 'nan' or yr_re == 0.0:
                    last_known_change.append(X.yr_built[idx])
                else:
                    last_known_change.append(int(yr_re))

            X['last_known_change'] = last_known_change
            X.drop("yr_renovated", axis=1, inplace=True)
            X.drop("yr_built", axis=1, inplace=True)
            return X
    


class DateTimeChangeTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['date'] = pd.to_datetime(X['date'])
        return X
    
    