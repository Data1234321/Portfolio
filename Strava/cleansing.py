"""
Docstrings: 
Class to clean strava data
"""

import pandas as pd

class cleansing_steps:
    def __init__(self, data):
        self.data = data

    def cleanse(self):
        """
        Function to cleanse data from dataset
        - Removing columns
        - Converting date column to datetime
        - Converting strings to integers
        - Setting correct index
        - Renaming columns
        """
        strava_df = self.data.drop(columns=[
            'Relative Effort', 'Commute',
            'Activity Private Note',
            'Activity Gear','Filename',
            'Athlete Weight', 'Bike Weight',
            'Elapsed Time.1', 'Average Speed',
            'Average Positive Grade', 'Average Negative Grade',
            'Max Cadence', 'Average Cadence',
            'Max Watts', 'Average Watts',
            'Max Temperature', 'Average Temperature',
            'Relative Effort.1', 'Total Work',
            'Number of Runs', 'Uphill Time',
            'Downhill Time', 'Other Time',
            'Type', 'Weighted Average Power',
            'Power Count', 'Prefer Perceived Exertion',
            'Perceived Relative Effort', 'Commute.1',
            'Total Weight Lifted', 'From Upload',
            'Grade Adjusted Distance', 'Weather Observation Time',
            'Weather Condition', 'Weather Temperature',
            'Apparent Temperature', 'Dewpoint',
            'Humidity', 'Weather Pressure',
            'Wind Speed', 'Wind Gust',
            'Wind Bearing', 'Precipitation Intensity',
            'Sunrise Time', 'Sunset Time',
            'Moon Phase', 'Bike',
            'Gear', 'Precipitation Probability',
            'Precipitation Type', 'Cloud Cover',
            'Weather Visibility', 'UV Index',
            'Weather Ozone', 'Jump Count',
            'Average Flow', 'Flagged',
            'Average Elapsed Speed','Dirt Distance',
            'Newly Explored Distance','Newly Explored Dirt Distance',
            'Media', 'Max Heart Rate.1',
            'Activity Count', 'Activity Description',
            'Total Grit', 'Start Time',
            'Perceived Exertion'
            ])

        strava_df['Activity Date'] = pd.to_datetime(strava_df['Activity Date'], format=('mixed'))

        strava_df['Distance'] = pd.to_numeric(strava_df['Distance'], errors='coerce')

        strava_df.set_index('Activity ID', inplace=True)

        strava_df = strava_df.rename(columns={
            'Distance': 'Distance_km',
            'Moving Time': 'Moving Time (sec)',
            'Elapsed Time':'Elapsed Time (sec)',
            'Max Heart Rate':'Max Heart Rate (bpm)',
            'Average Heart Rate':'Average Heart Rate (bpm)'
            })

        strava_df.drop(index=1454765617, axis='index', inplace=True)
        return strava_df