import pandas as pd
data = pd.DataFrame(
    {
        "Nome" : ["João", "Pedro", "André", "Tiago", "Tadeu", "Judas", "Simão", "Tomé", "Bartolomeu", "Tiago", "Filipe", "Mateus"],
        "Age" : [21, 39, 46, 50, 50, 36, 51, 30, 30, 39, 44, 41],
        "Cidade": ["Éfeso", "Roma", "Pátras", "Jerusalém", "Armênia", "Jerusalém", "Armênia", "Índia", "Albanonpolis", "Ostrakine", "Hierápolis", "Etiópia"]
    }
)
data_noage = data.drop("Age", axis = 1)
print(data_noage)