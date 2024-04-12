#This is a file created for a training
import streamlit as st
import pandas as pd
import numpy as np


# def point_treatment(dfp, fname) :
# 	dfp["str"]=1
# 	dfp.loc[dfp["str"].isna(), "str"]=0
# 	cn = ["str", "Northing", "Easting", "Elevation", "Point Name", 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 	column_names = [ x for x in cn if x in dfp ]
# 	dfp = dfp[column_names]
	
# 	res=[]
# 	first_line=[]
# 	fdate=dfp[4].values[0]
# 	for i in range(len(column_names)) :
#         if i == 0 :
#             first_line.append(fname)
#         elif i == 1 :
#             first_line.append(fdate)
#         else :
#             first_line.append("")
#     res.append(first_line)


#     second_line=[0 if i < 4 else "" for i in range(len(column_names))]
#     res.append(second_line)


#     for i in range(len(dfp)) :
#         row=list(dfp.iloc[i].values)
#         res.append(row)
#         res.append([0 if i < 4 else "" for i in range(len(column_names))])

#     res.append([0 if i < 4 else "" for i in range(len(column_names))])
#     res[-1][4]="END"

#     dp = pd.DataFrame(res)    
#     for i in range(1,4) :
#         dp[i] = [ str(x).replace(",",".") if isinstance(x, str) else x for x in dp[i] ]
	
# 	return dp


def point_cleaning(dfp, fname) :
    dfp["str"]=1
    dfp.loc[dfp["str"].isna(), "str"]=0
    cn = ["str", "Northing", "Easting", "Elevation", "Point Name", 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    column_names = [ x for x in cn if x in dfp ]
    dfp = dfp[column_names]
    return dfp



def point_str_format(dfp, fname) :
    first_line=[]
    res=[]
    
    column_names=dfp.columns
    
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

    dp = pd.DataFrame(res)
    for i in range(1,4) :
        dp[i] = [ str(x).replace(",",".") if isinstance(x, str) else x for x in dp[i] ]

    return dp



# def line_treatment(dfl, fname) :
#     dict_str = {"HA":1, "LR":2, "LJ":3, "LT":4, "S_Fo":5, "S_Mo":6, "S_fa":7, "BDR":8}
#     dfl["str"]=dfl["Point Code"].map(dict_str)

#     dfl.loc[dfl["str"].isna(), "str"]=8
#     column_names = ["str", "Northing", "Easting", "Elevation", "Point Name", 1, 2, 3, 4, "Point Code"]
#     dfl = dfl[column_names]

#     res=[]

#     first_line=[]
#     fdate=dfl[2].values[0]
#     for i in range(len(column_names)) :
#         if i == 0 :
#             first_line.append(fname)
#         elif i == 1 :
#             first_line.append(fdate)
#         else :
#             first_line.append("")
#     res.append(first_line)


#     second_line=[0 if i < 4 else "" for i in range(len(column_names))]
#     res.append(second_line)

#     point_code = None
#     for i in range(len(dfl)) :
#         row=list(dfl.iloc[i].values)
#         if (row[-1] != point_code) & (point_code != None) :
#             res.append([0 if i < 4 else "" for i in range(len(column_names))])
#         res.append(row)
#         point_code = row[-1]

#     res.append([0 if i < 4 else "" for i in range(len(column_names))])
#     res.append([0 if i < 4 else "" for i in range(len(column_names))])
#     res[-1][4]="END"
#     dp = pd.DataFrame(res)
    
#     for i in range(1,4) :
#         dp[i] = [ str(x).replace(",",".") if isinstance(x, str) else x for x in dp[i] ]
    
#     return dp


def line_cleaning(dfl, fname):
    dict_str = {"HA":1, "LR":2, "LJ":3, "LT":4, "S_Fo":5, "S_Mo":6, "S_fa":7, "BDR":8}
    dfl["str"]=dfl["Point Code"].map(dict_str)

    dfl.loc[dfl["str"].isna(), "str"]=8
    column_names = ["str", "Northing", "Easting", "Elevation", "Point Name", 1, 2, 3, 4, "Point Code"]
    return dfl[column_names]


def line_str_format(dfl, fname) :
    column_names=dfl.columns
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
    dp = pd.DataFrame(res)
    
    for i in range(1,4) :
        dp[i] = [ str(x).replace(",",".") if isinstance(x, str) else x for x in dp[i] ]
    return dp



"# Convert PDF GPS Data"
tab1, tab2 = st.tabs(["User interface", "Dev"])
tab1.info("GPS input data shall always be the same format. Will not work if only lines or only points in the file.")
file_up = tab1.file_uploader("Upload your .csv here", type=["CSV"])

if file_up :
	fname=file_up.name.replace(".csv","")
	df = pd.read_csv(file_up, sep=";")
	
	with tab2.expander("input file") :
		df
	
	residual = df[df.columns[-1]].str.split(',',expand=True)
	df = df[df.columns[:-2]]
	df = pd.concat([df, residual], axis=1)
	
	list_nb = [str(x) for x in range(0,100)]
	
	col_7 = [ f"{x}.{y}" if ((x in list_nb) & (y in list_nb)) else x for x,y in zip(df[7],df[8]) ]
	df[7] = col_7
	df = df.drop(columns=[8])
	
	with tab2.expander("cleaned file") :
		df
	
	df_line, df_point = df[df["Point Name"].str.startswith("Line")], df[~df["Point Name"].str.startswith("Line")]
	
	def convert_df(df):
		return df.to_csv(index=False, header=False).encode('utf-8')
	
	c1, c2 = st.columns(2)
	dict_str_clean_pt = {}
	if not df_point.empty :
        # df_point_clean = point_treatment(df_point, fname)
        # df_point_clean
		
		df_point_clean = point_cleaning(df_point, fname)
		df_point_clean.columns = [x for x in range(len(df_point_clean.columns))]
		list_chantier, list_niv = df_point_clean[5].unique(), df_point_clean[6].unique()
		for chantier in list_chantier :
			for niv in list_niv :
				df_nc = df_point_clean[(df_point_clean[5] == chantier) & (df_point_clean[6] == niv)]
				if not df_nc.empty :
					dict_str_clean_pt[f"{chantier}_{niv}"] = {"df":point_str_format(df_nc, fname), "chantier":chantier, "niveau":niv}
		
		with tab2.expander("points str"):
			dict_str_clean_pt

		all_points = df_point_clean[[4,1,2,3,5,6,7,8,9,10,11,12,13,14]]
		all_points.columns = ["Echantillon","Y","X","Z","Chantier","Niveau","Date", "Geologie","Observation","long front","Litho", "Type alteration", "Ocurrence","Indice"]
		
		all_points = all_points[1:]
		all_points = all_points[(all_points["X"]!=0)]
		
		for i in range(1,4) :
			all_points[list(all_points.columns)[i]] = [ str(x).replace(",",".") if isinstance(x, str) else x for x in all_points[list(all_points.columns)[i]] ]
		
		with tab2.expander("all points"):
			all_points


	dict_str_clean_line = {}
	if not df_line.empty :
		df_line_clean = line_cleaning(df_line, fname)
		df_line_clean.columns = [x for x in range(len(df_line_clean.columns))]
		list_chantier, list_niv = df_line_clean[5].unique(), df_line_clean[7].unique()
		
		for chantier in list_chantier :
			for niv in list_niv :
				df_nc = df_line_clean[(df_line_clean[5] == chantier) & (df_line_clean[7] == niv)]
				if not df_nc.empty :
					dict_str_clean_line[f"{chantier}_{niv}"] = {"df":line_str_format(df_nc, fname), "chantier":chantier, "niveau":niv}
		
		with tab2.expander("lines str"):
			dict_str_clean_line
		
		all_lines=df_line_clean[[4,1,2,3,5,7,6,9]]
		all_lines.columns = ["Point Ligne", "Y", "X", "Z","Chantier","Niveau","Date","Horizon"]
		all_lines = all_lines[1:]
		all_lines = all_lines[(all_lines["X"]!=0)] # & (all_lines["X"]!=None)]
		for i in range(1,4) :
			all_lines[all_lines.columns[i]] = [ str(x).replace(",",".") if isinstance(x, str) else x for x in all_lines[list(all_lines.columns)[i]] ]

		
		with tab2.expander("all lines"):
			all_lines
	
	def convert_df(df, header=True):
		return df.to_csv(index=False, header=header).encode('ISO-8859-1')
	
	import io, zipfile
	buf = io.BytesIO()
	with zipfile.ZipFile(buf, "x") as csv_zip:
		csv_zip.writestr("POINTS.csv", convert_df(all_points))
		csv_zip.writestr("LIGNES.csv", convert_df(all_lines))
		for key in dict_str_clean_pt :
			csv_zip.writestr(f"P_{key}.str", convert_df(dict_str_clean_pt[key]["df"], header=False))
		for key in dict_str_clean_line :
			csv_zip.writestr(f"L_{key}.str", convert_df(dict_str_clean_line[key]["df"], header=False))

	st.download_button(label="Download zip", data=buf.getvalue(), file_name="CSV+STR.zip", mime="application/zip")
