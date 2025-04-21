
# 🛠️ Cybersec-hack – Framework d'Orchestration d'Audit de Sécurité

**Cybersec-hack** est un outil d’audit de sécurité automatisé qui orchestre plusieurs outils bien connus (Nmap, Metasploit, John the Ripper, Mimikatz, BloodHound, Nikto, Hydra...) pour réaliser un test d'intrusion complet, du scan initial jusqu'au rapport final en PDF.


## 🚀 Fonctionnalités

| Module                  | Description |
|-------------------------|-------------|
| 🔍 Reconnaissance        | Scan furtif avec Nmap (TCP, services, OS) |
| 💥 Exploitation          | Attaque automatisée avec Metasploit (ex: EternalBlue) |
| 🧪 Post-exploitation     | Mimikatz, recherche de fichiers sensibles, vérification de privilèges |
| 🔐 Password cracking     | Crack des hashs avec John + rockyou.txt |
| 🧠 Analyse Active Directory | Intégration avec BloodHound (Neo4j) |
| 🌐 Scan de vulnérabilités Web | Nikto + parsing |
| 🧱 Brute-force HTTP      | Hydra (si serveur web détecté) |
| 📄 Génération de rapport | HTML → PDF avec résumé de l’audit |

---

## 📁 Structure du projet

```
cybersec-hack/
├── main.py
├── setup.py
├── reconnaissance.py
├── exploitation.py
├── post_exploitation.py
├── password_cracking.py
├── active_directory.py
├── vulnerability_scanner.py
├── reporting.py
├── templates/
│   └── rapport_template.html
└── tools/
    ├── mimikatz/
    └── wordlists/
        ├── rockyou.txt
        └── users.txt
```

---

## 🧰 Installation

```bash
git clone https://github.com/ErwannLejoly/cybersec-hack.git
cd cybersec-hack
python3 setup.py
```

⚠️ Nécessite `sudo` pour installer les outils système comme `nmap`, `john`, `neo4j`, `nikto`, `metasploit`, etc.

---
## ✅ Droits à attribuer
1. start.sh
Le script doit être exécutable :

```bash
chmod +x start.sh
Cela permet de le lancer avec ./start.sh
```
## 🧪 Utilisation

```bash
python3 main.py --target 192.168.1.10 --full --output rapport_final.pdf
```

**Arguments :**
- `--target` : IP ou hostname de la cible
- `--full` : Lance tous les modules en mode automatique
- `--output` : Nom du rapport PDF généré

---

## 📦 Outils intégrés (installés automatiquement)

- `nmap`
- `john`
- `metasploit-framework`
- `bloodhound`
- `neo4j`
- `nikto`
- `hydra`
- `wordlists` (rockyou.txt)

---

## 🧾 Rapport généré

Le rapport contient :
- Les hôtes et services détectés
- Les vulnérabilités exploitées
- Les mots de passe découverts
- Les chemins d’escalade de privilèges
- Les failles web et bruteforce
- Et bien plus…

---

## ⚠️ Avertissement

> Ce projet est uniquement destiné à des fins **pédagogiques** et **légales**.  
> Toute utilisation sur des systèmes non autorisés est **strictement interdite** et **pénalement répréhensible**.  
> Vous êtes **entièrement responsable** de l’usage que vous en faites.

---

## 📚 Auteur

Projet pédagogique réalisé pour les cours de cybersécurité avancée.  
By Erwann Lejoly

