import requests, re, json, urllib.request
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
}

queryParameters = {"q": "marvel", "tbm": "isch", "hl": "en", "gl": "us", "ijn": "0" }

target_image_path = ".isv-r.PNCib.MSM1fd.BUooTd"
targetted_image_base_html_path = ".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb"

html = requests.get("https://www.google.com/search", params=queryParameters, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

google_images = []

def scrape_and_download_google_images():
    
    images_data_in_json = convert_image_to_json()

    matched_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', images_data_in_json)

    removed_matched_thumbnails = remove_matched_get_thumbnails(matched_google_image_data=matched_image_data)

    matched_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_thumbnails)

    full_resolution_images = get_resolution_image(matched_resolution_images=matched_resolution_images)
    
    for index, (image_data, image_link) in enumerate(zip(soup.select(target_image_path), full_resolution_images), start=1):
        
        append_image_to_list(image_data=image_data, image_link=image_link)

        print(f'{index}. image started to download')
        
        download_image(image_link=image_link, index=index)
        
        print(f'{index}. image succesfully downloaded')

    print(f'scraped and downloaded images: {google_images}')


def remove_matched_get_thumbnails(matched_google_image_data):
    return re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', "", str(matched_google_image_data))

def get_resolution_image(matched_resolution_images):
    return [
        bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for img in matched_resolution_images
    ]

def convert_image_to_json():
    all_script_tags = soup.select("script")
    images_data = "".join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))
    fixed_images_data = json.dumps(images_data)
    return json.loads(fixed_images_data)

def append_image_to_list(image_data, image_link):
    google_images.append({
            "image_title": image_data.select_one(targetted_image_base_html_path)["title"],
            "image_source_link": image_data.select_one(targetted_image_base_html_path)["href"],
            "image_link": image_link
        })

def download_image(image_link, index):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_link, f'Scraped_Images/Image_{index}.jpg')


scrape_and_download_google_images()
