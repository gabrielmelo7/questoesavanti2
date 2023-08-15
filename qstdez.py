import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame(
    {
        "Name" : ["João", "Pedro", "André", "Tiago", "Tadeu", "Judas", "Simão", "Tomé", "Bartolomeu", "Tiago", "Filipe", "Mateus"],
        "Age" : [21, 39, 46, 50, 50, 22, 51, 48, 52, 39, 23, 19],
        "City": ["Éfeso", "Roma", "Pátras", "Jerusalém", "Armênia", "Jerusalém", "Armênia", "Índia", "Albanonpolis", "Ostrakine", "Hierápolis", "Etiópia"]
    }
)
fig, ax = plt.subplots(figsize = (8, 5))
ax = plt.scatter(data["Name"], data["Age"])
plt.suptitle("Gráfico original")
plt.show()
data_noout = data[data["Age"] > 30]
ax = plt.scatter(data_noout["Name"], data_noout["Age"])
plt.suptitle("Gráfico sem outliers")
plt.show()