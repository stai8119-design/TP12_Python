import numpy as np
noms = np.array(["Alice", "Bob", "Chloé", "David"])
notes = np.array([
    [14.5, 16.0, 13.0], 
    [11.0, 10.5, 12.5],  
    [17.0, 18.5, 16.5], 
    [9.0, 11.0, 10.0] 
])

print("Étudiants :", noms)
print("Notes :\n", notes)
print("Shape notes :", notes.shape)

moyenne_globale = np.mean(notes)
min_global = np.min(notes)
max_global = np.max(notes)
somme_globale = np.sum(notes)
ecart_type_global = np.std(notes)

print(f"Moyenne générale : {moyenne_globale:.2f}")
print(f"Minimum global : {min_global}")
print(f"Maximum global : {max_global}")
print(f"Somme globale : {somme_globale}")
print(f"Écart-type global : {ecart_type_global:.2f}")

moyennes_epreuves = np.mean(notes, axis=0)
mins_epreuves = np.min(notes, axis=0)
maxs_epreuves = np.max(notes, axis=0)
std_epreuves = np.std(notes, axis=0)

print("Moyennes par épreuve :", moyennes_epreuves)
print("Min par épreuve :", mins_epreuves)
print("Max par épreuve :", maxs_epreuves)
print("Écart-type par épreuve :", std_epreuves)
moyennes_etudiants = np.mean(notes, axis=1)
mins_etudiants = np.min(notes, axis=1)
maxs_etudiants = np.max(notes, axis=1)
std_etudiants = np.std(notes, axis=1)

print("Moyenne personnelle :", moyennes_etudiants)
print("Note min. personnelle :", mins_etudiants)
print("Note max. personnelle :", maxs_etudiants)
print("Dispersion personnelle :", std_etudiants)

idx_top_etudiant = np.argmax(moyennes_etudiants)
meilleur_etudiant = noms[idx_top_etudiant]
meilleure_moyenne = moyennes_etudiants[idx_top_etudiant]

print(f"Top étudiant : {meilleur_etudiant} ({meilleure_moyenne:.2f})")
epreuves = np.array(["E1", "E2", "E3"])
idx_epreuve_difficile = np.argmin(moyennes_epreuves)
epreuve_difficile = epreuves[idx_epreuve_difficile]
print(f"Épreuve la plus difficile : {epreuve_difficile} (moy. {moyennes_epreuves[idx_epreuve_difficile]:.2f})")

seuil_moyenne = 12
masque_moyenne = moyennes_etudiants >= seuil_moyenne
etudiants_admis = noms[masque_moyenne]
notes_admis = notes[masque_moyenne]

print(f"Étudiants avec moyenne ≥ {seuil_moyenne} :", etudiants_admis)
print("Leurs notes :\n", notes_admis)
masque_e2 = notes[:, 1] >= 15
print("Étudiants avec ≥15 en E2 :", noms[masque_e2])

moyennes_colonne = moyennes_etudiants.reshape(-1, 1)
notes_enrichies = np.hstack([notes, moyennes_colonne])
print("Notes + moyenne individuelle :\n", notes_enrichies)
epreuves_ext = np.append(epreuves, "Moyenne")
print("Colonnes :", epreuves_ext)
ligne_moyennes = np.append(moyennes_epreuves, [np.mean(moyennes_etudiants)])
tableau_final = np.vstack([notes_enrichies, ligne_moyennes])
noms_ext = np.append(noms, "Moyennes globales")

print("Tableau final :\n", tableau_final)
print("Lignes :", noms_ext)
ecarts_colonne = std_etudiants.reshape(-1, 1)
notes_info = np.hstack([notes_enrichies, ecarts_colonne])
epreuves_finales = np.append(epreuves_ext, "Écart-type")
print("Tableau avec écart-type :\n", notes_info)
print("Colonnes finales :", epreuves_finales)

for nom, ligne in zip(noms_ext, tableau_final):
    valeurs = " | ".join(f"{val:.2f}" for val in ligne)
    print(f"{nom:>20s} : {valeurs}")