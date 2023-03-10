# coding=utf-8
import time
import schedule
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import base64



print("Starting Playlist updater")

# TIK TOK 
name = "Tik Tok Mix 2023 - Tik tok mix Dj 2023 - Tiktok mix  Trends - Musica TikTok 2023"
description_l = "Aquí Encontrarás las mejores canciones y Trends de Tiktok Para bailar. Canciones de Tik tok 2023, Canciones de Tik Tok nuevas 2023, Mix Tik Tok Nuevos, Mix Tik Tok Musica"

# Dread Mar i 
name_dread_mar_i= "Dread Mar I Mix - Dread Mar I tu sin mi - Dread mar i Exitos"
descrip_dread_mar_i= "Aquí podrás escuchar los éxitos de Dread Mar I como: Tú sin mí, Así fue, Hoja en blanco, Sálvame, Mi amor, Más allá de tus ojos, Nada, entre otros exitos en este Dread Mar I mix."

# Olga tañon
name_olga_t = 'Olga Tañon mix - Olga Tañon que digan lo que quieran de mi - Olga Tañon exitos'
descrip_olga_t = 'Aquí podrás escuchar los grandes éxitos de la cantante Olga Tañon como: Basta Ya, La gran fiesta, Mi eterno amor secreto, Es mentiroso, Muchacho malo, Vendrás llorando, entre otros éxitos en este Olga Tañon mix'
# tITO ROJAS

name_tito_rojas = 'Tito Rojas mix - Tito Rojas Exitos - Tito rojas mama -  Tito Rojas Ayer me dijeron '
descrip_tito_rojas = 'Aquí podras escuchar los éxitos de Tito Rojas como: Siempre seré, Señora de madrugada, Ella se hizo deseo, He chocado con la vida, A dónde irás. Entre otros éxitos en este Tito Rojas mix.'

#Paulo Londra 
name_paulo_l = "Paulo Londra Mix - Paulo Londra Plan A - Paulo Londra Tal vez -  Paulo Londra BZRP  - Pablo Londras"
descrip_paulo_l = "Aquí Podrás escuchar los éxitos de Paulo Londra como: Plan A, Paulo Londra: Bzrp Music Sessions, Vol. 23, Adán y Eva, Solo pienso en ti De la Guetto J Quiles y Paulo Londra. entre otros exitos en este Paulo Londra Mix."


ids_list = []
titles = []
description = []
  
def func():
    def playlist_update(ids,title,description):
        path = (ids+'.jpg')
        with open(path, "rb") as img_file:
            myimage = base64.b64encode(img_file.read())
        scope = 'playlist-modify-public ugc-image-upload'

        # Spotify Username (LO PUEDES SACAR DE LA URL DE TU PERFIL DE SPOTIFY)
        username = 'gstd8crpqrnjs940ilqor3jch'

        # Spotify Developer App Client ID and Secret ID
        SPOTIPY_CLIENT_ID = '53acaa23a7334fd4b25484934464f12f'
        SPOTIPY_CLIENT_SECRET = '22ca3b5b6f9d40c1a7d1f6e221a45043'

        # Sustituye la url de "redirect_url" por la que has puesto en la app del developers
        token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri='http://localhost:8888/callback')
        sp = spotipy.Spotify(auth=token)

        # Playlist Data (No tienes que hacer nada aquí)
        url = ('https://open.spotify.com/playlist/'+ids)
        id = url
        playlist_name = title
        playlist_description = description
        image_b64 = myimage

        sp.playlist_upload_cover_image(playlist_id=id, image_b64=myimage)
        sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)
    
    # Tik tok
    playlist_update(ids='75TkDSsEegBNzCe6caqL0j',title=name,description=description_l)
        # copieando la linea de a continuación puedes tener tantas playlists como quieras actualizar. Siempre y cuando pertenezcan al mismo perfil.
    
    # Olga tañon
    playlist_update(ids='7y8GqnRYnARSSEFKcfRoJ0',title=name_olga_t,description=descrip_olga_t)
     # Drear Mar i 
    playlist_update(ids='7HdznI8w84hBQ8VYetSGpA',title=name_dread_mar_i,description=descrip_dread_mar_i)
     #Tito Rojas
    playlist_update(ids='64TfDC9IYGg01PLTaKePvI',title=name_tito_rojas,description=descrip_tito_rojas)

 #Paulo Londra
    playlist_update(ids='6tsyNPT5hDupsU8BbouFwU',title=name_paulo_l,description=descrip_paulo_l)

    print("Playlists updated")

func()

# Puedes eliminar todo a partir de aquí si no quieres que el script actualice cada 5 min. 
# Yo lo tengo con el task scheduler y no uso esta función, porque es el task scheduler el que me lo ejecuta cuando quiero.

schedule.every(5).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(60)
    continue 

