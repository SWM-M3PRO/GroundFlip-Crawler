from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
# ChromeDriver 경로 설정 (본인이 설치한 경로로 수정)
chrome_driver_path = "/Users/minuk/Desktop/SWM/GroundFlip-BE-Crawler/GroundFlip-BE-Crawler/chromedriver-mac-arm64/chromedriver"

results = []

university_list_lines = open('university_list.txt', 'r').readlines()
university_detail_file = open('university_details_list.txt', 'a')
driver = None

def rgb_to_hex(rgb_string):
    # 'rgb(0, 78, 150)'에서 숫자 부분만 추출
    rgb_values = re.findall(r'\d+', rgb_string)
    r, g, b = map(int, rgb_values)

    # 각각의 RGB 값을 16진수로 변환하여 #RRGGBB 형태로 반환
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

for line in university_list_lines:
    url = line.split(",")[0]

    # 브라우저 열기
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)

    university_detail_element = driver.find_element(By.CSS_SELECTOR, "div.D\\+GR2Ia1.zRAeL4pd")
    style_attribute = university_detail_element.find_element(By.CSS_SELECTOR, "table > tbody > tr:nth-child(1) > td").get_attribute("style")
    background_color = None


    if "background" in style_attribute:
        print(style_attribute)
        style_attributes = style_attribute.split(";")
    
        for attr in style_attributes:
            if "background-color" in attr:
                # background-color 값 추출
                background_color = attr.split(":")[1].strip()
    
                # RGB 값인 경우 HEX로 변환
                if "rgb" in background_color:
                    background_color = rgb_to_hex(background_color)

    strong_elements = university_detail_element.find_elements(By.TAG_NAME, "strong")
    # 한글만 확인하는 정규 표현식
    hangul_pattern = re.compile(r'^[가-힣]+$')

    # 한글이 있는 strong 태그의 텍스트를 name 변수에 할당
    name = None
    for strong in strong_elements:
        text = strong.text.strip()
        if hangul_pattern.match(text):
            name = text
            break  # 첫 번째 한글 텍스트를 찾으면 루프 종료

    img_element = None
    try:
        img_element = university_detail_element.find_element(By.CSS_SELECTOR, "img.BlUYu1D9")
        img_src = img_element.get_attribute("src")
    except:
        img_src = 'error'
        print(name)

    # src 속성 가져오기
    university_detail_file.write(f"{name},{background_color},{img_src}\n")

driver.quit()