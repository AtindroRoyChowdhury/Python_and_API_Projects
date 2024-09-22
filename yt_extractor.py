import requests
from urllib.parse import urlencode

def to_query_string(parameters):
    return urlencode(parameters, safe='')

def get_playlist_data(playlist_id, api_key):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    parameters = {
        'part': 'snippet',
        'maxResults': 50,
        'playlistId': playlist_id,
        'key': api_key
    }
    query_string = to_query_string(parameters)
    full_url = f'{url}?{query_string}'

    response = requests.get(full_url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    
    json_data = response.json()
    video_titles = [item['snippet']['title'] for item in json_data.get('items', [])]
    
    return video_titles


playlist_id = ''  # Replace with your playlist ID
api_key = ''  # Replace with your YouTube Data API key

title_data = get_playlist_data(playlist_id, api_key)


