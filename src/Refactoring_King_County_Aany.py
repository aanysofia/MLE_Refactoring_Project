import pandas as pd
import numpy as np

def bath_bed_ratio_outlier(df):
    df.copy()
    df["bath_bed_ratio"] = df["bathrooms"] / df["bedrooms"]
    for idx, ratio in enumerate(df["bath_bed_ratio"]):
        if ratio >= 2:
            df.drop(idx, inplace=True)
        elif ratio <= 0.10:
            df.drop(idx, inplace=True)
    return df


def sqft_basement(df):
    df.copy()
    df["sqft_basement"] = df["sqft_basement"].replace("?", np.nan)
    df["sqft_basement"] = df["sqft_basement"].astype(float)
    df["sqft_basement"] = df["sqft_living"] - df["sqft_above"]
    return df


def fill_missings_view_wf(df):
    df.copy()
    df["view"] = df["view"].fillna(0)
    df["waterfront"] = df["waterfront"].fillna(0)
    return df


def Calculate_last_change(df):
    df.copy()
    last_known_change = []
    for idx, yr_re in df.yr_renovated.items():
        if str(yr_re) == 'nan' or yr_re == 0.0:
            last_known_change.append(df.yr_built[idx])
        else:
            last_known_change.append(int(yr_re))

    df['last_known_change'] = last_known_change
    df.drop("yr_renovated", axis=1, inplace=True)
    df.drop("yr_built", axis=1, inplace=True)
    return df

def date_time_change(df):
    df.copy()
    df['date'] = pd.to_datetime(df['date'])
    return df

## Feature Engineering

def price_per_sqft(df):
    df.copy()
    df['sqft_price'] = (df.price/(df.sqft_living + df.sqft_lot)).round(2)
    return df

def house_center_distance(df):
    df.copy()
    df['delta_lat'] = np.absolute(47.62774- df['lat'])
    df['delta_long'] = np.absolute(-122.24194-df['long'])
    df['center_distance']= ((df['delta_long']* np.cos(np.radians(47.6219)))**2 
                                   + df['delta_lat']**2)**(1/2)*2*np.pi*6378/360
    return df

def house_beach_promenade_distance(long, lat, ref_long, ref_lat):
    delta_long = long - ref_long
    delta_lat = lat - ref_lat
    delta_long_corr = delta_long * np.cos(np.radians(ref_lat))
    return ((delta_long_corr)**2 +(delta_lat)**2)**(1/2)*2*np.pi*6378/360   

def house_waterfront_distance(df):
    df.copy()
    water_list= df.query('waterfront == 1')
    water_distance = []
    for idx, lat in df.lat.iteritems():
        ref_list = []
        for x,y in zip(list(water_list.long), list(water_list.lat)):
            ref_list.append(house_beach_promenade_distance(df.long[idx], df.lat[idx],x,y).min())
        water_distance.append(min(ref_list))
    
    df['water_distance'] = water_distance
    return df