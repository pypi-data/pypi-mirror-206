import os
import requests
import re
from bs4 import BeautifulSoup
from shttst.processing.audio_to_dataset import AudioToDatasetProcessor

def unique_list(array):
    return list(set(array))

def download_mp3(id, out_dir='/content/chomik/wavs') -> str:
    try:
        os.makedirs(out_dir, exist_ok=True)
        MP3_URL = f"https://chomikuj.pl/Audio.ashx?id={id}&type=2&tp=mp3"
        resp = requests.get(MP3_URL)

        file_path = os.path.join(out_dir, f'{id}.mp3')
        with open(file_path, 'w+b') as fs:
            fs.write(resp.content)

        return file_path
    except Exception as e:
        print(e)
        return None

def get_all_dirs(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    results = soup.find(id="TreeContainer")
    results = results.find_all('a')
    return unique_list([f"https://chomikuj.pl{r['href']}" for r in results])

def get_dir_pages(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    number_of_pages = 1
    result = soup.find(id="galleryView")
    if result:
        result = result.find('div', class_='paginator')
        if result:
            number_of_pages = max([int(r.text) for r in result.find('ul').find_all('li')])
    else:
        result = soup.find(id="listView")
        if result:
            result = result.find('div', class_='paginator')
            if result:
                number_of_pages = max([int(r.text) for r in result.find('ul').find_all('li')])

    return number_of_pages

def get_page_mp3s(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    result = soup.find(id="galleryView")
    if not result:
        result = soup.find(id="listView")
    if result:
        audios = result.find_all('a', class_='downloadAction')
        
        return(unique_list([re.search(r'\d{10}', r['href']).group() for r in audios if '.mp3' in r['href']]))
    
    return []

def download_chomik_dir(url: str, out_dir='/content/chomik/wavs'):
    max_pages = get_dir_pages(url)
    for i in range(max_pages):
        mp3s = get_page_mp3s(f'{url},{i+1}')
        for mp3 in mp3s:
            download_mp3(mp3, out_dir)

def download_all_chomik_dirs(url: str, out_dir='/content/chomik/wavs'):
    chomik_dirs = get_all_dirs(url)
    for dir in chomik_dirs:
        download_chomik_dir(dir, out_dir)

def create_dataset_from_chomik_dir(url: str, keep_not_fine=False, denoise_all=True, use_classifier=True):
    processor = AudioToDatasetProcessor(keep_not_fine, denoise_all, use_classifier)
    mp3s = get_page_mp3s(url)
    for mp3 in mp3s:
        path = download_mp3(mp3)
        if path:
            processor(path, vad_min_silence=1200)
        


if __name__ == '__main__':
    # URL = "https://chomikuj.pl/JuRiWlO/Audiobooki/"
    # download_all_chomik_dirs(URL)

    URL = "https://chomikuj.pl/piotrbobisz/!Ostatnio+Dodane!/Audiobooki/Adam+Ferency*2c+Maja+Jaszewska/Nie+i+tak.+Adam+Ferency+w+rozmowie+z+Maj*c4*85+Jaszewsk*c4*85+(Czyta+Maja+Jaszewska)"
    create_dataset_from_chomik_dir(URL, use_classifier=False)





