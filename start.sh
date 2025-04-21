#!/bin/bash

echo "[+] Bienvenue dans Cybersec-hack"
echo "[+] Préparation de l'environnement..."

# Étape 1 : Installation des outils et dépendances
python3 setup.py

# Étape 2 : Demander la cible à auditer
read -p "[?] IP ou nom de domaine de la cible : " target

# Étape 3 : Nom du rapport de sortie
read -p "[?] Nom du rapport final (default: rapport_final.pdf) : " report
report=${report:-rapport_final.pdf}

# Étape 4 : Lancer l'audit complet
echo "[+] Lancement de l'audit sur $target..."
python3 main.py --target "$target" --full --output "$report"
