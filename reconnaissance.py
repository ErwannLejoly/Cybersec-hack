# cybersec-hack/reconnaissance.py

import subprocess
import os
import xml.etree.ElementTree as ET

def run_nmap_scan(target):
    print(f"[+] Scan Nmap de la cible {target} en cours (mode furtif)...")
    output_file = f"nmap_scan_{target}.xml"

    try:
        subprocess.run([
            "nmap",
            "-sS",
            "-sV",
            "-O",
            "--max-retries", "2",
            "--host-timeout", "60s",
            "--scan-delay", "200ms",
            "--max-rate", "50",
            "-T2",
            "-oX", output_file,
            target
        ], check=True)
        print(f"[✓] Scan terminé. Résultat enregistré dans {output_file}")
        return output_file

    except subprocess.CalledProcessError:
        print("[!] Erreur lors du scan Nmap.")
        return None

def parse_nmap_results(xml_file):
    print(f"[+] Parsing des résultats de {xml_file}...")
    results = []
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for host in root.findall('host'):
            ip_elem = host.find('address')
            ip = ip_elem.get('addr') if ip_elem is not None else 'unknown'
            ports = []
            for port in host.findall(".//port"):
                port_id = port.get('portid')
                protocol = port.get('protocol')
                service = port.find('service')
                service_name = service.get('name') if service is not None else 'unknown'
                ports.append({
                    'port': port_id,
                    'protocol': protocol,
                    'service': service_name
                })
            results.append({'ip': ip, 'ports': ports})

        print(f"[✓] Parsing terminé : {len(results)} hôtes trouvés.")
        return results

    except Exception as e:
        print(f"[!] Erreur de parsing : {e}")
        return []

def extended_reconnaissance(target, nmap_results):
    print(f"[+] Début de la reconnaissance étendue sur {target}...")

    # WhatWeb - Détection de technologies Web
    try:
        print("[*] Scan WhatWeb...")
        subprocess.run(["whatweb", target], check=True)
    except Exception:
        print("[!] WhatWeb non disponible ou échec du scan.")

    # Enum4linux si SMB détecté
    if any("smb" in port['service'] for host in nmap_results for port in host['ports']):
        try:
            print("[*] Enum4linux détecté, lancement...")
            subprocess.run(["enum4linux", "-a", target])
        except Exception:
            print("[!] Enum4linux non disponible ou erreur.")

    # LDAP reconnaissance si port 389 détecté
    if any(port['port'] == '389' for host in nmap_results for port in host['ports']):
        try:
            print("[*] LDAP détecté, tentative de ldapsearch...")
            subprocess.run(["ldapsearch", "-x", "-H", f"ldap://{target}"], timeout=10)
        except Exception:
            print("[!] ldapsearch échoué ou indisponible.")

    print("[✓] Reconnaissance étendue terminée.")
