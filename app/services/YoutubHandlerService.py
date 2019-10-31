from bs4 import BeautifulSoup
import requests
import urllib.request



def request_data_from_youtube(url):
    # request dataa from web site
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    plain_text = requests.get(url, headers=headers)
    soup = BeautifulSoup(plain_text.text, 'html.parser')
    # print(soup)
    items = soup.find_all('div', attrs={'class': 'yt-lockup-dismissable'})
    data = []
    for item in items:
        video_url = item.find("a").get('href')
        video_title = item.find('a', {
            'class': 'yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2'}).get('title')
        video_views = item.find('ul', {'class': 'yt-lockup-meta-info'}).find('li').text[0:-6]
        video_duration = item.find('span', {'class': 'video-time'}).text
        img_url = item.find('img').get('src')
        img_path = 'images/' + video_url + '.jpg';
        download_image(img_url, './images/', video_url)
        data.append({'video_url': "https://www.youtube.com/" + video_url,
                     'title': video_title,
                     'views': video_views,
                     'duration': video_duration,
                     'img_url': img_url,
                     'img_path': img_path
                     })
    return data


def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)
