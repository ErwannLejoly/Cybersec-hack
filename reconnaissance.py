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

# Exemple d'utilisation depuis cybersec-hack (main.py)
if __name__ == "__main__":
    target = input("Cible à scanner : ")
    xml_file = run_nmap_scan(target)
    if xml_file:
        results = parse_nmap_results(xml_file)
        for host in results:
            print(f"Hôte : {host['ip']}")
            for port in host['ports']:
                print(f"  Port {port['port']}/{port['protocol']} - Service : {port['service']}")

