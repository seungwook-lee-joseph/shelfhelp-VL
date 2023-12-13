input_file = '/Users/seungwooklee/Documents/shelfhelp-VL/item2.txt'  # 원본 파일 경로
output_file = '/Users/seungwooklee/Documents/shelfhelp-VL/label_item2.txt'  # 라벨과 URL을 저장할 파일 경로

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        line = line.strip()  # 줄바꿈 제거
        parts = line.split('/')  # URL을 '/' 기준으로 분리
        label = parts[-3]  # 끝에서 두 번째 부분이 라벨
        outfile.write(f'{label}|{line}\n')  # 라벨과 URL을 파일에 쓰기

print("라벨 추출 및 저장이 완료되었습니다.")

