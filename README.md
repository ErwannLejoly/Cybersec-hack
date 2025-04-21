
# Cybersec-hack – Framework d'Orchestration d'Audit de Sécurité

**Cybersec-hack** est un orchestrateur Python qui centralise reconnaissance, exploitation, post-exploitation, analyse AD, brute-force web, génération de rapport PDF… et plus encore !



##  1. Installation & préparation

###  Arborescence du projet

```
cybersec-hack/
├── main.py
├── setup.py
├── start.sh
├── reconnaissance.py
├── exploitation.py
├── post_exploitation.py
├── password_cracking.py
├── active_directory.py
├── vulnerability_scanner.py
├── reporting.py
├── templates/
│   └── rapport_template.html
├── tools/
│   ├── mimikatz/
│   └── wordlists/
│       ├── rockyou.txt
│       └── users.txt
├── .gitignore
├── README.md
```

---

###  Outils installés automatiquement via `setup.py`

- `nmap`, `john`, `hydra`, `nikto`
- `msfconsole` (Metasploit) + PostgreSQL + `msfdb init`
- `bloodhound`, `neo4j` (avec mot de passe auto configuré)
- `enum4linux`, `whatweb`, `ldap-utils`, `exploitdb`
- `rockyou.txt` copié & décompressé dans `tools/wordlists/`
- `mimikatz` téléchargé depuis GitHub
- Dépendances Python : `jinja2`, `pdfkit`, `requests`

---

### ⚙ Étapes d'installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/ErwannLejoly/cybersec-hack.git
cd cybersec-hack
```

2. **Donner les droits au script de démarrage**

```bash
chmod +x start.sh
chmod +x setup.py  # Optionnel
```

3. **Lancer l’installation complète**

```bash
python3 setup.py
```

> ⚠️ Ce script installe tous les outils nécessaires avec `sudo` toutefois vérifier bien que python 3 est installé ou installer le manuellement , pour pouvoir executer correctement votre script.

---

## 🚀 2. 2 possibilitées d'utilisation: 

###  soit au Lancement automatique avec `start.sh`

```bash
./start.sh
```

> Demande la cible, le nom du rapport, puis lance l’audit complet

---

### soit en Mode manuel complet

```bash
python3 main.py --target <IP> --full --output rapport.pdf
```

- `--target` : IP ou hostname de la cible
- `--full` : Lance tous les modules en enchaînement
- `--output` : Nom du rapport final PDF (défaut : `rapport_final.pdf`)

---

###  Menu interactif

```bash
python3 main.py --target <IP> --interactive
```

Permet de lancer chaque module manuellement :
- Reconnaissance
- Exploitation (Metasploit)
- Mimikatz
- Post-exploitation
- Bruteforce Web
- Rapport final

---

### 👀 Mode simulation

```bash
python3 main.py --target <IP> --full --dry-run
```

> Affiche les étapes sans rien exécuter. Utile pour les démonstrations.

---

##  Rapport utilisant  du html pour générer un PDF: 

Le fichier PDF contient :
- Résultats de scan et services détectés
- Exploits utilisés et preuves
- Hashs cassés (via John + rockyou)
- Chemins d’exploitation AD (BloodHound)
- Brute-force Web
- Score de risque par service

---

## ⚠️⚠️ Avertissement de sécurité et d'utilisaton :⚠️⚠️

> Ce projet est fourni **à des fins pédagogiques uniquement**.  
> Toute utilisation non autorisée est **illégale** et sous votre responsabilité.

---

## 👨‍💻 Auteur

Projet Cybersec-hack – conçu pour les cours pratiques de cybersécurité offensive.
Par Erwann Lejoly
```
---
