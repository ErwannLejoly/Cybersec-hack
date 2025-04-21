# cybersec_tool/setup.py

import os
import subprocess
import shutil

def is_installed(tool):
    return shutil.which(tool) is not None

def apt_install(tool):
    subprocess.call(['sudo', 'apt', 'install', '-y', tool])

def download_mimikatz():
    print("[+] Téléchargement de Mimikatz...")
    os.makedirs("tools/mimikatz", exist_ok=True)
    url = "https://github.com/gentilkiwi/mimikatz/releases/latest/download/mimikatz_trunk.zip"
    subprocess.call(['wget', url, '-O', 'tools/mimikatz/mimikatz.zip'])
    subprocess.call(['unzip', '-o', 'tools/mimikatz/mimikatz.zip', '-d', 'tools/mimikatz'])

def download_rockyou():
    print("[+] Téléchargement du fichier rockyou.txt...")
    os.makedirs("tools/wordlists", exist_ok=True)
    subprocess.call(['sudo', 'apt', 'install', '-y', 'wordlists'])
    subprocess.call(['cp', '/usr/share/wordlists/rockyou.txt.gz', 'tools/wordlists/'])
    subprocess.call(['gunzip', 'tools/wordlists/rockyou.txt.gz'])

def setup_neo4j():
    print("[+] Installation et configuration de Neo4j...")
    apt_install('neo4j')

    print("[+] Démarrage de Neo4j service...")
    subprocess.call(['sudo', 'systemctl', 'enable', 'neo4j'])
    subprocess.call(['sudo', 'systemctl', 'start', 'neo4j'])

    print("[+] Configuration du mot de passe Neo4j par défaut...")
    try:
        subprocess.run([
            'cypher-shell',
            '-u', 'neo4j',
            '-p', 'neo4j',
            "CALL dbms.changePassword('password');"
        ], check=True)
        print("[✓] Mot de passe Neo4j changé en 'password'.")
    except subprocess.CalledProcessError:
        print("[!] Le mot de passe Neo4j a peut-être déjà été configuré.")

def check_and_install_tools():
    tools = {
        "nmap": "apt",
        "john": "apt",
        "msfconsole": "apt",  # metasploit-framework
        "bloodhound": "apt"
    }

    for tool, method in tools.items():
        if not is_installed(tool):
            print(f"[!] {tool} non installé. Installation...")
            if method == "apt":
                apt_install(tool)
        else:
            print(f"[✓] {tool} est déjà installé.")

    if not os.path.exists("tools/mimikatz/mimikatz.exe"):
        download_mimikatz()
    else:
        print("[✓] Mimikatz déjà téléchargé.")

    if not os.path.exists("tools/wordlists/rockyou.txt"):
        download_rockyou()
    else:
        print("[✓] rockyou.txt déjà présent.")

    setup_neo4j()

    print("[✓] Tous les outils nécessaires sont prêts.")
