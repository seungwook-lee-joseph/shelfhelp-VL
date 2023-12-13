# 파일 경로
input_file = '/Users/seungwooklee/Documents/shelfhelp-VL/output.txt'  # 원본 파일 경로
output_file = '/Users/seungwooklee/Documents/shelfhelp-VL/modified_output.txt'  # 수정된 경로를 저장할 파일 경로

# 변경할 경로
old_path = '/Users/seungwooklee/Documents/'
new_path = 'https://raw.githubusercontent.com/seungwook-lee-joseph/'

# 파일 읽기 및 쓰기
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # 경로 변경
        modified_line = line.replace(old_path, new_path)
        # 변경된 경로를 새 파일에 쓰기
        outfile.write(modified_line)

print("경로 변경이 완료되었습니다.")

