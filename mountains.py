import csv
import pandas as pd
df = pd.read_csv('IntroToPy/mountains_db.tsv',sep='\t',header=None,names=['Munte', 'Altitudine', 'Tara', 'Cod_ISO'])
print(df) 

mountains = {}

""" with open("IntroToPy/mountains_db.tsv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")
    for row in reader:
        key = row["Munte"]  # înlocuiește cu numele exact al coloanei
        mountains[key] = row  # toată linia devine valoarea """

mountains = {}

with open("IntroToPy/mountains_db.tsv", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t")
        nume_munte = parts[0]
        altitudine = parts[1]
        tara = parts[2]
        cod_iso = parts[3]

        mountains[nume_munte] = {
            "altitudine": altitudine,
            "țară": tara,
            "cod_iso": cod_iso
        }

tari_unice = set() #set() pastreaza doar valori unice

for info in mountains.values():
    tari_unice.add(info["țară"])

print("Număr de țări distincte:", len(tari_unice))

alt = 0

for nume, info in mountains.items():
    if info["altitudine"] == "NULL":
        alt = alt + 1

print("Munti fara altitudine:", alt)



df_filtered = df[df["Altitudine"].notna()]
print(df_filtered)


print(df["Altitudine"].notna())

print("🟢 Altitudine minimă:", df["Altitudine"].min())
print("🔵 Altitudine maximă:", df["Altitudine"].max())
print("🟠 Media altitudinilor:", round(df["Altitudine"].mean(), 2))
print("🟡 Mediana:", df["Altitudine"].median())
print("🔴 Standard deviation:", round(df["Altitudine"].std(), 2))


topN = 10

df_top = df_filtered.sort_values(by="Altitudine", ascending=False).head(topN)
print(df_top)
