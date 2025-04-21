# cybersec-hack/main.py

import argparse
from reconnaissance import run_nmap_scan, parse_nmap_results, extended_reconnaissance
from exploitation import run_metasploit_exploit, run_mimikatz, run_adaptive_exploitation
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
    parser.add_argument('--dry-run', action='store_true', help="Afficher les étapes sans exécuter les attaques")
    parser.add_argument('--interactive', action='store_true', help="Menu interactif pour choisir les modules")
    args = parser.parse_args()

    print("[+] Vérification et installation des outils requis...")
    check_and_install_tools()

    def run_all():
        xml_file = run_nmap_scan(args.target)
        if not xml_file:
            print("[!] Scan échoué. Abandon.")
            return

        nmap_results = parse_nmap_results(xml_file)
        extended_reconnaissance(args.target, nmap_results)

        if args.dry_run:
            print("[DRY-RUN] Étapes suivantes simulées mais non exécutées.")
            print("- Exploitation adaptative
- Mimikatz
- Post-exploitation
- Crack password
- Analyse AD
- Nikto
- Brute-force web")
            return

        run_adaptive_exploitation(nmap_results)
        mimikatz_results = run_mimikatz()
        post_exploitation_data = run_dummy_post_exploitation()
        cracked = crack_passwords(mimikatz_results)
        ad_graph = analyze_ad()
        run_nikto_scan(args.target)
        run_web_bruteforce(args.target)

        generate_report(
            args.target,
            nmap_results,
            cracked,
            ad_graph,
            args.output,
            post_exploitation_data
        )

    if args.full:
        run_all()

    elif args.interactive:
        while True:
            print("""
=== Menu Interactif Cybersec-hack ===
1. Scan Nmap
2. Reconnaissance étendue
3. Exploitation Metasploit adaptative
4. Mimikatz
5. Post-exploitation
6. Crack password
7. Analyse AD
8. Scan Web (Nikto)
9. Brute-force HTTP
10. Générer le rapport
0. Quitter
            """)
            choice = input("Choix > ")
            if choice == '1':
                xml_file = run_nmap_scan(args.target)
                parse_nmap_results(xml_file)
            elif choice == '2':
                extended_reconnaissance(args.target, parse_nmap_results(run_nmap_scan(args.target)))
            elif choice == '3':
                run_adaptive_exploitation(parse_nmap_results(run_nmap_scan(args.target)))
            elif choice == '4':
                run_mimikatz()
            elif choice == '5':
                run_dummy_post_exploitation()
            elif choice == '6':
                crack_passwords("mimikatz_output.txt")
            elif choice == '7':
                analyze_ad()
            elif choice == '8':
                run_nikto_scan(args.target)
            elif choice == '9':
                run_web_bruteforce(args.target)
            elif choice == '10':
                generate_report(args.target, [], [], "", args.output, {})
            elif choice == '0':
                print("[+] Sortie.")
                break
            else:
                print("[!] Choix invalide.")

if __name__ == '__main__':
    main()
