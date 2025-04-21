# cybersec-hack/main.py

import argparse
from reconnaissance import run_nmap_scan, parse_nmap_results
from exploitation import run_metasploit_exploit, run_mimikatz
from post_exploitation import run_dummy_post_exploitation
from password_cracking import crack_passwords
from active_directory import analyze_ad
from reporting import generate_report
from setup import check_and_install_tools
from vulnerability_scanner import run_nikto_scan, run_web_bruteforce

def main():
    parser = argparse.ArgumentParser(description="Cybersec-hack - Orchestrateur d'audit de sécurité")
    parser.add_argument('--target', required=True, help='Cible à auditer (IP ou hostname)')
    parser.add_argument('--full', action='store_true', help='Lancer tous les modules')
    parser.add_argument('--output', default='rapport_final.pdf', help='Fichier de rapport')
    args = parser.parse_args()

    print("[+] Vérification et installation des outils requis...")
    check_and_install_tools()

    if args.full:
        # Phase de reconnaissance
        xml_file = run_nmap_scan(args.target)
        if xml_file:
            nmap_results = parse_nmap_results(xml_file)

            # Exploitation automatique avec Metasploit
            run_metasploit_exploit(nmap_results)

            # Post-exploitation avec Mimikatz
            mimikatz_results = run_mimikatz()

            # Recherche de fichiers sensibles + priv esc
            post_exploitation_data = run_dummy_post_exploitation()

            # Crack de mots de passe avec John + rockyou
            cracked = crack_passwords(mimikatz_results)

            # Analyse AD via BloodHound (placeholder)
            ad_graph = analyze_ad()

            # Scan de vulnérabilités web avec Nikto
            run_nikto_scan(args.target)

            # Brute-force HTTP si serveur web détecté
            run_web_bruteforce(args.target)

            # Génération du rapport final
            generate_report(
                args.target,
                nmap_results,
                cracked,
                ad_graph,
                args.output,
                post_exploitation_data
            )

if __name__ == '__main__':
    main()
