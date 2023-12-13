import os

directory = '/Users/seungwooklee/Documents/shelfhelp-VL/grocery_images'  # 대상 디렉토리 경로
output_file = '/Users/seungwooklee/Documents/shelfhelp-VL/output.txt'    # 결과를 저장할 파일 경로

with open(output_file, 'w') as file:
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            file.write(file_path + '\n')

