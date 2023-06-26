
import pandas as pd
import numpy as np
import re
from sklearn.base import BaseEstimator, TransformerMixin

from src.data_cleaning import (BathBedRatioOutlierTransformer,
                          SqftBasementTransformer,
                          FillMissingsViewWFTransformer,
                          CalculateLastChangeTransformer,
                          DateTimeChangeTransformer)

from src.feature_engineering import (PricePerSqftTransformer,
                          HouseCenterDistanceTransformer,
                          HouseWaterfrontDistanceTransformer)

from sklearn.pipeline import Pipeline



class PreprocessingKingCountyData():
    def __init__(self):
        
        # Data cleaning Pipeline 
        self.data_cleaning_pipeline = Pipeline([
            ('Bath_bed_ratio_outlier_transformer', BathBedRatioOutlierTransformer()),
            ('sqft_basement_transformer', SqftBasementTransformer()),
            ('fill_missings_view_wf_transformer', FillMissingsViewWFTransformer()),
            ('calculate_last_change_transformer', CalculateLastChangeTransformer()),
            ('datetime_change_transformer', DateTimeChangeTransformer())
            ]
        )
        
        # Feature Engineering Pipeline 
        self.Feature_Engineering_pipeline = Pipeline([
            ('price_per_sqft_transformer', PricePerSqftTransformer()),
            ('house_center_distance_transformer', HouseCenterDistanceTransformer()),
            ('house_waterfront_distance_transformer', HouseWaterfrontDistanceTransformer())
            ]
        )

        