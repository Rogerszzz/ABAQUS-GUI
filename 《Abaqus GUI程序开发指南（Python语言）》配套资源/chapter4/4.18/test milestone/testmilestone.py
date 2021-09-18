p=mdb.models['Model-1'].parts['Part-1']
e=p.elements
N=len(e)
k=0
for e1 in e:
    print e1.label
    k=k+1
    milestone('已完成打印百分比为',100*k/N)