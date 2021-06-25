import pandas as pd
from connection import Db


df = pd.read_csv('F:\\Riss 2021\\AGGRO\\static\\cpdata.csv')
print(df.columns)
x= df.iloc[:,:].values
print(x)
db=Db()




for i in x:
    print("---",i[0])
    print("ii1",i[1])
    print(i[2])
    print(i[3])
    print(i[4])
    print(i[5])
    if(i[4]==False):
        c="0"
    else:
        c="1"

    qry="insert into newses(title,text,subject,date,type,label)values('"+i[0].replace("'","")+"','"+i[1].replace("'","")+"','"+i[2].replace("'","")+"','"+i[3].replace("'","")+"','"+str(i[4])+"','"+c+"')"
    print(qry)
    res=db.insert(qry)

