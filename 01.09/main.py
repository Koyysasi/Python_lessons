import pandas as pd
import numpy as np

def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

def read_data():
    library = pd.read_csv("libary.csv")
    print(library.head(5))
    print("======================================================================")
    library = library.drop(
            ["Edition Statement", "Corporate Contributors", "Corporate Author", "Contributors", "Former owner",
            "Engraver", "Issuance type"], axis=1)
    print(library.head(5))
    print("======================================================================")
    library = library.drop(columns=["Shelfmarks"])
    print(library.head(5))



def Data_reindex():
    print("======================================================================")
    library = pd.read_csv("libary.csv")
    print(library["Identifier"].is_unique)
    library = library.set_index("Identifier")
    print(library.head(5))


def row_data(index):
    print("======================================================================")
    library = pd.read_csv("libary.csv")
    library = library.set_index("Identifier")
    print(library.loc[index])

def row_data2(index):
    print("======================================================================")
    library = pd.read_csv("libary.csv")
    library = library.set_index("Identifier")
    print(library.iloc[index])


def clean_data():
    print("======================================================================")
    library = pd.read_csv("libary.csv")
    library = library.set_index("Identifier")
    print(library['Place of Publication'].head(10))
    london = library['Place of Publication'].str.contains('London')
    oxford = library['Place of Publication'].str.contains('Oxford')
    plymouth = library['Place of Publication'].str.contains('Plymouth')
    library["Place of Publication"] = np.where(london, "London", np.where(oxford, "Oxford", np.where(plymouth, "Plymouth", library["Place of Publication"].str.replace('-', ' '))))




def clean_place():
    print("======================================================================")
    library = pd.read_csv("libary.csv")
    library = library.set_index("Identifier")
    print(library.loc[1982:, 'Date of Publication'].head(20))
    print("======================================================================")
    extr = library['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    library['Date of Publication'] = pd.to_numeric(extr)
    print(library['Date of Publication'].isnull().sum() / len(library))
    avg = round(library['Date of Publication'].mean())

    library['Date of Publication'] = library['Date of Publication'].fillna(avg)
    print(library['Date of Publication'].head(20))




def specific_book():
    print("======================================================================")
    library = pd.read_csv("libary.csv")
    library = library.set_index("Identifier")
    find = library.loc[library["Date of Publication"] == "1892"]
    find2 = library.loc[library["Date of Publication"] == "London"]
    print(len(find2))
    print(find["Title"])



def rename_columns():
    olympics = pd.read_csv("olympics.csv", header=1)
    print(olympics.head(10))
    olympics.rename(columns={'Unnamed: 0': 'Country',
                             '? Summer': 'Summer Olympics',
                             '01 !': 'S_Gold',
                             '02 !': 'S_Silver',
                             '03 !': 'S_Bronze',
                             'Total': 'S_Total',
                             '? Winter': 'Winter Olympics',
                             '01 !.1': 'W_Gold',
                             '02 !.1': 'W_Silver',
                             '03 !.1': 'W_Bronze',
                             'Total.1': 'W_Total',
                             '? Games': '# Games',
                             '01 !.2': '#Gold',
                             '02 !.2': '#Silver',
                             '03 !.2': '#Bronze'}, inplace=True)
    print(olympics.head(10))
rename_columns()


if __name__ == "__main__":
    main()
    specific_book()