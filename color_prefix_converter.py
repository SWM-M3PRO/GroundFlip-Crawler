# 파일의 내용을 읽고, '#'을 'FF'로 바꾼 후 다시 파일에 저장하는 코드

# 파일 경로 설정
file_path = 'university_details_list.txt'

# 파일 열기 (읽기 모드)
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# '#' 문자를 'FF'로 변환
new_content = content.replace('#', 'FF')

# 변경된 내용을 파일에 다시 쓰기 (쓰기 모드)
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("변경이 완료되었습니다.")