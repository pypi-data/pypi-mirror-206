import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
    
def fit_ensemble_fluo_decay(df, ax=None):
    def model(x, a, b, c):
        return a*np.exp(-b*x) + c
    fit_df = pd.DataFrame(columns=['x','Fit','Group'])
    label_ypos = 0.82 - 0.07*len(df.Group.unique())
    for grp, data in df.groupby('Group', sort=False):
        popt,_ = curve_fit(model, data.Laser_time, data.MeanIntensity, p0=[data.MeanIntensity.iloc[0], 1, 0])
        x_model = np.linspace(data.Laser_time.iloc[0], data.Laser_time.iloc[-1], 300)
        df = pd.DataFrame({'x':x_model, 'Fit':model(x_model, *popt), 'Group':grp})
        fit_df = pd.concat([fit_df, df], axis=0)
        plt.text(0.5, label_ypos, f'Rate ({grp}) = {popt[1]:.3f} s\N{SUPERSCRIPT MINUS}\N{SUPERSCRIPT ONE}', transform=ax.transAxes)
        label_ypos += 0.07
    sns.lineplot(data=fit_df, x='x', y='Fit', hue='Group', hue_order=fit_df.Group.unique(), legend=False, ax=ax, linestyle='dashed')