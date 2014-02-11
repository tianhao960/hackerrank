# -*- coding: utf-8 -*-


from sklearn import linear_model

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
  rows.append(feature)
  ys.append(float(data[-1]))

regr = linear_model.RidgeCV(alphas=[0.1,1.0,10.0])

regr.fit(rows, ys)

print regr.alpha_
print regr.coef_
print regr.intercept_

predictNum = int(raw_input())
rowindex=0
rows=[]
while rowindex<predictNum:
  rowindex = rowindex+1;
  data =raw_input().split()
  feature = [float(data[0]),float(data[1])]
  rows.append(feature)  

for value in regr.predict(rows):
    print value
