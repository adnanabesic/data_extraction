import pandas as pd


i=1
items = range(0, 12)
for it in items:
    df = pd.read_csv('codes/'+str(i)+'.csv')
    # df['Code'].to_excel(str(i) + '.ods', header=False, index=False, engine='odf')
    df['Code'].to_excel('vouchers/'+ str(i) + '.xlsx', header=False, index=False, engine='xlsxwriter')
    i = i+1


