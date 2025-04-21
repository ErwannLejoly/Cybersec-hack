# cybersec-hack/reconnaissance.py

import subprocess
import os

def run_nmap_scan(target):
    print(f"[+] Scan Nmap de la cible {target} en cours...")
    output_file = f"nmap_scan_{target}.xml"

    try:
        subprocess.run([
            "nmap",
            "-sS",              # TCP SYN scan
            "-sV",              # Version des services
            "-O",               # Détection de l'OS
            "-T4",              # Vitesse de scan
            "-oX", output_file, # Export en XML
            target
        ], check=True)
        print(f"[✓] Scan terminé. Résultat enregistré dans {output_file}")
        return output_file

    except subprocess.CalledProcessError:
        print("[!] Erreur lors du scan Nmap.")
        return None
