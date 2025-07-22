import csv
import pandas as pd

mountains = {} # director gol in care vom salva muntii

with open("IntroToPy/mountains_db.tsv", "r", encoding="utf-8") as file: # deschidem fisierul in modul citire
    for line in file:
        parts = line.split("\t") # impartim linia in parti folosind tab ("\t") ca separator
        nume_munte = parts[0]
        altitudine = parts[1]
        tara = parts[2]
        cod_iso = parts[3]

        mountains[nume_munte] = { # un dictionar pentru fiecare munte (seamana cu un obiect / structura de date)
            "altitudine": altitudine,
            "țară": tara,
            "cod_iso": cod_iso
        }


tari_unice = set() # structura care pastreaza doar valori unice

for info in mountains.values(): # trecem prin valorile dictionarului mountains
    tari_unice.add(info["țară"]) # adaugam tara in set
print("Număr de țări distincte:", len(tari_unice))


alt = 0 # numar de munti cu altitudine NULL

for nume, info in mountains.items():
    if info["altitudine"] == "NULL":
        alt = alt + 1
print("Munti fara altitudine:", alt)


altitudini = [
    float(info["altitudine"]) # convertim altitudinea in float
    for info in mountains.values()
    if info["altitudine"] != "NULL" # ignoram muntii cu altitudine NULL
]

alt_series = pd.Series({
    name: float(info["altitudine"])
    for name, info in mountains.items()
    if info["altitudine"] != "NULL"
})


print("🟢 Altitudine minimă:", alt_series.min())
print("🔵 Altitudine maximă:", alt_series.max())
print("🟠 Media altitudinilor:", round(alt_series.mean(), 2))
print("🟡 Mediana:", alt_series.median())
print("🔴 Standard deviation:", round(alt_series.std(), 2))


topN = 10

top = alt_series.sort_values(ascending=False).head(topN)
print(top)




df = pd.DataFrame([
    {"Munte": name,
     "Altitudine": info["altitudine"],
     "Tara": info["țară"],
     "Cod_ISO": info["cod_iso"]}
    for name, info in mountains.items()
    if info["altitudine"] is not None
])

# 🛠️ Conversie în numeric pentru coloana Altitudine
df["Altitudine"] = pd.to_numeric(df["Altitudine"], errors="coerce")




import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Cod_ISO", order=df["Cod_ISO"].value_counts().index)
plt.title("Număr de munți pe țară (cod ISO)")
plt.xlabel("Cod ISO")
plt.ylabel("Număr munți")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


max_alt_by_country = df.groupby("Tara")["Altitudine"].max().sort_values()
plt.figure(figsize=(12, 6))
max_alt_by_country.plot(kind="barh", color="teal")
plt.title("Altitudine maximă a munților pe țară")
plt.xlabel("Altitudine (m)")
plt.tight_layout()
plt.show()




plt.figure(figsize=(8, 6))
sns.boxplot(x=df["Altitudine"], color="skyblue")
plt.title("Distribuția globală a altitudinilor")
plt.xlabel("Altitudine (m)")
plt.tight_layout()
plt.show()



fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

country_stats = df.groupby("Tara")["Altitudine"].agg(["min", "median", "max"])
country_stats.plot(ax=ax[0], kind="bar", colormap="tab10")
ax[0].set_title("Altitudine minimă, mediană și maximă pe țară")
ax[0].set_ylabel("Altitudine (m)")
ax[0].legend(loc="upper right")
ax[0].tick_params(axis='x', rotation=45)

sns.boxplot(data=df, x="Tara", y="Altitudine", ax=ax[1], palette="coolwarm")
ax[1].set_title("Distribuția altitudinilor pe țări")
ax[1].set_xlabel("Țară")
ax[1].set_ylabel("Altitudine (m)")
ax[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

