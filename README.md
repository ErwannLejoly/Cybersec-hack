 

# CyberSec-hack - Framework d'orchestration d'audit de sécurité

## Objectif

CyberSecTool est un orchestrateur d’audit de sécurité qui automatise toutes les étapes classiques d’un pentest :

- Scan réseau (Nmap)
- Exploitation (Metasploit)
- Post-exploitation (Mimikatz)
- Crack de mots de passe (John + rockyou)
- Cartographie Active Directory (BloodHound + SharpHound + Neo4j)
- Génération automatique d’un rapport

---

##  Structure du projet

```
cybersec_tool/
│
├── main.py                      # Point d'entrée principal
├── setup.py                     # Installation automatique des outils requis
│
├── reconnaissance.py            # Scan réseau et services
├── exploitation.py              # Exploits via Metasploit
├── post_exploitation.py         # Dump de credentials avec Mimikatz
├── password_cracking.py         # Crack de mots de passe
├── active_directory.py          # Cartographie AD avec BloodHound
├── reporting.py                 # Génération de rapport final (HTML / PDF)
│
└── tools/                       # Scripts, binaires, wordlists externes
    ├── mimikatz/
    └── wordlists/
```

---

##  Installation automatique (`setup.py`)

Le script `setup.py` vérifie et installe tous les outils nécessaires automatiquement :

###  Outils installés via `apt`

- `nmap`
- `john`
- `msfconsole` (Metasploit Framework)
- `bloodhound`
- `neo4j`
- `wordlists` (pour `rockyou.txt`)

### 📦 Téléchargement automatique

- **Mimikatz** : téléchargé depuis GitHub
- **rockyou.txt** : extrait automatiquement depuis `/usr/share/wordlists`

### 🛠️ Configuration automatique

- **Neo4j** : installé, activé, démarré
- **Mot de passe initial configuré** : `neo4j` → `password`

---

## ✅ Fonctionnalités prévues par module

| Module                  | Outil utilisé             | Intégration                                |
|-------------------------|---------------------------|---------------------------------------------|
| **Reconnaissance**       | `nmap`                    | `python-nmap` ou `subprocess`               |
| **Exploitation**         | `Metasploit`              | Automatisation via `msfrpc` ou `msfconsole` |
| **Post-exploitation**    | `Mimikatz`                | Exécuté sur la cible via PowerShell         |
| **Crack mot de passe**   | `John the Ripper` + rockyou.txt | Via subprocess                         |
| **Active Directory**     | `SharpHound`, `BloodHound`, `Neo4j` | Collecte et visualisation               |
| **Reporting**            | `Jinja2`, `WeasyPrint`    | HTML → PDF                                 |

---

## 📌 Utilisation

```bash
python3 main.py --target 192.168.1.10 --full --output rapport_final.pdf
```

---

## 🛡️ Avertissement

⚠️ Ce projet est destiné à un usage **éducatif** uniquement. Toute utilisation non autorisée de ces outils sur des systèmes tiers est **illégale**.

```
