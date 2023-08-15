import pandas as pd
data = pd.DataFrame(
    {
        "Name" :[None, "Félix", "Policarpo", "Irineu", "Inácio"],
        "City" :["Berlim", None, "Bruxelas", "Efésio", None]
    }
)
print("DataFrame com NaN:", data)
no_value_name = data["Name"].isna()
data["Name"].fillna("Carlos", inplace = True)
data["City"].fillna("Corinto", inplace = True)
print("DataFrame sem NaN:", data)