import pandas as pd
from cleansing import cleansing_steps
from analysis import strava_analysis


#######

def run(data):
    """
    Function to run all steps in analysis
    """

    # Cleanse the data
    tom_strava = cleansing_steps(data)
    tom_s = tom_strava.cleanse()

    correlations = strava_analysis(tom_s)
    corr_heatmap = correlations.correlations()
    


if __name__=="__main__":
    tom_strava_data = pd.read_csv('/workspaces/Portfolio/Strava/Tom Strava activities (1).csv')
    
    run(tom_strava_data)
