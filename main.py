#This is a file created for a training
import streamlit as st
import pandas as pd
import numpy as np

def point_treatment(dfp, fname) :
    dfp["str"]=1
    dfp.loc[dfp["str"].isna(), "str"]=0
    column_names = ["str", "Northing", "Easting", "Elevation", "Point Name", 1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
    dfp = dfp[column_names]

    res=[]

    first_line=[]
    fdate=dfp[4].values[0]
    for i in range(len(column_names)) :
        if i == 0 :
            first_line.append(fname)
        elif i == 1 :
            first_line.append(fdate)
        else :
            first_line.append("")
    res.append(first_line)


    second_line=[0 if i < 4 else "" for i in range(len(column_names))]
    res.append(second_line)


    for i in range(len(dfp)) :
        row=list(dfp.iloc[i].values)
        res.append(row)
        res.append([0 if i < 4 else "" for i in range(len(column_names))])

    res.append([0 if i < 4 else "" for i in range(len(column_names))])
    res[-1][4]="END"

    return pd.DataFrame(res)


def line_treatment(dfl, fname) :
    dict_str = {"HA":1, "LR":2, "LJ":3, "LT":4, "S_Fo":5, "S_Mo":6, "S_fa":7, "BDR":8}
    dfl["str"]=dfl["Point Code"].map(dict_str)

    dfl.loc[dfl["str"].isna(), "str"]=0
    column_names = ["str", "Northing", "Easting", "Elevation", "Point Name", 1, 2, 4, "Point Code"]
    dfl = dfl[column_names]

    res=[]

    first_line=[]
    fdate=dfl[2].values[0]
    for i in range(len(column_names)) :
        if i == 0 :
            first_line.append(fname)
        elif i == 1 :
            first_line.append(fdate)
        else :
            first_line.append("")
    res.append(first_line)


    second_line=[0 if i < 4 else "" for i in range(len(column_names))]
    res.append(second_line)

    point_code = None
    for i in range(len(dfl)) :
        row=list(dfl.iloc[i].values)
        if (row[-1] != point_code) & (point_code != None) :
            res.append([0 if i < 4 else "" for i in range(len(column_names))])
        res.append(row)
        point_code = row[-1]

    res.append([0 if i < 4 else "" for i in range(len(column_names))])
    res.append([0 if i < 4 else "" for i in range(len(column_names))])
    res[-1][4]="END"

    return pd.DataFrame(res)


"# Convert PDF GPS Data"
file_up = st.file_uploader("Upload your .csv here", type=["CSV"])

if file_up :
    fname=file_up.name
    df = pd.read_csv(file_up, sep=";")

    residual = df[df.columns[-1]].str.split(',',expand=True)
    df = df[df.columns[:-2]]
    df = pd.concat([df, residual], axis=1)
    df_line, df_point = df[df["Point Name"].str.startswith("Line")], df[~df["Point Name"].str.startswith("Line")]

    def convert_df(df):
        return df.to_csv(index=False, header=False).encode('utf-8')

    c1, c2 = st.columns(2)
    if not df_point.empty :
        df_point_clean = point_treatment(df_point, fname)
        c1.download_button("Download point file", convert_df(df_point_clean), f"p{fname}.csv", "text/csv", key='download-csv-point', use_container_width=True)

    if not df_line.empty :
        df_line_clean = line_treatment(df_line, fname)
        c2.download_button("Download line file", convert_df(df_line_clean), f"l{fname}.csv", "text/csv", key='download-csv-line', use_container_width=True)