from django.shortcuts import render
from django.http import HttpResponse #new

from django.template import loader
from django.shortcuts import render
import json

def index(request): #new
    import pyodbc
    import pymssql
    import warnings
    import pandas as pd
    warnings.filterwarnings('ignore')
    try:
        conn = pymssql.connect(server="192.168.1.246", user="MT_DataPro", password="MT_DataPro",
                             database="DP_All_Data_Summary")
        print("===Docking sucessfully===")
    except Exception:
        print("\nERROR: Unable to Dock to the server 20.")
        exit(-1)
    qry = " SELECT  [Sym],[Min_DT],[Max_DT] ,[BarsCnt]  ,[Sum_C] ,[DysCnt] FROM [DP_All_Data_Summary].[dbo].[DataSummary_NSE_OptM__MT] where sym like 'NI%' "
    ac_df_sql = pd.read_sql(qry, conn)
    print(ac_df_sql)

    data_clo = ac_df_sql.columns
    print(data_clo)
    json_records = ac_df_sql.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'jyoti': data,'jyoti1':data_clo}

    return render(request, 'data.html',context)


def index1(request): #new
    return HttpResponse('<h1>Django Include URLs aaaaa</h1>')