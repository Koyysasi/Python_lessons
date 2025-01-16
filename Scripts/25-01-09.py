import pandas as pd
import numpy as n

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def read_data():
	library = pd.read_csv("library.csv")
	print(library.head(5))
	print("--------------------------------------------------")
	library = library.drop(["Edition Statement", "Corporate Contributors", "Corporate Author", "Contributors", "Former owner", "Engraver", "Issuance type"], axis=1)
	print(library.head(5))
	print("--------------------------------------------------")
	library.drop(columns=["Shelfmarks"])
	print(library.head(5))

#read_data()

def index_data():
	library = pd.read_csv("library.csv")
	print(library["Identifier"].is_unique)
	library.set_index("Identifier")
	print(library.head(5))

#index_data()


def row_data(index):
	library = pd.read_csv("library.csv")
	library.set_index("Identifier")
	print(library.loc[index])

#row_data(206)

def row_data2(index):
	library = pd.read_csv("library.csv")
	library.set_index("Identifier")
	print(library.iloc[index])

#row_data2(207)

def clean_date():
	library = pd.read_csv("library.csv")
	library = library.drop (
		[ "Edition Statement" , "Corporate Contributors" , "Corporate Author" , "Contributors" , "Former owner" ,
		  "Engraver" , "Issuance type" ] , axis=1 )
	london = library[ 'Place of Publication' ].str.contains ( 'London' )
	oxford = library[ 'Place of Publication' ].str.contains ( 'Oxford' )
	plymouth = library[ 'Place of Publication' ].str.contains ( 'Plymouth' )
	library['Place of Publication'] = n.where(london, "London",
									  n.where(oxford, "Oxford",
									  n.where(plymouth, "Plymouth", library['Place of Publication'].str.replace('-', ' '))))

#clean_date()

def clean_date():
	library = pd.read_csv("library.csv")
	library = library.set_index("Identifier")
	print(library.loc[1982:, "Date of Publication"].head(20))
	extr = library['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
	library['Date of Publication'] = pd.to_numeric(extr)
	print("------------------------")
	print(library["Date of Publication"].head(20))
	print(library['Date of Publication'].isnull().sum() / len(library))
	avg = round(library['Date of Publication'].mean())
	library['Date of Publication'] = library['Date of Publication'].fillna(avg)
	print("---------------------------------------")
	print(library['Date of Publication'].head(20))

#clean_date()

def specific_book():
	library = pd.read_csv("library.csv")
	library = library.set_index("Identifier")
	find = library.loc[library['Date of Publication'] == "1899"]
	find2 = find.loc[library['Place of Publication'] == "London"]
	print(len(find2))
	print(find2["Title"])

specific_book()