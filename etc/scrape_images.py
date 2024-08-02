"""
Selenium must be installed to use this module.
To install selenium, Enter this command to the terminal:
pip install selenium
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from google_images_download import google_images_download


response = google_images_download.googleimagesdownload()
spr_keywords = ["수지", "로제", "박민영", "임소향", "아이유", "배우 한혜진", "모델 한혜진", "윤아", "아이린", "조보아", "김유정", "유인나", "조이", "제시카", "김세정"]
smr_keywords = ["손예진", "김고은", "장원영", "강소라", "문소리", "문채연", "김연아", "안유진", "박민영", "정채연", "아린", "나연", "김태리", "다현", "모모"]
fll_keywords = ["천우희", "이효리", "탕웨이", "하지원", "제니", "하정우", "현아", "고아라", "신세경", "한효주", "박신애", "하연수", "쯔위", "미나", "정연"]
wnt_keywords = ["서지혜", "채영", "지효", "임시완", "현빈", "서지수", "남궁민", "한가인", "이나영", "전지현", "설현", "이영애", "김혜수", "차승원", "윤두준"]

d = {"fall": fll_keywords, "spring": spr_keywords, "summer": smr_keywords, "winter": wnt_keywords}

for k, v in d.items():
    for i in v:
        arguments = {
            "keywords": i + "기사사진",
            "limit": 100,
            "print_urls": True,
            "format": "jpg",
            "output_directory": "../../../OneDrive/ColorUs_Project/",
            "image_directory": k
        }
        paths = response.download(arguments)


def download_images(image, path, file):
    new_path = path

    if file.find("가을딥") > -1:
        new_path += "fall_dark/"
    elif file.find("가을뮤트") > -1:
        new_path += "fall_mute/"
    elif file.find("봄라이트") > -1:
        new_path += "spring_bright/"
    elif file.find("봄브라이트") > -1:
        new_path += "spring_light/"
    elif file.find("여름라이트") > -1:
        new_path += "summer_light/"
    elif file.find("여름뮤트") > -1:
        new_path += "summer_mute/"
    elif file.find("겨울브라이트") > -1:
        new_path += "winter_bright/"
    elif file.find("겨울딥") > -1:
        new_path += "winter_dark/"

    image.screenshot(new_path + file)


def scrape_images(driver, link):
    driver.get(link)

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "se-component"))
    )

    # Get all components in order
    components = driver.find_elements(
        By.CSS_SELECTOR, ".se-main-container .se-component"
    )

    # Get all relevant texts in order
    text_elements = driver.find_elements(
        By.CSS_SELECTOR, ".se-main-container .se-text-paragraph span"
    )

    # Remove empty texts
    filtered_texts = list(
        filter(
            lambda x: len(x.get_attribute("innerHTML")) > 1,
            text_elements,
        )
    )

    # Remove white spaces
    texts = list(
        map(lambda x: x.get_attribute("innerHTML").replace(" ", ""), filtered_texts)
    )

    image_count = 1  # count image to name the image file
    text_count = 0  # index used for texts
    for component in components:
        class_name = component.get_attribute("class")
        if class_name.find("se-imageStrip") > -1 or class_name.find("se-image") > -1:
            # If the component contains images
            images = component.find_elements(By.TAG_NAME, "img")
            for image in images:
                # Download image
                path = "/Users/shawnrim/Desktop/Projects/ColorUs/src/"
                file_name = f"{texts[text_count]}{image_count}.png"

                download_images(image, path, file_name)

                image_count += 1
        else:
            # If the component contains texts
            image_count = 1
            text_count += 1


def main():
    url = "https://m.blog.naver.com/danceslowly?categoryNo=9&tab=1"

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Scroll down after awaiting for elements to load for few seconds to load more elements
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "link__Awlz5"))
    )
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "link__Awlz5"))
    )

    post_links = driver.find_elements(By.CLASS_NAME, "link__Awlz5")

    source_links = set()

    for link in post_links:
        if link.get_attribute("innerHTML").find("연예인 퍼스널컬러 모음") > -1:
            source_links.add(link.get_attribute("href"))

    for href in source_links:
        scrape_images(driver, href)


if __name__ == "__main__":
    main()
