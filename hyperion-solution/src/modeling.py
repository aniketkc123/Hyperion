# src/modeling.py
import numpy as np
from scipy.optimize import minimize, curve_fit
import matplotlib.pyplot as plt
import os
import pandas as pd

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results')
FIG_DIR = os.path.join(RESULTS_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

def model_rotation_curve(r, rho0, rs, v0):
    return v0 * (1 - np.exp(-r/rs)) + np.sqrt(rho0) * 0.1*r

def chi2(params, r, v, v_err):
    rho0, rs, v0 = params
    model_v = model_rotation_curve(r, rho0, rs, v0)
    return np.sum(((v - model_v)/v_err)**2)

def fit_dark_matter_density(df):
    r = df['r'].to_numpy()
    v = df['v'].to_numpy()
    v_err = df.get('v_err', pd.Series(np.ones_like(v)*0.1)).to_numpy()

    p0 = [0.1, 5.0, np.median(v)]
    res = minimize(chi2, p0, args=(r, v, v_err), method='Powell')
    params = res.x
    return params, None

def pulse_model(t, A, t0, tau_r, tau_d):
    return A * np.exp(-((t - t0)/tau_d) - (tau_r/(t - t0 + 1e-9)))

def analyze_lightcurve(df):
    t = df['time'].to_numpy()
    f = df['flux'].to_numpy()

    from scipy.signal import savgol_filter, find_peaks
    f_smooth = savgol_filter(f, window_length=21 if len(f)>21 else 5, polyorder=2)
    peaks, _ = find_peaks(f_smooth, height=np.mean(f_smooth) + 2*np.std(f_smooth))
    print(f"Detected peaks at indices: {peaks}")

    if len(peaks) > 0:
        pidx = peaks[0]
        t_win = (t > t[pidx] - 5) & (t < t[pidx] + 20)
        try:
            popt, pcov = curve_fit(pulse_model, t[t_win], f[t_win], p0=[f[pidx], t[pidx], 1.0, 5.0], maxfev=10000)
            plt.figure()
            plt.plot(t, f, label='flux')
            plt.plot(t, f_smooth, label='smooth')
            plt.plot(t[t_win], pulse_model(t[t_win], *popt), label='fit')
            plt.legend()
            plt.savefig(os.path.join(FIG_DIR, 'lightcurve_peak_fit.png'))
            plt.close()
            print("Pulse fit parameters:", popt)
        except Exception as e:
            print("pulse fit failed:", e)
