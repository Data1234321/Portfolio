import pandas as pd
import argparse
import logging
from cleansing import cleansing_steps
from analysis.analysis import StravaAnalysis


########################################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

########################################
########################################
########################################

def run(data):
    """
    Function to run all steps in analysis
    """

    # Cleanse the data
    tom_strava = cleansing_steps(data)
    tom_s = tom_strava.cleanse()

    if args.all == True or args.correlation == True:
        correlations = strava_analysis(tom_s)
        corr_heatmap = correlations.correlations()
        exit()


########################################
########################################
########################################


if __name__=="__main__":

    tom_strava_data = pd.read_csv('/workspaces/Portfolio/Strava/tom_strava_activities.csv')

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all analysis'
    )

    parser.add_argument(
        '--correlation',
        action='store_true',
        help='Run only correlation analysis'
    )

    args = parser.parse_args()

    logger.info(f"Args called: {args}")


    ########################################
    ########################################
    ########################################

    run(tom_strava_data)
