import pandas as pd
data = pd.DataFrame(
    {
        "Name" : ["João", "Pedro", "André", "Tiago", "Tadeu", "Judas", "Simão", "Tomé", "Bartolomeu", "Tiago", "Filipe", "Mateus"],
        "Age" : [21, 39, 46, 50, 50, 36, 51, 30, 30, 39, 44, 41],
        "City": ["Éfeso", "Roma", "Pátras", "Jerusalém", "Armênia", "Jerusalém", "Armênia", "Índia", "Albanonpolis", "Ostrakine", "Hierápolis", "Etiópia"]
    }
)
names_mfor = data.loc[data["Age"] >= 40, "Name"]
print("Aqueles que tem 40 ou mais anos são:")
for name in names_mfor:
    age_mfor = data.loc[data["Name"] == name, "Age"].iloc[0]
    city_mfor = data.loc[data["Name"] == name, "City"].iloc[0]
    print(f"{name} que tem {age_mfor} anos, de {city_mfor}")
