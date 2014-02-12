# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import RidgeCV

MN=raw_input()
MN = MN.split()
F= int(MN[0])
N = int(MN[1])

rowindex=0
rows=[]
ys=[]
while rowindex<N:
  rowindex = rowindex+1;
  data =raw_input().split()
  feature = [float(data[0]),float(data[1])]
  #print np.vander(feature,5).flatten()
  rows.append(np.vander(feature,5).flatten())
  ys.append(float(data[-1]))

#print rows
ridge = RidgeCV(alphas=[0.1,1.0,10.0])
ridge.fit(rows,ys)

print ridge.alpha_
print ridge.coef_
print ridge.intercept_


predictNum = int(raw_input())
rowindex=0
rows=[]
while rowindex<predictNum:
  rowindex = rowindex+1;
  data =raw_input().split()
  feature = [float(data[0]),float(data[1])]
  rows.append(np.vander(feature,5).flatten())

for value in ridge.predict(rows):
    print value
