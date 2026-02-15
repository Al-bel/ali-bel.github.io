#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def generer_album_html():
    """Génère automatiquement ALBUM-PHOTOS.html à partir des images du dossier"""
    
    # Configuration
    dossier_photos = './MOMENTS-SPECIAUX'
    template_file = 'ALBUM-PHOTOS-template.html'
    output_file = 'moments-speciaux.html'
    
    # Extensions acceptées
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG')
    
    print("🔍 Recherche des photos...")
    
    # Récupérer toutes les photos
    photos = []
    if os.path.exists(dossier_photos):
        for fichier in os.listdir(dossier_photos):
            if fichier.endswith(extensions):
                photos.append(fichier)
    
    if not photos:
        print(f"❌ Aucune photo trouvée dans {dossier_photos}")
        return False
    
    # Trier les photos par nom
    photos.sort()
    
    print(f"✅ {len(photos)} photos trouvées")
    for i, photo in enumerate(photos, 1):
        print(f"   {i}. {photo}")
    
    # Lire le template
    print(f"\n📖 Lecture du template {template_file}...")
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"❌ Fichier {template_file} introuvable !")
        return False
    
    # Générer les carousel items
    print("🎠 Génération du carrousel...")
    carousel_items = ""
    for i, photo in enumerate(photos):
        loading = "eager" if i == 0 else "lazy"
        carousel_items += f'''                    <div class="carousel-item">
                        <img src="./ALBUM-PHOTOS/{photo}" alt="Photo {i+1}" loading="{loading}">
                    </div>
'''
    
    # Générer les thumbnails
    print("🖼️  Génération des miniatures...")
    thumbnails = ""
    for i, photo in enumerate(photos):
        active = "active" if i == 0 else ""
        thumbnails += f'''                <div class="thumbnail {active}" onclick="goToSlide({i})">
                    <img src="./ALBUM-PHOTOS/{photo}" alt="Miniature {i+1}">
                </div>
'''
    
    # Remplacer dans le template
    html_final = template.replace('{{CAROUSEL_ITEMS}}', carousel_items.rstrip())
    html_final = html_final.replace('{{THUMBNAILS}}', thumbnails.rstrip())
    html_final = html_final.replace('{{TOTAL_PHOTOS}}', str(len(photos)))
    
    # Personnaliser pour Moments Spéciaux
    html_final = html_final.replace('<title>Album Photos - Protégé</title>', '<title>✨ Moments Spéciaux</title>')
    html_final = html_final.replace('<h2>🔒 Album Protégé</h2>', '<h2>✨ Moments Spéciaux</h2>')
    html_final = html_final.replace('href="photos.html"', 'href="index.html"')
    
    # Sauvegarder
    print(f"💾 Sauvegarde de {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_final)
    
    print(f"\n🎉 Succès ! {output_file} généré avec {len(photos)} photos\n")
    return True

if __name__ == '__main__':
    generer_album_html()