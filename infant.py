import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="shwetha",
                     db="mortality")


cur = db.cursor()

# this is the query we will be making
#query = "SELECT `drid` FROM `disease_rate` WHERE `year`=2000 LIMIT 5"
query="SELECT year,ilower,imedian,iupper FROM infant_mortality LIMIT 5 ";
# execute the query
cur.execute(query)
# retrieve the whole result set
rows= cur.fetchall()
df=pd.DataFrame([[j for j in i] for i in rows])
# create plot++++++
#print(df[1][0])

years=['2000','2001','2002','2003','2004']
lower=[df[1][0],df[1][1],df[1][2],df[1][3],df[1][4]]
median=[df[2][0],df[2][1],df[2][2],df[2][3],df[2][4]]
upper=[df[3][0],df[3][1],df[3][2],df[3][3],df[3][4]]
fig,ax = plt.subplots()
x=np.arange(len(years)) 
width=0.35
opacity = 0.4
'''plt.bar(x-width,lower,alpha=opacity,color='r')
plt.bar(x,median,alpha=opacity,color='b')
plt.bar(x+width,upper,alpha=opacity,color='g')


plt.xlabel('')
plt.ylabel('')
plt.title('Scores by person')

plt.legend()'''
ax = plt.subplot()
ax.bar(x-0.2, lower,width=0.2,color='b',align='center')
ax.bar(x, median,width=0.2,color='g',align='center')
ax.bar(x+0.2, upper,width=0.2,color='r',align='center')
plt.legend(('lower','median','upper'))
plt.xticks(x+width/2,(years))
plt.title('Number of death rates for infants')
plt.show()

db.close()
