import pymysql

import pymysql

# MySQL 연결 정보 설정
connection = pymysql.connect(
    host='',      # MySQL 서버 주소
    user='',  # MySQL 사용자 이름
    password='',  # MySQL 비밀번호
    database='',  # 사용할 데이터베이스
    cursorclass=pymysql.cursors.DictCursor  # 결과를 딕셔너리로 받기 위한 설정
)

try:
    with connection.cursor() as cursor:
        # 텍스트 파일 열기
        with open('university_details_list.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # 각 줄을 콤마(,)로 분리
                row = line.strip().split(',')

                # INSERT 쿼리 작성 (컬럼 개수에 맞게 조정)
                sql = "INSERT INTO community (name, community_color, background_image_url) VALUES (%s, %s, %s)"
                cursor.execute(sql, (row[0], row[1], row[2]))
        # 트랜잭션 커밋
        connection.commit()

finally:
    connection.close()

print("텍스트 파일 데이터가 MySQL에 성공적으로 삽입되었습니다.")