import requests

rouge = "\033[31m"
print(f"""{rouge} _     _ _______ _______      _____  _______ _____ __   _ _______
 |_____| |_____| |  |  | ___ |     | |______   |   | \  |    |   
 |     | |     | |  |  |     |_____| ______| __|__ |  \_|    |   
                                                                 """)

# Définition des choix
nombre_1 = "recherche réseau sociaux"
nombre_2 = "google dorking"
nombre_3 = "info adresse ip"

# Affichage des options
print("[1]", nombre_1)
print("[2]", nombre_2)
print("[3]", nombre_3)

chiffre_choisis = int(input("Quel méthode choisir ?: "))

# Recherche réseau sociaux 
if chiffre_choisis == 1:
    pseudo = input("[1] Entrer le pseudo : ")
    # URL pour OSINT réseau sociaux     
    instagram = f"https://www.instagram.com/{pseudo}"
    snapchat = f"https://www.snapchat.com/add/{pseudo}"
    Tiktok = f"https://www.tiktok.com/@{pseudo}"
    facebook = f"https://www.facebook.com/{pseudo}"
    reddit = f"https://www.reddit.com/r/{pseudo}/"
    X = f"https://www.x.com/{pseudo}/"
    linkedin = f"https://www.linkedin.com/pub/dir/{pseudo}"
    # Résultat
    print(f"URL générée :", instagram)
    print(f"URL générée :", snapchat)
    print(f"URL générée :", Tiktok)
    print(f"URL générée :", facebook)
    print(f"URL générée :", reddit)
    print(f"URL générée :", X)
    print(f"URL générée :", linkedin)

# Google dorking
elif chiffre_choisis == 2:
    print(f"Méthode choisie [2]: {nombre_2}")
    # Liste de propositions
    email_1 = "Recherche e-mail"
    réseau_num2 = "Recherche réseau sociaux"
    numéro_tel_3 = "Numéro de téléphone"
    photo_image_4 = "Photo et images"
    info_perso_5 = "Information personnelles"
    fichier_sensi_6 = "Fichier sensibles"
    print("[1]", email_1)
    print("[2]", réseau_num2)
    print("[3]", numéro_tel_3)
    print("[4]", photo_image_4)
    print("[5]", info_perso_5)
    print("[6]", fichier_sensi_6)
    
    choisis_google_dorking = int(input("Quel méthode choisir ?: "))
    
    if choisis_google_dorking == 1:
        # Email Google dorking
        cible = input("[1] Nom prénom de la cible : ")
        # Génération du Google dorking e-mail
        print(f"inurl:@gmail.com {cible}") 
        print(f"inurl:@yahoo.com {cible}") 
        print(f"inurl:@outlook.fr {cible}") 
    elif choisis_google_dorking == 2:
        # Réseaux sociaux Google dorking
        cible = input("[2] Quel est le nom et prénom de la personne : ")
        site_internet_choisis = input("Sur quel réseau social (exemple : instagram.com) ? : ")
        print(f"site:{site_internet_choisis} {cible}")
    elif choisis_google_dorking == 3:
        # Numéro Google dorking
        cible = input("[3] Nom prénom de la cible : ")
        print(f"{cible} numéro de téléphone")
        print(f"{cible} phone OR tel")
        print(f"intitle:contacts {cible}")
    elif choisis_google_dorking == 4:
        # Image Google dorking
        cible = input("[4] Nom prénom de la cible : ")
        print(f"site:pinterest.com inurl:images {cible}")
        print(f"filetype:jpg OR filetype:png {cible}")
    elif choisis_google_dorking == 5:
        # Info perso
        cible = input(f"[5] Nom prénom de la cible : ")
        print(f"filetype:pdf {cible} CV")
        print(f"intitle:curriculum vitae {cible}")
    elif choisis_google_dorking == 6:
        # Fichier sensible
        cible = input(f"[6] Nom prénom de la cible : ")
        print(f"filetype:txt {cible} password")
        print(f"filetype:log {cible}")
        print(f"filetype:sql {cible}")
        print(f"inurl:database {cible}")

# Adresse IP info
elif chiffre_choisis == 3:
    print(f"Méthode choisie [3]: {nombre_3}")
    ip = input("[3] L'adresse IP de la victime : ")
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    ip_info = response.json()
    print(f"Les infos de l'adresse {ip} :")
    for key, value in ip_info.items():
        print(f"{key}: {value}")
