# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 07:23:58 2023

@author: bebis
References:
    - https://spotipy.readthedocs.io/
    - https://phoenixnap.com/kb/windows-set-environment-variable
    - https://www.section.io/engineering-education/spotify-python-part-1/#:~:text=The%20first%20step%20is%20to,can%20be%20whatever%20you%20want.
    - https://spotipy.readthedocs.io/en/2.22.1/?highlight=recently#spotipy.client.Spotify.current_user_recently_played
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import datetime
import time

from cred import client_id, client_secret, redirect_uri, username


def get_playlist_tracks(sp,username,playlist_id):
    '''
    sp... spotipy API client instance
    username... spotify username
    playlist_id... playlist id (not name)
    '''
    playlist = sp.user_playlist(user=username,playlist_id=playlist_id) # dict with keys 'tracks'
    track_list = playlist['tracks']  #dict with key 'items', which values are the tracks
    tracks_list_items=track_list['items']

    while track_list['next']:
        print('next page')
        track_list=sp.next(track_list) # use the sp (the client) to go to next page, weird however why this needs be done on ['tracks'] level
        tracks_list_items.extend(track_list['items'])
    # tracks_list_items is a list of dicts. Each dict is a track. 
        # item in the list has keys: dict_keys(['added_at', 'added_by', 'is_local', 'primary_color', 'track', 'video_thumbnail'])
        # item['track'] in the list has keys: dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'episode', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track', 'track_number', 'type', 'uri'])
        # item['track']['name'] is the tracks name
        # item['track']['artists'] can be a list of dicts of contributors
    return tracks_list_items

def get_playlist(sp,username,list_name):
    playlists=sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name']=='Mit Star bewertet':
            the_list=playlist
    return the_list

def test_playlist_tracks(username):
    scope = "playlist-read-private"
    client_id = "d4cbf68c29034fbf931ef56c28dde292"
    client_secret = "d4dd4e7045484a99b9e725bdad466633"
    redirect_uri = "http://localhost:9000" # this can be any URL, but must be registered in your app settings
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

    the_list=get_playlist(sp,username=username,list_name='Mit Star bewertet')
    tracks_list_items=get_playlist_tracks(sp=sp,username=username,playlist_id=the_list['id'])

    return tracks_list_items[-1]    


def create_api_session(scope,client_id,client_secret, redirect_uri):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
    return sp

def export_spotify_playlists(username,sp):
   
#    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
    playlists = sp.user_playlists(username)

    # Create a dictionary to store the playlist titles and their tracks
    all_playlists = {}

    for playlist in playlists["items"]:
        if playlist["owner"]["id"] == username:
            playlist_title = playlist["name"]
            print(playlist_title)
            playlist_tracks_short = []
            playlist_tracks = get_playlist_tracks(sp=sp,username=username,playlist_id=playlist['id'])

            for item in playlist_tracks:     
#                print('\n')
#                print(item)
#                print(item['track']['name'])
                track_name = item['track']['name']
                artist_name = item["track"]["artists"][0]["name"]
                playlist_tracks_short.append((track_name,artist_name))
            all_playlists[playlist_title] = playlist_tracks_short

#    print(all_playlists)
    return all_playlists


def playlists_to_dataframe(all_playlists,to_clipboard = False, savefile="my_spotify_playlists.xlsx"):
    # Initialize an empty list to store the rows of the DataFrame
    rows = []
    
    # Iterate over each playlist in the all_playlists dictionary
    for playlist_title, playlist_tracks in all_playlists.items():
        # Iterate over each track in the playlist
        for track in playlist_tracks:
            # Split the track name and artist name using the " - " separator
            artist, title = track[0],track[1]
            # Append a new row to the list of rows
            rows.append({"Playlist": playlist_title, "Artist": artist, "Title": title})
    
    # Convert the list of rows into a pandas DataFrame
    df = pd.DataFrame(rows)
    
    if to_clipboard == True:
        df.to_clipboard()
    if savefile != None:
        df.to_excel(savefile, index=False)

    return df

def recently_played(sp):   
    '''
    Problem: Only tracks that have been played to the end are on this list.
    '''
    # Get the user's recently played tracks
    number_tracks=1
    results = sp.current_user_recently_played(limit=number_tracks,after=date_to_timestamp('2023-04-1'))
    print(results.keys())
    print(results['next'])
    while results['next']:
        results=sp.next(results)
        print('next page of {}'.format(number_tracks))
        for item in results['items']:
            track = item['track']
            print(track['name'], '-', track['artists'][0]['name'])



def date_to_timestamp(input_date):
    # Convert input date to datetime object
    dt = datetime.datetime.strptime(input_date, '%Y-%m-%d')

    # Convert datetime object to Unix timestamp in milliseconds
    unix_timestamp = int(time.mktime(dt.timetuple()))*1000

    return unix_timestamp


if __name__ == '__main__':
    scope = "playlist-read-private"
    sp = create_api_session(scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
    all_playlists = export_spotify_playlists(username,sp)
    df = playlists_to_dataframe(all_playlists)

#    timestamp = date_to_timestamp('2023-04-30')
#    scope = "user-read-recently-played"
#    sp = create_api_session(scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
#    recently_played(sp)
