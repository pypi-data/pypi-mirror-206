import numpy as np
import pandas as pd
import inspect
from scipy.optimize import curve_fit
from .util import arg_to_list

def get_model(model_type=''):
    if model_type == 'monoexp_decay':
        def model(x, a, b):
            return a*np.exp(-b*x, dtype='float64')
    elif model_type == 'biexp_decay':
        def model(x, a, b, c, d):
            return a*np.exp(-b*x, dtype='float64') + c*np.exp(-d*x, dtype='float64')
    elif model_type == 'monoexp_decay_offset':
        def model(x, a, b, c):
            return a*np.exp(-b*x) + c
    return model

def make_fit(df_in, x:str, y:str, model, groupby:str='Group', p0=None):
    fit_results = dict()
    for name, data in df_in.groupby(groupby, sort=False):
        try:
            popt,_ = curve_fit(model, data[x], data[y], p0=p0)
            fit_results[name] = popt
        except:
            print(f'Fit for dataset {name} failed')
    return fit_results

def get_rates(fit_results, model, dt=1):
    dt = arg_to_list(dt)
    rates = pd.DataFrame(columns=['Group', 'Rate type', 'Rate', 'Population'])
    i=0
    for j, grp in enumerate(fit_results.keys()):
        popt = fit_results[grp]
        dt_grp = dt[j] if len(dt) > 1 else dt[0]
        if len(inspect.getfullargspec(model).args) == 3:
            rates.loc[i] = {'Group':grp, 'Rate type':1, 'Rate':popt[1]/dt_grp, 'Population':1}
            i+=1
        elif len(inspect.getfullargspec(model).args) == 5:
            rates.loc[i] = {'Group':grp, 'Rate type':'Fast', 'Rate':popt[1]/dt_grp, 'Population':popt[0]/(popt[0]+popt[2])}
            i+=1
            rates.loc[i] = {'Group':grp, 'Rate type':'Slow', 'Rate':popt[3]/dt_grp, 'Population':popt[2]/(popt[0]+popt[2])}
            i+=1
    rates = rates.astype({'Group':'category', 'Rate type':'category', 'Rate':'float64', 'Population':'float64'})
    return rates