# -* - coding:UTF-8 -*-                     #中文编码
p=mdb.models['Model-1'].parts['Part-1']     #指定part对象
f1=p.elementFaces[1]                        #指定零件上某单元面
highlight(f1)                               #高亮显示该单元面
#unhighlight(f1)                             #取消高亮显示
