#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:20:22 2022

@author: danycajas
"""

import numpy as np
import pandas as pd
import yfinance as yf
import warnings

warnings.filterwarnings("ignore")
pd.options.display.float_format = '{:.4%}'.format


#%%
assets = ["JCI", "TGT", "CMCSA", "CPB", "MO", "NBL", "APA", "MMC", "JPM", "ZION"]

data = pd.read_csv("stock_prices.csv", parse_dates=True, index_col=0)
Y = data[assets].pct_change().dropna().iloc[-200:]

w_2 = pd.read_csv("HC_NCO.csv", parse_dates=False, index_col=0)


#%%
import riskfolio as rp
import mosek

port = rp.HCPortfolio(returns=Y)

model = "NCO"
codependence = "pearson"
covariance = "hist"
obj = "MinRisk"
rf = 0
linkage = "ward"
max_k = 10
leaf_order = True

rms = [
    "MV",
    "MAD",
    "MSV",
    "FLPM",
    "SLPM",
    "CVaR",
    "EVaR",
    "WR",
    "MDD",
    "ADD",
    "CDaR",
    "EDaR",
    "UCI",
]

w_1 = pd.DataFrame([])

for i in rms:
    w = port.optimization(
        model=model,
        codependence=codependence,
        covariance=covariance,
        obj=obj,
        rm=i,
        rf=rf,
        linkage=linkage,
        max_k=max_k,
        leaf_order=leaf_order,
    )

    w_1 = pd.concat([w_1, w], axis=1)

w_1.columns = rms

a = np.testing.assert_array_almost_equal(w_1.to_numpy(), w_2.to_numpy(), decimal=6)
if a is None:
    print("There are no errors in test_hc_nco_optimization")


#%%
# import matplotlib.pyplot as plt
# rm = "GMD"

# for rm in rms:
#     # lala = rp.Risk_Contribution(w_1[rm].to_frame(),
#     #                             cov=Y.cov(),
#     #                             returns=Y,
#     #                             rm=rm,
#     #                             rf=0,
#     #                             alpha=0.05,
#     #                             a_sim=100,
#     #                             beta=None,
#     #                             b_sim=None)
#     # print(lala)
#     ax = rp.plot_risk_con(w_1[rm].to_frame(),
#                           cov=Y.cov(),
#                           returns=Y,
#                           rm=rm,
#                           rf=0,
#                           alpha=0.05,
#                           color="tab:red",
#                           height=6,
#                           width=10,
#                           ax=None)
#     plt.show()


import riskfolio as rp

rm = "MV"

ax = rp.plot_risk_con(w_1[rm].to_frame(),
                      cov=Y.cov(),
                      returns=Y,
                      rm=rm,
                      rf=0,
                      alpha=0.05,
                      percentage=False,
                      color="tab:red",
                      height=6,
                      width=10,
                      ax=None)