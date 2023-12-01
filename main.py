import  pandas as  pd
import  pymysql
import time
from operator import itemgetter
import numpy as np
start=time.time()
import sqlalchemy
from sqlalchemy import create_engine
parse=(0.2,0.5,0.2,0.1)
db=pymysql.connect(host="127.0.0.1",user="root",password="111111",port=3306,db="test",charset='utf8')
cursor=db.cursor()
sql='''select * from global where TS="Catering industry"'''
sql_2='''select SUM(TSR),SUM(WT),SUM(TF),SUM(AP)  from global where TS="Catering industry"'''
cursor.execute(sql_2)
weight=cursor.fetchall()
res=cursor.execute(sql)
list=cursor.fetchall()
#df1=pd.DataFrame(list)
#print(weight)
for a in weight:
    TSRA=a[0]
    WTRA=float(a[1])
    TFA=a[2]
    APA=a[3]
#print(parse[0])
#print(type(WTRA))
#print(list)
#print(TSRA,WTRA,TFA,APA)
#print(res)
#df=pd.read_sql(sql,db)
#print(df)
my_list = []  # 先创建一个主列表
for value in list:
    #print(type(value[2]),value[1])
    #write=pymysql.connect(host="127.0.0.1",user="root",password="111111",port=3306,db="test",charset='utf8')
    #wcursor=write.cursor()
    ji=(value[3]/float(TSRA)*parse[0])+(float(value[4])/WTRA*parse[1])+(float(value[5])/TFA*parse[2])+(float(value[6])/APA*parse[3])
    ji_1=(value[3])
    #writeSql="Insert INTO info(TS,AN,BN,TSR,WT,TF,AP,ALL)VALUES ('%s','%s','%s','%f','%f','%f','%f','%f')" %\
             #ab=[value[0],value[1],value[2],value[3],float(value[4]),float(value[5]),float(value[6]),float(ji)]

    #print(writeSql)
    #for i in range(res):  # 循环遍历6次，依次为主列表的每个元素创建新的列表
        #j = []  # 先创建新列表并添加入主列表中
    #my_list.append(j)
    #for m in range(1, 7):
    li=[value[0],value[1],value[2],value[3],float(value[4]),float(value[5]),float(value[6]),float(ji)]
    my_list.append(li)  # 为子列表添加元素

m=sorted(my_list,key=itemgetter(7))
print(m)  # 输出
"""
    try:
        wcursor.execute(writeSql)
        write.commit()
    except:
        write.rollback()
    #db.close()
    #write.close()
"""

end=time.time()
print("运行耗时",end-start)

#mysql_engine = create_engine("mysql+mysqlconnector://root:111111@127.0.0.1:3306/test")

#mysql_delays_df3 = pd.read_sql(sql, con=mysql_engine)