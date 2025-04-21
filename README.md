 
Voici un **README.md** complet pour ton dépôt GitHub **Cybersec-hack**, à jour avec toutes les fonctionnalités que tu as mises en place :

---

```markdown
# 🛠️ Cybersec-hack – Framework d'Orchestration d'Audit de Sécurité

Cybersec-hack est un outil d’audit de sécurité automatisé combinant des outils de cybersécurité open-source pour effectuer :

- La reconnaissance réseau
- L'exploitation de vulnérabilités
- La post-exploitation
- Le cassage de mots de passe
- L’analyse Active Directory
- Le scan de vulnérabilités web
- Le brute-force HTTP
- Et la génération d’un rapport complet en PDF

---

## 🚀 Fonctionnalités principales

| Module                   | Description |
|--------------------------|-------------|
| 🔍 Reconnaissance        | Scan furtif (Nmap) + parsing XML |
| 💥 Exploitation          | Metasploit : MS17-010 (EternalBlue) |
| 🧪 Post-Exploitation     | Mimikatz, escalade de privilèges, fichiers sensibles |
| 🔐 Crack MDP             | John the Ripper + rockyou.txt |
| 🧠 Active Directory      | Analyse via BloodHound (placeholder) |
| 🌐 Vulnérabilités Web    | Scan avec Nikto |
| 🧱 Brute-force Web       | Hydra avec wordlists |
| 📄 Rapport               | HTML rendu en PDF (Jinja2 + pdfkit) |

---

## 🗂️ Structure du projet

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

## 📦 Installation

```bash
git clone https://github.com/votre-user/cybersec-hack.git
cd cybersec-hack
python3 setup.py
```

> ⚠️ Nécessite `sudo` pour installer certains outils via APT.

---

## 🧪 Utilisation

```bash
python3 main.py --target 192.168.1.10 --full --output rapport_final.pdf
```

Options :
- `--target` : IP ou nom de domaine de la cible
- `--full` : Lance tous les modules automatiquement
- `--output` : Nom du fichier de rapport PDF généré

---

## 🧰 Outils requis (installés automatiquement)

- `nmap`
- `john`
- `metasploit-framework`
- `bloodhound`
- `neo4j`
- `nikto`
- `hydra`
- `wordlists` (rockyou.txt)

---

## 📄 Exemple de rapport

Le rapport est généré en HTML puis converti en PDF. Il inclut :
- La liste des ports ouverts et services détectés
- Les exploits lancés
- Les fichiers sensibles trouvés
- Les mots de passe cassés
- Les résultats de bruteforce web
- Les éléments AD analysés

---

## ⚠️ Avertissement

> Ce projet est fourni à **des fins pédagogiques uniquement**.  
> N'utilisez **jamais cet outil** sur un système sans **autorisation explicite**.  
> L’usage illégal de cet outil est **entièrement à vos risques et périls**.

---

## 📚 Auteurs

**Cybersec-hack** – projet éducatif de démonstration pour les cours de cybersécurité.
```

---

Souhaites-tu aussi que je te génère un fichier `requirements.txt` avec les bibliothèques Python nécessaires ?
