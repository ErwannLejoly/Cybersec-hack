# cybersec-hack/reporting.py

from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

def generate_report(target, nmap_results, cracked_passwords, ad_graph, output_file, post_exploitation_data):
    print("[+] Génération du rapport final...")

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("rapport_template.html")

    html_content = template.render(
        target=target,
        nmap=nmap_results,
        cracked=cracked_passwords,
        ad=ad_graph,
        post=post_exploitation_data
    )

    with open("rapport_temp.html", "w") as f:
        f.write(html_content)

    try:
        pdfkit.from_file("rapport_temp.html", output_file)
        print(f"[✓] Rapport généré : {output_file}")
    except Exception as e:
        print(f"[!] Erreur lors de la génération du PDF : {e}")
