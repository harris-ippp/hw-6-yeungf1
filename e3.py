import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_election = []
for i in range(1924,2020,4):
    header = pd.read_csv("president_general_{}.csv".format(i), nrows = 5).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_{}.csv".format(i), index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = i
    df_election.append(df.loc[:,["Democratic","Republican","Total Votes Cast","Year"]])

df = pd.concat(df_election)

df["Republican Share"]=df["Republican"]/df["Total Votes Cast"]

#Accomack county:
AccomackCounty = df.loc['Accomack County'].sort_values(by = 'Year', ascending = True)
figure1 = AccomackCounty.plot(x ="Year", y="Republican Share")
plt.title("Republican Vote Share of Accomack County")
figure1.get_figure().savefig('accomack_county.pdf')

#Albemarle County
AlbemarleCounty = df.loc['Albemarle County'].sort_values(by = 'Year', ascending = True)
figure2 = AlbemarleCounty.plot(x ="Year", y="Republican Share")
plt.title("Republican Vote Share of Albemarle County")
figure2.get_figure().savefig('albemarle_county.pdf')

#Alexandria City
AlexandriaCity = df.loc['Alexandria City'].sort_values(by = 'Year', ascending = True)
figure3 = AlexandriaCity.plot(x ="Year", y="Republican Share")
plt.title("Republican Vote Share of Alexandria City")
figure3.get_figure().savefig('alexandra_city.pdf')

#Alleghany County
AlleghanyCounty = df.loc['Alleghany County'].sort_values(by = 'Year', ascending = True)
figure4 = AlleghanyCounty.plot(x ="Year", y="Republican Share")
plt.title("Republican Vote Share of Alleghany County")
figure4.get_figure().savefig('alleghany_county.pdf')
