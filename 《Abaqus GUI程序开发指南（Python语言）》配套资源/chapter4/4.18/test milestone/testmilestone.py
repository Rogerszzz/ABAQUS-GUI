p=mdb.models['Model-1'].parts['Part-1']
e=p.elements
N=len(e)
k=0
for e1 in e:
    print e1.label
    k=k+1
    milestone('����ɴ�ӡ�ٷֱ�Ϊ',100*k/N)