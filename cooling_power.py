import pandas as pd
import numpy as np
%matplotlib notebook
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Helvetica']

df = pd.read_csv('Cooling_Power_0_10_20.txt', sep = '\t', header = None)
df.columns = [['I_0', 'I_1', 'I_still', 'I_mc']]
df['Q_mc_uW'] = (df.I_mc*1e-6)**2*100*1e6
df['Q_still_mW'] = (df.I_still*1e-6)**2*100*1e3

T_mc = [14.29, 19.07, 29.90, 43.95, 57.26, 70.62, 83.82, 96.98, 109.3, 121.7, 135.8, 150.2, 165.1,
        20.00, 22.46, 30.46, 40.43, 51.11, 62.20, 73.19, 84.26, 95.39, 106.8, 118.3, 130.2, 142.4,
        22.38, 22.57, 28.83, 37.28, 46.80, 56.41, 66.47, 76.37, 86.67, 96.91]

df['T_mc'] = pd.Series(T_mc)

plt.figure(figsize=(9,5))
for i in (1, 2):
    plt.subplot(1, 2, i)

    plt.plot(df.Q_mc_uW.values[0:13], df.T_mc.values[0:13], 'rD-', label = '0 mA', lw = 0.5)
    plt.plot(df.Q_mc_uW.values[14:26], df.T_mc.values[14:26], 'gD-', label = '10 mA', lw = 0.5)
    plt.plot(df.Q_mc_uW.values[27:], df.T_mc.values[27:], 'bD-', label = '20 mA', lw = 0.5)
    plt.axvline(900, color='k', linestyle='solid', lw = 0.5)
    plt.axhline(120, color='k', linestyle='solid', lw = 0.5)
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.xlabel(r'Q$_{\rm mc}$ (μW)', fontsize = 12)
    plt.ylabel(r'T$_{\rm mc}$ (mK)', fontsize = 12)
    plt.tight_layout(pad=2, w_pad=1, h_pad=1)
    plt.title('Cooling Power Test', fontsize= 12)
    legend = plt.legend(loc='upper left', frameon=False)
    for label in legend.get_texts():
        label.set_fontsize(10)

    for label in legend.get_lines():
        label.set_linewidth(1)  

    if i == 2:
        plt.xscale('log')
        plt.yscale('log')
plt.savefig('_color_raw.pdf', dpi = 300,  transparent=True)
