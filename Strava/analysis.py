"""
Docstrings for analysis steps
"""

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

########

class strava_analysis:
    def __init__(self, data):
        self.data = data

    def correlations(self):
        """
        Returns an interactive correlation heatplot in new window
        """
        data = pd.DataFrame(self.data)

        stacked_data = data.corr(method='pearson', numeric_only=True).round(3).unstack().sort_values(ascending=False)
        so_df = pd.DataFrame(stacked_data).reset_index().rename(columns={0:'Correlation',
                                                               'level_0': 'Variable 0',
                                                               'level_1': 'Variable 1'
                                                               })
        
        # Find the highest correlated variables
        correlated_df = so_df[so_df['Correlation'] < 1].reset_index(drop=True)
        
        corr_ten = correlated_df.loc[:20]

        corr_ten['pair'] = corr_ten.apply(lambda row: tuple(sorted([row['Variable 0'], row['Variable 1']])), axis=1)

        corr_ten_filtered = corr_ten.drop_duplicates(subset=['pair']).drop(columns=['pair']).reset_index(drop=True)
        print(corr_ten_filtered)
        
        
        # Create a heatmap visualisation of correlations
        fig = px.imshow(data.corr(numeric_only=True).round(2), 
                        text_auto=True,
                        aspect='auto',
                        color_continuous_scale='viridis'
                        )
        
        fig.update_xaxes(side='top')
        return fig.show();
