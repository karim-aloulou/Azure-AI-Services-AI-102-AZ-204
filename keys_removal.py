import os
import re

def nettoyer_env_files_racine(trace_fichier):
    # Obtenir le chemin actuel
    racine = os.getcwd()
    trace = []
    
    # Parcours récursif des fichiers dans tous les sous-dossiers
    for root, _, files in os.walk(racine):
        for file in files:
            if file.endswith('.env'):
                file_path = os.path.join(root, file)
                trace += nettoyer_env_file(file_path)
    
    # Écriture des informations dans le fichier de traçabilité
    with open(trace_fichier, 'w') as trace_file:
        for ligne in trace:
            trace_file.write(ligne + '\n')

def nettoyer_env_file(file_path):
    trace_lignes = []
    try:
        with open(file_path, 'r') as file:
            lignes = file.readlines()
        
        nouvelles_lignes = []
        for ligne in lignes:
            if '=' in ligne and not ligne.strip().startswith('#'):  # Évite les commentaires
                nom_variable, valeur = map(str.strip, ligne.split('=', 1))
                trace_lignes.append(f"{file_path}: {nom_variable}: {valeur}")
                nouvelles_lignes.append(f"{nom_variable}=\n")  # Remplace par une ligne sans valeur
            else:
                nouvelles_lignes.append(ligne)
        
        # Écriture des nouvelles lignes sans affectations
        with open(file_path, 'w') as file:
            file.writelines(nouvelles_lignes)
        
        print(f"Nettoyé : {file_path}")
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path} : {e}")
    
    return trace_lignes

# Spécifiez le nom pour le fichier de traçabilité
fichier_trace = "trace_env.txt"

# Nettoyer les fichiers .env à partir du dossier actuel et sauvegarder les traces
nettoyer_env_files_racine(fichier_trace)
