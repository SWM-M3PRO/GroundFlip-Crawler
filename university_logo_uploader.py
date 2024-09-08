import pymysql
import requests
import boto3
from botocore.config import Config
from botocore.exceptions import NoCredentialsError

def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="",
            aws_secret_access_key="",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3

def download_image(image_url, save_path):
    # URL로부터 이미지 데이터를 가져옴
    response = requests.get(image_url)

    # 정상적으로 이미지를 가져왔는지 확인
    if response.status_code == 200:
        # 파일 쓰기 모드로 이미지 저장
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"이미지가 성공적으로 저장되었습니다: {save_path}")
    else:
        print(f"이미지를 다운로드하는 중 문제가 발생했습니다. 상태 코드: {response.status_code}")


# MySQL 연결 정보 설정
connection = pymysql.connect(
    host='',      # MySQL 서버 주소
    user='',  # MySQL 사용자 이름
    password='',  # MySQL 비밀번호
    database='',  # 사용할 데이터베이스
    cursorclass=pymysql.cursors.DictCursor  # 결과를 딕셔너리로 받기 위한 설정
)

s3 = s3_connection()

try:
    with connection.cursor() as cursor:
        # 텍스트 파일 열기
        with open('university_details_list.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # 각 줄을 콤마(,)로 분리
                row = line.strip().split(',')

                # 이미지를 다운로드
                # 파일명 변경
                try:
                    download_image(row[2], "logo/" + row[0] + ".svg")
                except:
                    print(row[0])
                    print('다운 불가')

                # s3 업로드
                try:
                    s3.upload_file("logo/" + row[0] + ".svg", "ground-flip-s3", "university_logo/" + row[0] + ".svg")
                except FileNotFoundError:
                    print(row[0])
                except NoCredentialsError:
                    print(row[0])
                    print("AWS 자격 증명을 찾을 수 없습니다.")
                # sql update

                sql = """
                UPDATE community
                SET background_image_url = %s
                WHERE name = %s
                """

                # 동적으로 삽입할 URL 생성
                background_image_url = f"https://ground-flip-s3.s3.ap-northeast-2.amazonaws.com//{row[0]}.svg"

                # 쿼리 실행 (파라미터 바인딩 사용)
                cursor.execute(sql, (background_image_url, row[0]))

        # 트랜잭션 커밋
        connection.commit()

finally:
    connection.close()