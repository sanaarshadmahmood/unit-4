# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:40:01 2023

@author: SANA
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
bcs = pd.read_csv('BCS_ann.csv')
bp = pd.read_csv('BP_ann.csv')
tsco = pd.read_csv('TSCO_ann.csv')
vod = pd.read_csv("VOD_ann.csv")
plt.figure()




plt.subplot(2,2,1)




plt.hist(bcs["ann_return"],label="barclays")
plt.legend()
plt.xlabel("return (%)")
plt.ylabel("N")



plt.subplot(2,2,2)
plt.hist(bp['ann_return'],label="bp")
plt.legend()
plt.xlabel("return (%)")
plt.ylabel("N")



plt.subplot(2,2,3)
plt.hist(tsco['ann_return'], label="tesco")
plt.legend()



plt.subplot(2,2,4)
plt.hist(vod['ann_return'], label="vodaphone")
plt.legend()
plt.xlabel("return (%)")
plt.ylabel("N")
plt.show()

plt.figure()
plt.hist(tsco["ann_return"], label="tesco",alpha=0.7 ,density=True)
plt.hist(vod["ann_return"], label="vodaphone",alpha=0.7, density=True)

plt.legend()

plt.xlabel("return (%)")
plt.ylabel("N")
plt.show()






