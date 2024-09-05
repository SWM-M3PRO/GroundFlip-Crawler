from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver 경로 설정 (본인이 설치한 경로로 수정)
chrome_driver_path = "/Users/minuk/Desktop/SWM/GroundFlip-BE-Crawler/GroundFlip-BE-Crawler/chromedriver-mac-arm64/chromedriver"

# 브라우저 열기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98%20%EB%8C%80%ED%95%99%EA%B5%90%20%EB%AA%A9%EB%A1%9D"

driver.get(url)

# ul 요소를 CSS 셀렉터로 찾기d
select_list = ["#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(7) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(9) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(11) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(13) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(15) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(17) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(23) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(25) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               "#app > div._17s0-GlA.a3yv20wk > div.XhNDx51d.FXgnxt9K > div > div.Nnp2k2UW > div > div.O7Sh7taf.fy2iB5u6 > div.uK3Apzs7.zRn852xP > div:nth-child(29) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > ul",
               ]
# 결과를 저장할 리스트
results = []

for selector in select_list:
    ul_element = driver.find_element(By.CSS_SELECTOR, selector)

    # ul 안의 li > div > a 요소들 찾기
    a_elements = ul_element.find_elements(By.CSS_SELECTOR, "li > div > a")


    # 각 a 요소에서 href와 title 추출
    for a in a_elements:
        href = a.get_attribute("href")
        title = a.get_attribute("title")
        if href and title:
            results.append(f"{href},{title}")


# 브라우저 종료
driver.quit()

# 결과를 텍스트 파일에 저장
with open("university_list.txt", "w", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")

