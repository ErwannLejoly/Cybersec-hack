# cybersec-hack/password_cracking.py

import subprocess
import os

def crack_passwords(hash_file):
    print("[+] Tentative de cassage de mot de passe avec John the Ripper...")
    if not hash_file or not os.path.exists(hash_file):
        print("[!] Fichier de hash introuvable.")
        return []

    rockyou_path = "tools/wordlists/rockyou.txt"
    if not os.path.exists(rockyou_path):
        print("[!] Wordlist rockyou.txt manquante.")
        return []

    try:
        subprocess.run(["john", "--wordlist=" + rockyou_path, hash_file], check=True)
        subprocess.run(["john", "--show", hash_file], stdout=open("cracked_passwords.txt", "w"))

        with open("cracked_passwords.txt", "r") as f:
            results = f.read().strip().split('\n')
            print("[✓] Mots de passe craqués :")
            for line in results:
                print("  -", line)
            return results

    except subprocess.CalledProcessError as e:
        print("[!] Erreur avec John the Ripper :", e)
        return []
