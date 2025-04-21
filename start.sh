#!/bin/bash

# Affiche la bannière
cat << "EOF"
┏━━━┓━━━━━┏┓━━━━━━━━━━━━━━━━━━━━━━━━━━┏┓━━━━━━━━━━━┏┓━━━━━━
┃┏━┓┃━━━━━┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━━━━━━━┃┃━━━━━━
┃┃━┗┛┏┓━┏┓┃┗━┓┏━━┓┏━┓┏━━┓┏━━┓┏━━┓━━━━━┃┗━┓┏━━┓━┏━━┓┃┃┏┓━━━━
┃┃━┏┓┃┃━┃┃┃┏┓┃┃┏┓┃┃┏┛┃━━┫┃┏┓┃┃┏━┛┏━━━┓┃┏┓┃┗━┓┃━┃┏━┛┃┗┛┛━━━━
┃┗━┛┃┃┗━┛┃┃┗┛┃┃┃━┫┃┃━┣━━┃┃┃━┫┃┗━┓┗━━━┛┃┃┃┃┃┗┛┗┓┃┗━┓┃┏┓┓━━━━
┗━━━┛┗━┓┏┛┗━━┛┗━━┛┗┛━┗━━┛┗━━┛┗━━┛━━━━━┗┛┗┛┗━━━┛┗━━┛┗┛┗┛━━━━
━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

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

# Étape 5 : Proposer élévation de privilèges locale
read -p "[?] Voulez-vous tenter une élévation de privilège locale ? (y/N) : " elevate
if [[ "$elevate" =~ ^[Yy]$ ]]; then
    echo "[+] Lancement de l'escalade locale de privilèges..."
    python3 priv_esc.py
fi
