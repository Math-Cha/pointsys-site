# -*- coding: utf-8 -*-
"""Générateur du site pointsys.fr — méthode site-vitrine-pro.
Usage : python3 -I build.py   → génère dist/
Pour modifier un texte : éditer les dictionnaires ci-dessous puis relancer."""
import os, shutil, json, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refs_data import SITES, CATS
import anim
_LC=[0]
def _uid():
    _LC[0]+=1
    return 'l%d' % _LC[0]

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
DOMAIN = "https://www.pointsys.fr"
TEL, TEL_H = "01 88 59 04 90", "+33188590490"
MAIL = "contact@pointsys.fr"
ADR = ("1 rue Michelet", "94200 Ivry-sur-Seine")
LINKEDIN = "https://www.linkedin.com/company/pointsys-telecom/"

ICONS = {
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
 "menu": '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>',
 "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/>',
 "fibre": '<path d="M2 12h4l3-9 6 18 3-9h4"/>',
 "network": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>',
 "cam": '<path d="M16.75 12h3.632a1 1 0 0 1 .894 1.447l-2.034 4.069a1 1 0 0 1-1.708.134l-2.124-2.97"/><path d="M17.106 9.053a1 1 0 0 1 .447 1.341l-3.106 6.211a1 1 0 0 1-1.342.447L3.61 12.3a2.92 2.92 0 0 1-1.3-3.91L3.69 5.6a2.92 2.92 0 0 1 3.92-1.3z"/><path d="M2 19h3.76a2 2 0 0 0 1.8-1.1L9 15"/><path d="M2 21v-4"/><path d="M7 9h.01"/>',
 "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
 "server": '<rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>',
 "key": '<path d="m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4"/><path d="m21 2-9.6 9.6"/><circle cx="7.5" cy="15.5" r="5.5"/>',
 "bell": '<path d="M10.268 21a2 2 0 0 0 3.464 0"/><path d="M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326"/>',
 "monitor": '<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>',
 "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
 "doc": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="m9 15 2 2 4-4"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
 "calendar": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
 "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 "landmark": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
 "train": '<rect width="16" height="16" x="4" y="3" rx="2"/><path d="M4 11h16"/><path d="M12 3v8"/><path d="m8 19-2 3"/><path d="m18 22-2-3"/><path d="M8 15h.01"/><path d="M16 15h.01"/>',
 "hospital": '<path d="M12 6v4"/><path d="M14 14h-4"/><path d="M14 18h-4"/><path d="M14 8h-4"/><path d="M18 12h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/><path d="M18 22V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v18"/>',
 "school": '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
 "building": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/>',
 "city": '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>',
 "pin": '<path d="M20 10c0 4.99-5.54 10.19-7.4 11.8a1 1 0 0 1-1.2 0C9.54 20.19 4 14.99 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
}
def ic(n): return f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
def e(s): return html.escape(s, quote=True)
ARW = ic("arrow")

# ---------------------------------------------------------------- contenus
EXP = [
 dict(slug="reseaux-fibre", n="01", t="Réseaux & fibre optique", img="fibre.jpg", ico="fibre", gal=["cf-erp.jpg","vdi.jpg"],
  s="Fibre optique, câblage VDI cuivre, backbones et téléphonie pour bâtiments tertiaires.",
  lead="Des infrastructures de communication fiables, recettées et documentées, du local technique au poste de travail.",
  cards=[("fibre","Fibre optique","Tirage, raccordement et soudure, tiroirs optiques, recette par photométrie et réflectométrie."),
         ("network","Câblage VDI","Réseaux voix-données-images cuivre, baies de brassage, certification des liens."),
         ("server","Backbones et liaisons","Rocades optiques entre bâtiments et étages, reprise et rationalisation des réseaux existants."),
         ("phone","Téléphonie","Raccordement des équipements, migrations et déménagements de postes en site occupé.")],
  faq=[("Livrez-vous un dossier de recette ?","Oui : plans de repérage, cahiers de mesures et dossier des ouvrages exécutés sont remis à la réception."),
       ("Pouvez-vous reprendre un réseau existant ?","Oui. Nous auditons l'existant, conservons ce qui peut l'être et remettons l'ensemble à niveau."),
       ("Intervenez-vous hors des heures de bureau ?","Oui, lorsque l'activité du site l'exige, les coupures sont planifiées le soir ou le week-end.")]),
 dict(slug="surete", n="02", t="Sûreté électronique", img="video.jpg", ico="shield",
  s="Vidéoprotection, contrôle d'accès, détection d'intrusion et hypervision.",
  lead="Protéger les personnes et les sites sensibles avec des systèmes de sûreté intégrés, exploitables et maintenus dans la durée.",
  cards=[("cam","Vidéoprotection","Caméras IP, enregistrement, postes d'exploitation, extensions de systèmes existants."),
         ("key","Contrôle d'accès","Lecteurs de badges, gestion des droits, interphonie et portes sécurisées."),
         ("bell","Détection d'intrusion","Centrales, détecteurs et transmission d'alarme, maintenance préventive et corrective."),
         ("monitor","Hypervision","Supervision unifiée des dispositifs de sûreté et postes centraux de sécurité.")],
  faq=[("Travaillez-vous sur des sites sensibles ?","Oui : institutions, ministères et préfectures nous confient des opérations soumises à des exigences de confidentialité et d'habilitation."),
       ("Pouvez-vous intégrer un système existant ?","Oui, nous étendons ou faisons migrer les installations en place sans interrompre la protection du site."),
       ("Assurez-vous la maintenance ?","Oui, en contrat de maintenance préventive et corrective, avec un interlocuteur dédié.")]),
 dict(slug="securite-incendie", n="03", t="Sécurité incendie (SSI)", img="ssi.jpg", ico="flame",
  s="Systèmes de sécurité incendie, détection, mise en conformité et asservissements.",
  lead="Du remplacement de la centrale à la création du poste central de sécurité, des SSI conformes et opérationnels.",
  cards=[("flame","Systèmes de sécurité incendie","Remplacement et extension de SSI de catégorie A, centrales et tableaux de report."),
         ("bell","Détection","Détecteurs automatiques, déclencheurs manuels, remplacement des détecteurs ioniques."),
         ("bolt","Asservissements","Désenfumage, portes coupe-feu, compartimentage et diffusion de l'alarme."),
         ("monitor","Postes centraux de sécurité","Création et réaménagement des PC sécurité et de leurs reports.")],
  faq=[("Intervenez-vous en ERP occupé ?","Oui : hôpitaux, EHPAD, établissements d'enseignement et stations de métro, avec un phasage qui maintient la sécurité à chaque étape."),
       ("Accompagnez-vous la mise en service ?","Oui, essais, coordination avec le coordinateur SSI et le bureau de contrôle, puis formation des exploitants."),
       ("Proposez-vous la maintenance des SSI ?","Oui, en accord-cadre ou en contrat dédié, selon vos sites.")]),
 dict(slug="data-centers", n="04", t="Data centers", img="dc-salle.jpg", ico="server",
  s="Grands chantiers de data centers, salles informatiques et réseaux d'infrastructure.", gal=["dc-equipes.jpg","vdi.jpg"],
  lead="Des grands data centers d'opérateurs, comme ceux d'Orange à Val-de-Reuil et à Chartres, à la salle informatique en site occupé : des équipes dimensionnées pour les chantiers de data centers.",
  cards=[("city","Grands chantiers de data centers","Data centers d'opérateurs : câblage des salles, des locaux techniques et des liaisons entre bâtiments, en coordination avec l'entreprise générale et l'exploitant."),
         ("fibre","Câblage structuré à grande échelle","Chemins de câbles, rocades et trunks fibre, brassage de centaines de baies, recette et repérage exhaustifs."),
         ("server","Salles informatiques et urbanisation","Implantation des baies, cloisonnement des allées, organisation des liaisons cuivre et fibre."),
         ("calendar","Équipes et planning","Équipes renforcées selon les phases du chantier, livraisons par salle et respect des jalons de mise en service.")],
  faq=[("Pouvez-vous intervenir sur un grand chantier de data center ?","Oui. Nous mobilisons des équipes dimensionnées selon les phases, avec un encadrement dédié et une recette salle par salle."),
       ("Travaillez-vous aussi en environnement exploité ?","Oui, nous aménageons depuis plus de dix ans des salles informatiques et réseaux pour un grand opérateur télécom, dans les fenêtres validées avec l'exploitant."),
       ("Prenez-vous en charge l'électricité ?","Oui, les courants forts associés sont réalisés avec nos équipes ou celles de Bathelec, au sein du Groupe SITTE.")]),
]

STATS = [("<i>30</i> ans","d'expertise réseaux et sûreté, depuis 1996"),
         ("<i>50</i>+","marchés de référence publics et privés"),
         ("Classe <i>4</i>","Qualifelec courants faibles tertiaire"),
         ("<i>8</i>","départements d'Île-de-France")]

CLIENT_LOGOS = [("an","Assemblée nationale"),("ratp","RATP"),("orange","Orange"),("minefi","Ministère de l'Économie et des Finances"),
 ("interieur","Ministère de l'Intérieur"),("esr","Ministère de l'Enseignement supérieur et de la Recherche"),("dgfip","Finances publiques"),
 ("ccip","CCI Paris Île-de-France"),("cpam75","CPAM de Paris"),("chsf","Centre Hospitalier Sud Francilien"),("cd94","Département du Val-de-Marne"),
 ("sorbonne","Sorbonne Université"),("upc","Université Paris Cité"),("spie","Spie Batignolles"),("versailles","Ville de Versailles"),
 ("clichy","Ville de Clichy"),("rueil","Ville de Rueil-Malmaison"),("villejuif","Ville de Villejuif"),("massy","Ville de Massy"),("ensea","ENSEA")]
def logos_html(p=""):
    return '<div class="logos rv">' + "".join(f'<div class="lg" title="{e(n)}"><img src="{p}img/logos/{k}.png" alt="{e(n)}" loading="lazy"></div>' for k,n in CLIENT_LOGOS) + '</div>'

CLIENTS = ["Assemblée nationale","RATP","Ministère de l'Économie et des Finances","Ministère de l'Intérieur",
 "Ministère de l'Éducation nationale","Préfecture de la région Île-de-France","Orange","DRFiP Île-de-France",
 "CCI Paris Île-de-France","CPAM de Paris","Centre Hospitalier Sud Francilien","Conseil départemental du Val-de-Marne",
 "Sorbonne Université","Ville de Versailles","ENSEA"]

REALS = [("Sûreté","2023-2024","Assemblée nationale","Remplacement du système d'hypervision des dispositifs de sûreté, puis travaux d'électricité et de courants faibles de sûreté."),
 ("SSI","2021-2024","RATP · Ligne 4","Systèmes de sécurité incendie du projet Symphonie, après plusieurs stations du réseau et le prolongement de la ligne 14."),
 ("Contrôle d'accès","2025-2026","Préfecture de la région Île-de-France","Remplacement des installations de contrôle d'accès de l'immeuble Le Ponant."),
 ("SSI","2025-2026","Centre Hospitalier Sud Francilien","Mise aux normes du SSI de l'EHPAD Le Village à Arpajon, en établissement occupé."),
 ("VDI · Courants faibles","2021-2024","Ministère de l'Économie et des Finances","Remplacement des infrastructures numériques voix, données, images et des réseaux électriques associés."),
 ("Data centers","2014-2024","Orange · Val-de-Reuil et Chartres","Aménagement des salles informatiques et réseaux des data centers, sur plusieurs marchés successifs.")]

# Références complètes (source : dossiers de références POINTSYS transmis en nov. 2026)
REF_CF = [
 ("Centre Hospitalier Sud Francilien","Mise aux normes SSI de l'EHPAD Le Village (Arpajon) – lot électricité et asservissements","2025-2026"),
 ("Ville de Massy","Réhabilitation de la halle couverte du marché du centre – courants forts et faibles","2025-2026"),
 ("Ville de Dammarie-lès-Lys","Rénovation de la Maison de l'emploi – courants forts et faibles","2025-2026"),
 ("CPAM de Paris","Restructuration des locaux du 1er étage de l'immeuble Bercy","2025-2026"),
 ("Préfecture de la région Île-de-France","Remplacement du contrôle d'accès de l'immeuble Le Ponant","2025-2026"),
 ("ENSEA","Réhabilitation, extension et maintenance de la vidéoprotection","2024"),
 ("Assemblée nationale","Travaux d'électricité et prestations de courants faibles de sûreté","2024"),
 ("Assemblée nationale","Remplacement du système d'hypervision des dispositifs de sûreté","2023-2024"),
 ("Ministère de l'Intérieur et des Outre-mer","Accord-cadre d'acquisition, d'installation et d'extension de systèmes de sûreté","2023-2024"),
 ("DRFiP Île-de-France et Paris","Mise à niveau des systèmes de câblage courants faibles","2023-2024"),
 ("Orange","Aménagement des salles informatiques et réseaux de data centers","2014-2024"),
 ("Conseil départemental du Val-de-Marne","Câblage VDI dans les collèges du département","2020-2024"),
 ("Ville de Clichy","Entretien, dépannage et extension des équipements de sécurité des bâtiments communaux","2022-2025"),
 ("Ville de Villejuif","Maintenance des installations de détection d'intrusion des bâtiments communaux","2022-2023"),
 ("Conseil départemental du Val-de-Marne","Maintenance des systèmes de télésécurité et de contrôle d'accès","2022-2023"),
 ("Sorbonne Université","Aménagement de laboratoires – courants forts et faibles","2021-2022"),
 ("CPAM de Paris","Accord-cadre d'entretien des immeubles – lot électricité courants forts et faibles","2022-2025"),
 ("CAF de la Seine-Saint-Denis","Entretien et modification des installations électriques et du câblage informatique","2021-2023"),
 ("Centre Hospitalier Sud Francilien","Remplacement des détecteurs ioniques de l'EHPAD Le Village","2022-2024"),
 ("Centre Hospitalier Sud Francilien","Relocalisation du service post-cure (Corbeil-Essonnes) – lot électricité CFO/CFA","2021-2022"),
 ("Ministère de l'Économie et des Finances","Remplacement des infrastructures numériques voix, données, images et réseaux électriques","2021-2024"),
 ("Ville de Rueil-Malmaison","Aménagement, grosses réparations et entretien des bâtiments communaux","2021-2024"),
 ("CPAM de la Seine-Saint-Denis","Aménagement de quatre espaces d'accueil","2021-2022"),
 ("CCI Paris Île-de-France","Travaux tous corps d'état – lot électricité","2022-2025"),
 ("CIPAV","Rénovation de trois niveaux d'un immeuble de bureaux","2021-2022"),
 ("Ville de Versailles","Entretien des bâtiments communaux, du CCAS et de la communauté d'agglomération","2022-2025"),
]
REF_SSI = [
 ("RATP","Projet Symphonie – ligne 4","2021-2024"),
 ("RATP","Prolongement de la ligne 14 – mise en place du SSI","2021-2022"),
 ("RATP","Stations Champs-Élysées–Clemenceau, Créteil-L'Échat et Porte de Choisy","2019-2020"),
 ("Ministère de l'Enseignement supérieur et de la Recherche","Remplacement du SSI et création d'un poste central de sécurité, site Descartes (Paris 5e)","2021-2023"),
 ("Ville de Clichy","Entretien et extension des équipements de sécurité des bâtiments communaux","2023-2024"),
 ("Conseil départemental du Val-de-Marne","Collèges Willy-Ronis et Amédée-Dunois","2022"),
 ("Centre Hospitalier René-Dubos (Cergy-Pontoise)","GHT Nord-Ouest Vexin Val-d'Oise","2021-2022"),
 ("Spie Batignolles","Opération AMT Italie","2021-2024"),
 ("Orange","Remplacement des infrastructures numériques","2021"),
]
REF_VIDEO = [
 ("Assemblée nationale","Hypervision et vidéoprotection des dispositifs de sûreté","2023-2024"),
 ("Conseil départemental du Val-de-Marne","Nouveau système de vidéoprotection dans les collèges","2021"),
 ("Université Paris Cité","Nouveau système de vidéoprotection en site occupé","2021"),
 ("CPAM de la Seine-Saint-Denis","Extension du système de vidéoprotection","2022"),
 ("Ministère de l'Économie et des Finances","Infrastructures numériques et vidéoprotection","2021-2024"),
]

SECT = [("landmark","Institutions et ministères","Assemblée, ministères, préfectures, services de l'État : des sites sensibles et habilités."),
        ("train","Transports","Stations et lignes de métro : sécurité incendie et réseaux en environnement exploité."),
        ("hospital","Santé","Centres hospitaliers et EHPAD, établissements occupés 24 h/24."),
        ("school","Enseignement et recherche","Universités, écoles, collèges et laboratoires."),
        ("city","Collectivités","Villes et départements : entretien et extension du patrimoine bâti."),
        ("building","Tertiaire et opérateurs","Sièges, organismes sociaux, salles informatiques et data centers.")]

ENG = [("calendar","Accords-cadres pluriannuels","Des équipes qui connaissent vos sites, un interlocuteur stable sur toute la durée du marché."),
       ("shield","Sites sensibles et occupés","Confidentialité, habilitations, coupures planifiées : l'activité continue pendant les travaux."),
       ("doc","Recettes documentées","Mesures, plans de repérage et DOE remis à chaque réception, pour une exploitation sereine."),
       ("wrench","Maintenance dans la durée","Contrats préventifs et correctifs pour garder vos systèmes disponibles.")]

STEPS = [("Visite et diagnostic","Un chargé d'affaires visite le site, relève l'existant et identifie les contraintes d'exploitation."),
         ("Étude et offre","Une proposition argumentée, avec choix techniques, planning et phasage."),
         ("Travaux en site occupé","Équipes encadrées, interventions planifiées, propreté et sécurité du chantier."),
         ("Recette et maintenance","Essais, dossier de recette, formation des exploitants, puis maintenance si vous le souhaitez.")]

CERTS = [("Qualifelec CFMGTI · classe 4","Courants faibles moyen et gros tertiaire, industrie (20 à 49 exécutants)"),
         ("Mention Fibre optique","Réseaux optiques : raccordement, soudure et recette"),
         ("Mention Maintenance","Maintenance des installations courants faibles"),
         ("Domaine Réseaux de communications","Infrastructures VDI cuivre et fibre"),
        ]

BAND = "Un projet, un accord-cadre, un programme multi-sites ? Nos chargés d'affaires vous répondent sous 48 h."

# ---------------------------------------------------------------- gabarit
def brand(p):
    svg = anim.logo(_uid()).replace('style="display:block;width:100%;height:auto"', 'style="display:block;height:66px;width:auto"')
    return f'<a class="brand" href="{p}index.html" aria-label="POINTSYS Télécom, accueil">{svg}</a>'

def shell(title, desc, body, p="", path="", active=""):
    canon = DOMAIN + "/" + path
    nav_exp = "".join(f'<a href="{p}expertises/{x["slug"]}.html">{ic(x["ico"])}<span>{x["t"]}<small>{e(x["s"])}</small></span></a>' for x in EXP)
    def on(k): return ' class="on"' if active == k else ""
    ld = {"@context":"https://schema.org","@type":"Electrician","name":"POINTSYS Télécom","url":DOMAIN,
          "telephone":"+33 1 88 59 04 90","email":MAIL,"address":{"@type":"PostalAddress","streetAddress":ADR[0],
          "postalCode":"94200","addressLocality":"Ivry-sur-Seine","addressCountry":"FR"},"areaServed":"Île-de-France",
          "parentOrganization":{"@type":"Organization","name":"Groupe SITTE"}}
    foot_exp = "".join(f'<li><a href="{p}expertises/{x["slug"]}.html">{x["t"]}</a></li>' for x in EXP)
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg"><meta property="og:url" content="{canon}"><meta property="og:locale" content="fr_FR">
<link rel="icon" type="image/svg+xml" href="{p}img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head><body>
<div class="top"><div class="wrap"><span class="hide-m">Réseaux · Fibre optique · Sûreté · Sécurité incendie — Île-de-France · Une société du Groupe SITTE</span>
<div class="r"><a href="tel:{TEL_H}">{ic("phone")}{TEL}</a><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a><a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ic("linkedin")}</a></div></div></div>
<header class="h"><div class="wrap">
{brand(p)}
<nav class="m">
<div class="dd"><a href="{p}index.html#expertises"{on("exp")}>Expertises</a><div class="menu">{nav_exp}</div></div>
<a href="{p}index.html#secteurs">Secteurs</a>
<a href="{p}references.html"{on("refs")}>Références</a>
<a href="{p}entreprise.html"{on("ent")}>L'entreprise</a>
<a href="{p}contact.html"{on("contact")}>Contact</a>
<a class="btn btn-o" href="{p}contact.html#form">Demander un devis {ARW}</a>
</nav>
<a class="callm" href="tel:{TEL_H}" aria-label="Appeler POINTSYS Télécom">{ic("phone")}</a>
<button class="burger" aria-label="Menu">{ic("menu")}</button>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="cols">
<div>{brand(p)}<p>Réseaux et fibre optique, sûreté électronique, sécurité incendie et data centers pour les bâtiments tertiaires, publics et privés d'Île-de-France. Une société du Groupe SITTE.</p></div>
<div><h4>Expertises</h4><ul>{foot_exp}</ul></div>
<div><h4>POINTSYS</h4><ul><li><a href="{p}references.html">Références</a></li><li><a href="{p}entreprise.html">L'entreprise</a></li><li><a href="{p}contact.html">Contact</a></li><li><a href="https://www.bathelec.fr" target="_blank" rel="noopener">Bathelec, groupe SITTE</a></li></ul></div>
<div><h4>Contact</h4><ul><li>{ADR[0]}<br>{ADR[1]}</li><li><a href="tel:{TEL_H}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
</div>
<div class="bot"><span>© POINTSYS Télécom — Groupe SITTE</span><span><a href="{p}mentions-legales.html">Mentions légales</a> · <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></span></div>
</div></footer>
<script>
try{{history.scrollRestoration='manual'}}catch(e){{}}
function toTop(){{try{{window.scrollTo(0,0);document.documentElement.scrollIntoView({{block:'start'}})}}catch(e){{}}}}
if(!location.hash){{toTop();addEventListener('DOMContentLoaded',toTop);addEventListener('load',()=>{{toTop();setTimeout(toTop,150)}})}}
document.querySelector('.burger')?.addEventListener('click',()=>document.querySelector('nav.m').classList.toggle('open'));
document.querySelectorAll('nav.m a').forEach(a=>a.addEventListener('click',()=>document.querySelector('nav.m').classList.remove('open')));
const io=new IntersectionObserver(es=>es.forEach(x=>{{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
</script>
</body></html>'''

def band(p):
    return f'<section class="band" style="padding-top:{0}px"><div class="wrap"><div class="box"><p>{BAND}</p><a class="btn btn-o" href="{p}contact.html#form">Demander un devis {ARW}</a></div></div></section>'

def cta(p):
    return f'''<section class="cta"><div class="wrap"><div class="box">
<div class="rv"><span class="kicker">Parlons de votre projet</span><h2>Un interlocuteur unique pour les réseaux et la sûreté de vos bâtiments.</h2>
<p class="lead">Visite, étude et proposition sur demande, sans engagement.</p></div>
<div class="contact-l rv"><a class="t" href="tel:{TEL_H}">{ic("phone")}{TEL}</a><a class="t" href="mailto:{MAIL}">{ic("mail")}{MAIL}</a>
<a class="btn btn-o" href="{p}contact.html#form">Demander un devis {ARW}</a></div>
</div></div></section>'''

def reals_html(items, cls=""):
    return f'<div class="reals {cls}">' + "".join(
        f'<article class="real rv"><div class="meta"><span>{e(a)}</span><span>{b}</span></div><h3>{e(c)}</h3><p>{e(d)}</p></article>'
        for a,b,c,d in items) + '</div>'

# ---------------------------------------------------------------- pages
def home():
    p = ""
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a,b in STATS)
    exps = "".join(f'''<a class="exp rv" href="expertises/{x["slug"]}.html"><div class="ph"><img src="img/{x["img"]}" alt="{e(x["t"])}" loading="lazy"></div>
<div class="bd"><span class="n">{x["n"]}</span><h3>{x["t"]}</h3><p>{e(x["s"])}</p><span class="link">Découvrir {ARW}</span></div></a>''' for x in EXP)
    eng = "".join(f'<div class="rv"><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i,t,d in ENG)
    sect = "".join(f'<li><span class="ico">{ic(i)}</span><div><h3>{t}</h3><p>{e(d)}</p></div></li>' for i,t,d in SECT)
    clients = "".join(f'<div>{e(c)}</div>' for c in CLIENTS)
    steps = "".join(f'<div class="step rv"><h3>{t}</h3><p>{d}</p></div>' for t,d in STEPS)
    certs = "".join(f'<div><b>{t}</b><span>{d}</span></div>' for t,d in CERTS)
    body = f'''<section class="hero"><div class="wrap"><div class="grid">
<div><span class="kicker">POINTSYS Télécom · Groupe SITTE</span>
<h1>Les réseaux et la sûreté de vos bâtiments, <em>100 % disponibles.</em></h1>
<p class="lead">Fibre optique, câblage VDI, sûreté électronique, sécurité incendie et data centers : nous équipons et maintenons les bâtiments tertiaires, publics et privés des grands comptes, du site occupé au grand chantier.</p>
<div class="ctas"><a class="btn btn-o" href="contact.html#form">Demander un devis {ARW}</a><a class="btn btn-l" href="#expertises">Nos expertises</a></div></div>
<div class="pic"><img src="img/hero.jpg" alt="Hall d'un bâtiment tertiaire équipé de vidéoprotection et de contrôle d'accès">
<div class="badge"><span class="ico">{ic("shield")}</span><div><b>Sites sensibles</b><span>Assemblée nationale, RATP, ministères, préfecture</span></div></div></div>
</div>
<div class="stats">{stats}</div></div></section>
{band(p)}
<section id="expertises"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Nos expertises</span><h2>Quatre métiers, une même exigence de disponibilité.</h2>
<p class="lead">Des réseaux qui transportent l'information aux systèmes qui protègent les personnes, nous couvrons l'ensemble des courants faibles de vos bâtiments.</p></div></div>
<div class="exp-grid">{exps}</div></div></section>
<section class="soft"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">100 % disponible</span><h2>Un partenaire de long terme<br>pour les donneurs d'ordre exigeants.</h2></div>
<p class="lead" style="max-width:440px">Une grande partie de notre activité repose sur des marchés pluriannuels : nos clients nous confient leurs sites dans la durée.</p></div>
<div class="eng">{eng}</div></div></section>
{map_section("carte", "Nos réalisations", "Nos chantiers en Île-de-France et en région.", True)}
<section id="data-centers"><div class="wrap split">
<div class="rv"><span class="kicker">Grands chantiers</span><h2>Du data center au bâtiment public.</h2>
<p class="lead" style="margin-top:14px">Data centers d'opérateurs, sièges, administrations, hôpitaux, établissements recevant du public : nos équipes déploient fibre optique et câblage courants faibles à grande échelle, en chantier neuf comme en site occupé.</p>
<ul class="sect">
<li><span class="ico">{ic("server")}</span><div><h3>Data centers</h3><p>Salles informatiques et réseaux des data centers d'Orange à Val-de-Reuil et à Chartres.</p></div></li>
<li><span class="ico">{ic("network")}</span><div><h3>Courants faibles en ERP</h3><p>Câblage VDI, fibre et sûreté dans les bâtiments publics et tertiaires occupés.</p></div></li>
<li><span class="ico">{ic("doc")}</span><div><h3>Recette exhaustive</h3><p>Mesures, repérage et documentation prêts pour l'exploitation.</p></div></li></ul>
<div style="margin-top:28px"><a class="btn btn-l" href="expertises/data-centers.html">Notre expertise data centers {ARW}</a></div></div>
<div class="img dcimgs rv"><img src="img/dc-equipes.jpg" alt="Techniciens tirant de la fibre au-dessus des baies d'un data center" loading="lazy"><img src="img/cf-erp.jpg" alt="Technicien courants faibles dans le faux plafond d'un établissement recevant du public" loading="lazy"></div>
</div></section>
<section id="secteurs"><div class="wrap split">
<div class="img rv"><img src="img/video.jpg" alt="Poste central de sécurité et murs d'images de vidéoprotection" loading="lazy"></div>
<div class="rv"><span class="kicker">Secteurs d'intervention</span><h2>Au service des bâtiments publics et privés.</h2>
<ul class="sect">{sect}</ul></div></div></section>
<section class="soft" id="references"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Ils nous font confiance</span><h2>Des références institutionnelles.</h2></div>
<a class="link" href="references.html">Toutes nos références {ARW}</a></div>
{logos_html()}</div></section>
<section><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Réalisations</span><h2>Des opérations de premier plan.</h2>
<p class="lead">Accords-cadres, sites sensibles, bâtiments occupés : quelques opérations récentes.</p></div>
<a class="link" href="references.html">Toutes nos réalisations {ARW}</a></div>
{reals_html(REALS, "home-reals")}</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Notre méthode</span><h2>De la visite à la recette.</h2></div></div>
<div class="steps">{steps}</div></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="sec-head rv"><div><span class="kicker">Qualifications</span><h2>Des compétences reconnues.</h2></div></div>
<div class="certs rv">{certs}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="gbox rv">
<div class="t"><span class="kicker">Groupe SITTE</span><h2>Un ancrage francilien, la solidité d'un groupe.</h2>
<p>POINTSYS Télécom fait partie du Groupe SITTE, aux côtés de Bathelec pour l'électricité. Ensemble, nous proposons aux maîtres d'ouvrage un lot électricité complet, courants forts et courants faibles. Depuis Ivry-sur-Seine, nos équipes interviennent dans toute l'Île-de-France.</p>
<div class="zone"><span>75</span><span>77</span><span>78</span><span>91</span><span>92</span><span>93</span><span>94</span><span>95</span></div>
<a class="btn btn-l" href="entreprise.html">Découvrir l'entreprise {ARW}</a></div>
<div class="im" style="background-image:url(img/dc-salle.jpg)"></div></div></div></section>
{cta(p)}'''
    return shell("POINTSYS Télécom | Réseaux, fibre optique, sûreté et sécurité incendie en Île-de-France",
                 "POINTSYS Télécom (Groupe SITTE) installe et maintient réseaux VDI, fibre optique, vidéoprotection, contrôle d'accès et SSI des bâtiments tertiaires, publics et privés d'Île-de-France.",
                 body, p, "", "")

def expertise(x):
    p = "../"
    cards = "".join(f'<div class="card rv"><div class="ico">{ic(i)}</div><h3>{t}</h3><p>{e(d)}</p></div>' for i,t,d in x["cards"])
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in x["faq"])
    gal = ('<div class="gal rv">' + "".join(f'<img src="../img/{g}" alt="{e(x["t"])}" loading="lazy">' for g in x["gal"]) + '</div>') if x.get("gal") else ""
    others = "".join(f'<a href="{o["slug"]}.html">{o["t"]} {ARW}</a>' for o in EXP if o is not x)
    body = f'''<section class="phero"><div class="wrap"><div class="grid">
<div><div class="crumb"><a href="../index.html">Accueil</a> / <a href="../index.html#expertises">Expertises</a> / {x["t"]}</div>
<div class="num">{x["n"]} — EXPERTISE</div><h1>{x["t"]}</h1><p>{e(x["lead"])}</p>
<div style="margin-top:28px"><a class="btn btn-o" href="../contact.html#form">Demander un devis {ARW}</a></div></div>
<div class="pic"><img src="../img/{x["img"]}" alt="{e(x["t"])}"></div></div></div></section>
<section><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Ce que nous réalisons</span><h2>{x["t"]} : nos interventions.</h2></div></div>
<div class="cards4">{cards}</div>{gal}</div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Questions fréquentes</span><h2>Vos questions.</h2></div></div>
<div class="faq rv">{faq}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><div><span class="kicker">Nos autres expertises</span></div></div><div class="other">{others}</div></div></section>
{cta(p)}'''
    return shell(f'{x["t"]} | POINTSYS Télécom', x["lead"], body, p, f'expertises/{x["slug"]}.html', "exp")

def table(rows):
    return '<table class="reftable"><thead><tr><th>Client</th><th>Opération</th><th>Période</th></tr></thead><tbody>' + "".join(
        f'<tr><td>{e(a)}</td><td>{e(b)}</td><td>{c}</td></tr>' for a,b,c in rows) + '</tbody></table>'

def map_data():
    W, H = 593.2, 478.8
    sites = [dict(id=i, logo=l, client=c, lieu=lu, lat=la, lon=lo, paris=pa,
                  cats=sorted(set(o[2] for o in ops), key=CATS.index), ops=ops) for (i,l,c,lu,la,lo,pa,ops) in SITES]
    data = {"W": W, "H": H, "proj": [1.43, 49.25, 0.66, 420], "full": [-120, -45, W + 140, H + 60], "paris": [194.0, 117.6, 124.7, 100.7],
            "ext": [{"id": "orange-vdr", "label": "Val-de-Reuil (27)"}, {"id": "orange-cha", "label": "Chartres (28)"}], "sites": sites}
    return sites, data

def map_section(sid="carte", kicker="Carte des réalisations", title="Nos chantiers sur la carte.", link=False):
    sites, data = map_data()
    frag = open(os.path.join(ROOT, "idf_map.svgfrag"), encoding="utf-8").read()
    n_ops = sum(len(x["ops"]) for x in sites); n_cli = len(set(x["client"] for x in sites))
    vb = " ".join(str(v) for v in data["full"])
    skip = ("ratp-ce", "ratp-pc", "ratp-l14", "ratp-cr", "chsf2", "orange-cha")
    mlist = "".join('<button data-site="%s">%s</button>' % (x["id"], e(x["client"])) for x in sites if x["id"] not in skip)
    more = f'<a class="link" href="references.html">Toutes nos références {ARW}</a>' if link else ""
    return (f'<section id="{sid}"><div class="wrap">'
      f'<div class="sec-head rv"><div><span class="kicker">{kicker}</span><h2>{title}</h2>'
      f'<p class="lead">Survolez ou touchez un point pour découvrir l\'opération réalisée.</p></div>{more}</div>'
      f'<div class="mapbox" id="refmap"><div class="map rv"><div class="mtools"><button data-z="idf" class="on">Île-de-France &amp; data centers</button><button data-z="paris">Paris</button></div>'
      f'<svg viewBox="{vb}" role="img" aria-label="Carte des références POINTSYS">{frag}<g id="pins"></g></svg>'
      f'<span class="hint">Survolez ou touchez un point</span></div>'
      f'<aside class="mpanel rv" id="mpanel"><div class="def"><span class="kicker">Nos chantiers</span><h3>Une présence dans toute l\'Île-de-France</h3>'
      f'<div class="big"><div><b>{len(sites)}</b><span>sites de référence</span></div><div><b>{n_ops}</b><span>opérations</span></div><div><b>{n_cli}</b><span>donneurs d\'ordre</span></div></div>'
      f"<p>Le point au centre regroupe les sites parisiens : cliquez dessus pour zoomer. Les data centers d'Orange à Val-de-Reuil et à Chartres apparaissent en bleu, hors Île-de-France.</p>"
      f'<div class="mlist">{mlist}</div></div></aside></div>'
      f'<script type="application/json" id="refdata">{json.dumps(data, ensure_ascii=False)}</script></div></section>'
      f'<script>{MAPJS}</script>')

def references():
    W, H = 593.2, 478.8
    PROJ = [1.43, 49.25, 0.66, 420]
    frag = open(os.path.join(ROOT, "idf_map.svgfrag"), encoding="utf-8").read()
    sites = [dict(id=i, logo=l, client=c, lieu=lu, lat=la, lon=lo, paris=pa,
                  cats=sorted(set(o[2] for o in ops), key=CATS.index), ops=ops) for (i,l,c,lu,la,lo,pa,ops) in SITES]
    data = {"W": W, "H": H, "proj": PROJ, "full": [-120, -45, W + 140, H + 60], "paris": [194.0, 117.6, 124.7, 100.7],
            "ext": [{"id": "orange-vdr", "label": "Val-de-Reuil (27)"}, {"id": "orange-cha", "label": "Chartres (28)"}], "sites": sites}
    n_ops = sum(len(x["ops"]) for x in sites); n_cli = len(set(x["client"] for x in sites))
    chips = '<button class="on" data-f="*">Toutes</button>' + "".join(f'<button data-f="{e(c)}">{e(c)}</button>' for c in CATS)
    def logo(x):
        if x["logo"]: return f'<div class="lgo"><img src="img/logos/{x["logo"]}.png" alt="{e(x["client"])}" loading="lazy"></div>'
        return f'<div class="lgo ini"><span>{ic("landmark")}</span></div>'
    def card(grp):
        x = grp[0]
        cats = sorted(set(c for g in grp for c in g["cats"]), key=CATS.index)
        tags = "".join(f"<span>{e(c)}</span>" for c in cats)
        multi = len(grp) > 1
        ops = "".join(f"<li>{('<i>' + e(g['lieu']) + '</i>') if multi else ''}<b>{o[1]}</b>{e(o[0])}</li>" for g in grp for o in g["ops"])
        loc = f"{len(grp)} sites" if multi else x["lieu"]
        return (f'<article class="rcard rv" data-id="{x["id"]}" data-cats="{e("|".join(cats))}" tabindex="0">'
                f'<div class="rtop">{logo(x)}<div class="tags">{tags}</div></div>'
                f'<h3>{e(x["client"])}</h3><div class="loc">{ic("pin")}{e(loc)}</div>'
                f'<ul>{ops}</ul><span class="see">Voir sur la carte {ARW}</span></article>')
    groups = {}
    for x in sites: groups.setdefault(x["client"], []).append(x)
    cards = "".join(card(g) for g in groups.values())
    vb = " ".join(str(v) for v in data["full"])
    body = (f'<section class="phero"><div class="wrap"><div class="grid solo"><div>'
      f'<div class="crumb"><a href="index.html">Accueil</a> / Références</div><h1>Nos références</h1>'
      f"<p>Institutions, transports, santé, enseignement, collectivités et opérateurs : {n_cli} donneurs d'ordre nous ont confié {n_ops} opérations, en Île-de-France et sur des data centers en région.</p></div></div></div></section>"
      f'<section style="padding-top:10px"><div class="wrap">{logos_html()}</div></section>'
      f'{map_section()}'
      f'<section style="padding-top:0" id="realisations"><div class="wrap">'
      f'<div class="sec-head rv"><div><span class="kicker">Le détail</span><h2>Toutes nos références.</h2>'
      f'<p class="lead">Cliquez sur une carte pour la situer sur la carte.</p></div></div>'
      f'<div class="chips" id="chips">{chips}</div><div class="rgrid" id="rgrid">{cards}</div></div></section>'
      f'{cta("")}')
    return shell("Références | POINTSYS Télécom", "Références de POINTSYS Télécom sur une carte : Assemblée nationale, RATP, ministères, préfecture, hôpitaux, collectivités, data centers d'Orange à Val-de-Reuil et Chartres.", body, "", "references.html", "refs")

MAPJS = r"""(function(){
const root=document.getElementById('refmap'); if(!root) return;
const D=JSON.parse(document.getElementById('refdata').textContent);
const svg=root.querySelector('svg'), gp=svg.querySelector('#pins'), panel=document.getElementById('mpanel'), def=panel.innerHTML;
const FULL=D.full, PAR=D.paris; let vb=FULL.slice(), mode='idf', sel=null, filt='*';
const NS='http://www.w3.org/2000/svg';
const P=(lon,lat)=>[(lon-D.proj[0])*D.proj[2]*D.proj[3],(D.proj[1]-lat)*D.proj[3]];
const PIN='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 4.99-5.54 10.19-7.4 11.8a1 1 0 0 1-1.2 0C9.54 20.19 4 14.99 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>';
function setVB(v){vb=v;svg.setAttribute('viewBox',v.join(' '));draw();}
function anim(to){const fr=vb.slice(),t0=performance.now();function st(t){const k=Math.min(1,(t-t0)/450),e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;setVB(fr.map((a,i)=>a+(to[i]-a)*e));if(k<1)requestAnimationFrame(st)}requestAnimationFrame(st)}
function el(n,a){const x=document.createElementNS(NS,n);for(const k in a)x.setAttribute(k,a[k]);return x}
const vis=x=>filt==='*'||x.cats.includes(filt);
function draw(){gp.innerHTML='';const s=vb[2]/D.W, r=7*s;svg.querySelectorAll('.dlab').forEach(t=>t.setAttribute('font-size',11*s));
 const show=D.sites.filter(x=>vis(x)&&(mode==='paris'||!x.paris));
 show.forEach(x=>{const [cx,cy]=P(x.lon,x.lat);const g=el('g',{class:'pin'+(sel===x.id?' on':'')+(x.cats.includes('Data centers')?' dc':''),tabindex:0,'aria-label':x.client,'data-id':x.id});
  g.append(el('circle',{class:'halo',cx,cy,r:r*2}),el('circle',{class:'dot',cx,cy,r}));
  const ex=D.ext.find(e=>e.id===x.id); if(ex&&mode==='idf'){const t=el('text',{class:'elab',x:cx,y:cy+r*3.6,'text-anchor':'middle','font-size':9.5*s});t.textContent=ex.label;g.append(t)}
  g.addEventListener('mouseenter',()=>open(x));g.addEventListener('click',e=>{e.stopPropagation();open(x,true)});g.addEventListener('focus',()=>open(x));gp.append(g)});
 if(mode==='idf'){const ps=D.sites.filter(x=>x.paris&&vis(x));if(ps.length){const [cx,cy]=P(2.3488,48.8566);const g=el('g',{class:'pin cl',tabindex:0,'aria-label':'Paris'});
  g.append(el('circle',{class:'halo',cx,cy,r:r*2.6}),el('circle',{class:'dot',cx,cy,r:r*1.8}));const t=el('text',{x:cx,y:cy+4*s,'text-anchor':'middle','font-size':12*s});t.textContent=ps.length;g.append(t);
  g.addEventListener('click',e=>{e.stopPropagation();zoomParis()});g.addEventListener('mouseenter',()=>{panel.innerHTML='<div class="def"><span class="kicker">Paris</span><h3>'+ps.length+' sites de référence dans Paris</h3><p style="margin-top:12px">Cliquez sur le point pour zoomer sur Paris.</p></div>'});gp.append(g)}}
}
function mark(){gp.querySelectorAll('.pin[data-id]').forEach(g=>g.classList.toggle('on',g.dataset.id===sel));document.querySelectorAll('.rcard').forEach(c=>c.classList.toggle('on',c.dataset.id===sel))}
function lg(x){return x.logo?'<div class="lgo"><img src="img/logos/'+x.logo+'.png" alt=""></div>':''}
function open(x,force){if(sel===x.id&&!force)return;sel=x.id;mark();
 panel.innerHTML=lg(x)+'<h3>'+x.client+'</h3><div class="loc">'+PIN+x.lieu+'</div><ul class="ops">'+x.ops.map(o=>'<li><div class="meta"><span>'+o[2]+'</span><span>'+o[1]+'</span></div><p>'+o[0]+'</p></li>').join('')+'</ul><div class="mlist" style="margin-top:22px"><button data-reset>← Toutes les références</button></div>';
 panel.querySelector('[data-reset]').onclick=()=>{sel=null;mark();panel.innerHTML=def;bindDef()};
}
function zoomParis(){mode='paris';btns();anim(PAR)}
function zoomIdf(){mode='idf';btns();anim(FULL)}
function btns(){root.querySelectorAll('[data-z]').forEach(b=>b.classList.toggle('on',b.dataset.z===mode))}
root.querySelectorAll('[data-z]').forEach(b=>b.onclick=()=>b.dataset.z==='paris'?zoomParis():zoomIdf());
function go(id){const x=D.sites.find(y=>y.id===id);if(!x)return;root.scrollIntoView({behavior:'smooth',block:'center'});
 if(x.paris&&mode!=='paris')zoomParis();if(!x.paris&&mode!=='idf')zoomIdf();setTimeout(()=>open(x,true),460)}
function bindDef(){panel.querySelectorAll('[data-site]').forEach(b=>b.onclick=()=>{const x=D.sites.find(y=>y.id===b.dataset.site);if(x.paris&&mode!=='paris')zoomParis();if(!x.paris&&mode!=='idf')zoomIdf();setTimeout(()=>open(x,true),x.paris?460:0)})}
bindDef();
document.querySelectorAll('.rcard').forEach(c=>{c.addEventListener('click',()=>go(c.dataset.id));c.addEventListener('keydown',e=>{if(e.key==='Enter')go(c.dataset.id)})});
document.querySelectorAll('#chips button').forEach(b=>b.onclick=()=>{filt=b.dataset.f;document.querySelectorAll('#chips button').forEach(o=>o.classList.toggle('on',o===b));
 document.querySelectorAll('.rcard').forEach(c=>c.style.display=(filt==='*'||c.dataset.cats.split('|').includes(filt))?'':'none');draw()});
setVB(FULL);
})();"""


def entreprise():
    tl = [("1996","Création de POINTSYS, spécialiste des télécoms et de la fibre optique."),
          ("Groupe SITTE","Intégration au groupe, aux côtés de Bathelec, et recentrage sur les grands comptes publics et privés."),
          ("Aujourd'hui","Réseaux, sûreté, sécurité incendie et data centers pour l'État, les transports, la santé et le tertiaire.")]
    tlh = "".join(f'<div class="rv"><b>{a}</b><p>{e(b)}</p></div>' for a,b in tl)
    eng = "".join(f'<div class="rv"><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i,t,d in ENG)
    certs = "".join(f'<div><b>{t}</b><span>{d}</span></div>' for t,d in CERTS)
    body = f'''<section class="phero"><div class="wrap"><div class="grid">
<div><div class="crumb"><a href="index.html">Accueil</a> / L'entreprise</div><h1>L'entreprise</h1>
<p>Des femmes et des hommes des courants faibles, au service des bâtiments qui ne peuvent pas s'arrêter.</p></div>
<div class="pic"><img src="img/hero.jpg" alt="Hall d'un bâtiment tertiaire"></div></div></div></section>
<section><div class="wrap split" style="align-items:start">
<div class="rv"><span class="kicker">Notre histoire</span><h2>Trente ans de réseaux et de sûreté.</h2></div>
<div class="prose rv"><p>Créée en 1996 autour des télécommunications et de la fibre optique, POINTSYS Télécom a élargi son savoir-faire à la sûreté électronique, à la sécurité incendie et à l'aménagement des salles informatiques.</p>
<p>Intégrée au Groupe SITTE, l'entreprise travaille en complémentarité avec Bathelec, spécialiste de l'électricité des bâtiments tertiaires : les maîtres d'ouvrage disposent ainsi d'un lot électricité complet, courants forts et courants faibles.</p>
<p>Depuis Ivry-sur-Seine, nos chargés d'affaires et nos techniciens interviennent dans les huit départements d'Île-de-France, pour l'État, les transports, la santé, l'enseignement, les collectivités et le tertiaire privé.</p></div></div>
<div class="wrap"><div class="timeline" style="margin-top:48px">{tlh}</div></div></section>
<section class="soft"><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Nos engagements</span><h2>100 % disponible.</h2></div></div><div class="eng">{eng}</div></div></section>
<section><div class="wrap"><div class="sec-head rv"><div><span class="kicker">Qualifications</span><h2>Des compétences reconnues.</h2></div></div><div class="certs rv">{certs}</div></div></section>
{cta("")}'''
    return shell("L'entreprise | POINTSYS Télécom", "POINTSYS Télécom, société du Groupe SITTE créée en 1996 : réseaux, fibre optique, sûreté et sécurité incendie en Île-de-France.", body, "", "entreprise.html", "ent")

def contact():
    opts = "".join(f'<option>{x["t"]}</option>' for x in EXP) + "<option>Maintenance / contrat</option><option>Accord-cadre / marché public</option><option>Candidature</option><option>Autre</option>"
    body = f'''<section class="phero"><div class="wrap"><div class="grid solo"><div>
<div class="crumb"><a href="index.html">Accueil</a> / Contact</div><h1>Contact</h1>
<p>Visite, étude et proposition sur demande, sans engagement.</p></div></div></div></section>
<section id="form" style="padding-top:30px"><div class="wrap cgrid">
<div class="info rv"><span class="kicker">Nous joindre</span><h2>Parlons de votre projet.</h2>
<h3>Téléphone</h3><a href="tel:{TEL_H}">{ic("phone")}{TEL}</a>
<h3>E-mail</h3><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a>
<h3>Siège</h3><p>{ADR[0]}<br>{ADR[1]}</p>
<h3>Horaires</h3><p>Du lundi au vendredi, 9 h – 18 h</p>
<h3>Recrutement</h3><p>Techniciens courants faibles, fibre optique, SSI : envoyez votre candidature via le formulaire (objet « Candidature »).</p></div>
<form class="f rv" action="https://formsubmit.co/{MAIL}" method="POST">
<input type="hidden" name="_subject" value="Demande de contact via pointsys.fr"><input type="hidden" name="_next" value="{DOMAIN}/merci.html"><input type="hidden" name="_captcha" value="false"><input type="text" name="_honey" style="display:none">
<div><label>Prénom</label><input name="Prénom" required></div><div><label>Nom</label><input name="Nom" required></div>
<div><label>Organisation</label><input name="Organisation"></div><div><label>Fonction</label><input name="Fonction"></div>
<div><label>E-mail</label><input type="email" name="email" required></div><div><label>Téléphone</label><input name="Téléphone"></div>
<div class="full"><label>Objet</label><select name="Objet">{opts}</select></div>
<div class="full"><label>Votre projet</label><textarea name="Message" required placeholder="Site, nature des travaux, calendrier…"></textarea></div>
<div class="full"><button class="btn btn-o" type="submit">Envoyer ma demande {ARW}</button></div></form></div></section>'''
    return shell("Contact | POINTSYS Télécom", "Contactez POINTSYS Télécom, Ivry-sur-Seine : réseaux, fibre optique, sûreté et sécurité incendie en Île-de-France.", body, "", "contact.html", "contact")

def legal():
    body = f'''<section><div class="wrap legal"><span class="kicker">Informations légales</span><h1 style="font-size:44px">Mentions légales</h1>
<h2>Éditeur</h2><p>POINTSYS Télécom, société par actions simplifiée, société du Groupe SITTE<br>Siège social : {ADR[0]}, {ADR[1]}<br>Téléphone : {TEL} — {MAIL}<br>SIREN : 848 099 586 — SIRET : 848 099 586 00036 — APE : 4321A<br>Directeur de la publication : Pierre Chaplain</p>
<h2>Hébergement</h2><p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Données personnelles</h2><p>Les informations transmises via le formulaire sont utilisées uniquement pour répondre à votre demande ou traiter votre candidature, et ne sont jamais cédées à des tiers. Le formulaire est acheminé par le service FormSubmit. Conformément au RGPD, vous disposez d'un droit d'accès, de rectification et de suppression : écrivez à {MAIL}.</p>
<h2>Cookies</h2><p>Ce site n'utilise aucun cookie de mesure d'audience ni de publicité.</p>
<h2>Propriété intellectuelle</h2><p>Les contenus de ce site (textes, visuels) sont la propriété de POINTSYS Télécom, sauf mention contraire. Les noms de clients sont cités à titre de références.</p></div></section>'''
    return shell("Mentions légales | POINTSYS Télécom", "Mentions légales du site pointsys.fr.", body, "", "mentions-legales.html")

def merci():
    body = f'''<section class="phero"><div class="wrap"><div class="grid solo"><div><span class="kicker">Message envoyé</span><h1>Merci, votre demande est bien reçue.</h1>
<p>Un chargé d'affaires vous recontacte sous 48 h ouvrées.</p><div style="margin-top:28px"><a class="btn btn-o" href="index.html">Retour à l'accueil {ARW}</a></div></div></div></div></section>'''
    return shell("Merci | POINTSYS Télécom", "Demande envoyée.", body, "", "merci.html")

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#ef7d1a"/><text x="32" y="42" font-family="Arial,Helvetica,sans-serif" font-size="26" font-weight="800" fill="#fff" text-anchor="middle">PS</text></svg>'

def build():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, "expertises"))
    shutil.copytree(os.path.join(ROOT, "img"), os.path.join(DIST, "img"))
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
    fav = anim.icon("fv", 64).replace('class="ps-logo" ', 'xmlns="http://www.w3.org/2000/svg" ')
    open(os.path.join(DIST, "img", "favicon.svg"), "w", encoding="utf-8").write(fav)
    pages = {"index.html": home(), "references.html": references(), "entreprise.html": entreprise(),
             "contact.html": contact(), "mentions-legales.html": legal(), "merci.html": merci()}
    for x in EXP: pages[f'expertises/{x["slug"]}.html'] = expertise(x)
    for k, v in pages.items():
        open(os.path.join(DIST, k), "w", encoding="utf-8").write(v)
    urls = "".join(f"<url><loc>{DOMAIN}/{'' if k=='index.html' else k}</loc></url>" for k in pages if k != "merci.html")
    open(os.path.join(DIST, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print("OK", len(pages), "pages")

if __name__ == "__main__":
    build()
