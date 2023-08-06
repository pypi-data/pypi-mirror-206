import requests
import json
from bs4 import BeautifulSoup

def find_stats(json_data):
    for key, value in json_data.items():
        if isinstance(value, dict):
            if 'stats' in value:
                return value['stats']
            else:
                stats = find_stats(value)
                if stats is not None:
                    return stats
    return None

def find_author_stats(json_data):
    # print(json_data)
    for key, value in json_data.items():
        if isinstance(value, dict):
            if 'authorStats' in value:
                return value['authorStats']
            else:
                stats = find_author_stats(value)
                if stats is not None:
                    return stats
    return None


def scrape_tiktok_video_data(url):
    if (url.find('https://') == -1):
        url = "https://" + url
    # Send GET request to URL
    response = requests.get(url)

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract JSON data from #SIGI_STATE element
    sigi_state = soup.find('script', id='SIGI_STATE', type='application/json')
    json_data = json.loads(sigi_state.string)

    # Find the stats object
    stats = find_stats(json_data)

    # Extract number of likes, shares, views, comments, and collects
    likes = stats['diggCount']
    shares = stats['shareCount']
    views = stats['playCount']
    comments = stats['commentCount']
    collects = stats['collectCount']

    # Return results as dictionary
    results = {
        'likes': likes,
        'shares': shares,
        'views': views,
        'comments': comments,
        'collects': collects
    }
    return results

def scrape_tiktok_user_data(url):
    # Send GET request to URL
    if (url.find('https://') == -1):
        url = "https://" + url
    response = requests.get(url)

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract JSON data from #SIGI_STATE element
    sigi_state = soup.find('script', id='SIGI_STATE', type='application/json')
    json_data = json.loads(sigi_state.string)
    # Find the stats object
    # print(json_data)
    stats = find_author_stats(json_data)
    print(stats)
    # Extract user data from JSON

    # Extract number of following and total likes
    #diggCount is a metric on TikTok that represents the number of times a users video has been "liked" or "dug" by other users. It is similar to the "like" count on other social media platforms. The term "digg" comes from the name of the feature on TikTok that allows users to show their appreciation for a video by tapping on the screen. The number of digs that a video receives is reflected in its digg count.
    following = stats['followingCount']
    total_likes = stats['heartCount']
    followers = stats['followerCount']
    total_videos = stats['videoCount']
    total_diggs = stats['diggCount']


    # Return results as dictionary
    results = {
        'following': following,
        'total_likes': total_likes,
        'followers':followers,
        'total_videos':total_videos,
        'total_diggs':total_diggs
        }
    return results
