# -*- coding: utf-8 -*-
# Références géolocalisées (source : dossiers de références POINTSYS, nov. 2026)
# (id, logo, client, lieu, lat, lon, paris, [(opération, période, domaine)])
SITES = [
 ("an","an","Assemblée nationale","Palais Bourbon, Paris 7e",48.8619,2.3186,True,[
   ("Remplacement du système d'hypervision des dispositifs de sûreté","2023-2024","Sûreté"),
   ("Travaux d'électricité et prestations de courants faibles de sûreté","2024","Sûreté"),
   ("Vidéoprotection des dispositifs de sûreté","2023-2024","Vidéoprotection")]),
 ("ratp-l4","ratp","RATP","Ligne 4, Paris",48.8530,2.3470,True,[
   ("Projet Symphonie : systèmes de sécurité incendie de la ligne 4","2021-2024","SSI")]),
 ("ratp-ce","ratp","RATP","Station Champs-Élysées–Clemenceau, Paris 8e",48.8676,2.3141,True,[
   ("Système de sécurité incendie de la station","2019","SSI")]),
 ("ratp-pc","ratp","RATP","Station Porte de Choisy, Paris 13e",48.8200,2.3646,True,[
   ("Système de sécurité incendie de la station","2020","SSI")]),
 ("ratp-l14","ratp","RATP","Prolongement de la ligne 14 sud",48.8100,2.3550,False,[
   ("Mise en place du SSI d'une station du prolongement de la ligne 14","2021-2022","SSI")]),
 ("ratp-cr","ratp","RATP","Station Créteil-L'Échat",48.7963,2.4495,False,[
   ("Système de sécurité incendie de la station","2020","SSI")]),
 ("minefi","minefi","Ministère de l'Économie et des Finances","Bercy et Chevaleret, Paris 12e-13e",48.8380,2.3790,True,[
   ("Remplacement des infrastructures numériques voix, données, images","2021-2024","Réseaux & VDI"),
   ("Ouvrages électriques courants forts et faibles de l'administration centrale","2021-2024","Électricité"),
   ("Vidéoprotection des bâtiments","2021-2024","Vidéoprotection")]),
 ("interieur","interieur","Ministère de l'Intérieur et des Outre-mer","Paris",48.8722,2.3166,True,[
   ("Accord-cadre d'acquisition, d'installation et d'extension de systèmes de sûreté","2023-2024","Sûreté")]),
 ("esr","esr","Ministère de l'Enseignement supérieur et de la Recherche","Site Descartes, Paris 5e",48.8462,2.3480,True,[
   ("Remplacement du SSI et création d'un poste central de sécurité","2021-2023","SSI")]),
 ("prefidf","","Préfecture de la région Île-de-France","Immeuble Le Ponant, Paris 15e",48.8392,2.2775,True,[
   ("Remplacement des installations de contrôle d'accès","2025-2026","Sûreté")]),
 ("dgfip","dgfip","DRFiP Île-de-France et Paris","Paris",48.8670,2.3530,True,[
   ("Mise à niveau des systèmes de câblage courants faibles","2023-2024","Réseaux & VDI")]),
 ("cpam75","cpam75","CPAM de Paris","Bercy, Réaumur et Château-d'Eau, Paris",48.8690,2.3555,True,[
   ("Restructuration des locaux du 1er étage de l'immeuble Bercy","2025-2026","Électricité"),
   ("Accord-cadre d'entretien des immeubles, lot électricité courants forts et faibles","2022-2025","Électricité"),
   ("Réhabilitation des 2e et 3e étages et des sanitaires","2021","Électricité"),
   ("Réhabilitation et mise aux normes du centre de santé Réaumur","2020","Électricité")]),
 ("cipav","cipav","CIPAV","Avenue de la Grande-Armée, Paris 17e",48.8760,2.2900,True,[
   ("Rénovation des niveaux 2, 3 et 4 de l'immeuble","2021-2022","Électricité")]),
 ("ccip","ccip","CCI Paris Île-de-France","Paris",48.8746,2.3007,True,[
   ("Travaux tous corps d'état, lot électricité courants forts et faibles","2022-2025","Électricité")]),
 ("sorbonne","sorbonne","Sorbonne Université","Paris 12e",48.8494,2.3890,True,[
   ("Aménagement de laboratoires, courants forts et faibles","2021-2022","Électricité")]),
 ("upc","upc","Université Paris Cité","Paris 6e",48.8510,2.3400,True,[
   ("Nouveau système de vidéoprotection en site occupé","2021","Vidéoprotection")]),
 ("spie","spie","Spie Batignolles","Opération AMT Italie, Paris 13e",48.8310,2.3560,True,[
   ("Système de sécurité incendie","2021-2024","SSI")]),
 ("cd94","cd94","Département du Val-de-Marne","Collèges du département",48.7790,2.4550,False,[
   ("Câblage VDI dans les collèges du département","2020-2024","Réseaux & VDI"),
   ("Maintenance des systèmes de télésécurité et de contrôle d'accès","2022-2023","Sûreté"),
   ("Nouveau système de vidéoprotection dans les collèges","2021","Vidéoprotection"),
   ("SSI des collèges Willy-Ronis et Amédée-Dunois","2022","SSI")]),
 ("clichy","clichy","Ville de Clichy","Clichy-la-Garenne",48.9045,2.3060,False,[
   ("Entretien, dépannage et extension des équipements de sécurité des bâtiments communaux","2022-2025","Sûreté")]),
 ("villejuif","villejuif","Ville de Villejuif","Villejuif",48.7922,2.3634,False,[
   ("Maintenance de la détection d'intrusion des bâtiments communaux","2022-2023","Sûreté")]),
 ("massy","massy","Ville de Massy","Halle du marché du centre, Massy",48.7309,2.2713,False,[
   ("Réhabilitation de la halle couverte, courants forts et faibles","2025-2026","Électricité")]),
 ("dammarie","dammarie","Ville de Dammarie-lès-Lys","Maison de l'emploi, Dammarie-lès-Lys",48.5170,2.6390,False,[
   ("Rénovation de la Maison de l'emploi, courants forts et faibles","2025-2026","Électricité")]),
 ("chsf","chsf","Centre Hospitalier Sud Francilien","EHPAD Le Village, Arpajon",48.5900,2.2480,False,[
   ("Mise aux normes du SSI, lot électricité et asservissements","2025-2026","SSI"),
   ("Remplacement des détecteurs ioniques","2022-2024","SSI")]),
 ("chsf2","chsf","Centre Hospitalier Sud Francilien","Maison d'accueil Galignani, Corbeil-Essonnes",48.6110,2.4820,False,[
   ("Relocalisation du service post-cure, lot électricité CFO/CFA","2021-2022","Électricité")]),
 ("ensea","ensea","ENSEA","Cergy",49.0390,2.0710,False,[
   ("Réhabilitation, extension et maintenance de la vidéoprotection","2024","Vidéoprotection")]),
 ("dubos","","Centre hospitalier René-Dubos","Pontoise",49.0480,2.0950,False,[
   ("Sécurité incendie, GHT Nord-Ouest Vexin Val-d'Oise","2021-2022","SSI")]),
 ("caf93","caf","CAF de la Seine-Saint-Denis","Seine-Saint-Denis",48.9100,2.4400,False,[
   ("Entretien des installations électriques et du câblage informatique","2021-2023","Réseaux & VDI")]),
 ("cpam93","cpam93","CPAM de la Seine-Saint-Denis","Bobigny",48.9050,2.4520,False,[
   ("Aménagement de quatre espaces d'accueil","2021-2022","Électricité"),
   ("Extension du système de vidéoprotection","2022","Vidéoprotection")]),
 ("rueil","rueil","Ville de Rueil-Malmaison","Rueil-Malmaison",48.8770,2.1800,False,[
   ("Aménagement, grosses réparations et entretien des bâtiments communaux","2021-2024","Électricité")]),
 ("versailles","versailles","Ville de Versailles","Versailles",48.8049,2.1204,False,[
   ("Entretien des bâtiments communaux, du CCAS et de l'agglomération","2022-2025","Électricité")]),
 ("orange-vdr","orange","Orange","Data center de Val-de-Reuil (Eure)",49.2730,1.2100,False,[
   ("Aménagement des salles informatiques et réseaux du data center","2014-2024","Data centers")]),
 ("orange-cha","orange","Orange","Data center de Chartres (Eure-et-Loir)",48.4470,1.4890,False,[
   ("Aménagement des salles informatiques et réseaux du data center","2014-2024","Data centers")]),
]
CATS = ["Réseaux & VDI","Data centers","Sûreté","Vidéoprotection","SSI","Électricité"]
