import os

os.chdir(r'C:\Users\student\TIL\startCamp\02_day') #500개의 지원서가 있는 곳으로 디렉토리를 바꿔야 합니다. r 뒤에 디렉토리를 입력해야합니다. 
# 어디에서 이 파이썬 파일을 실행하더라도 디렉토리를 02_day로 옮겨가서 실행하라라는 뜻

filenames = os.listdir('.') #.은 현재 디렉토리입니다. listdir은 모든 파일의 이름을 불러오세요 라는 함수입니다.

#앞에 삼성을 붙여라
# for filename in filenames :
#     #확장자가 .txt인 파일만 이름을 바꾼다.
#     extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리
#     if extension == '.txt' :
#         os.rename(filename, f'SAMSUNG_{filename}') # 첫번째 인자로 넘어간 이름을 두번째 인자로 넘어간 이름으로 바꾼다.

#삼성을 싸피로 바꾸라
for filename in filenames :
    #확장자가 .txt인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리
    if extension == '.txt' :
        
        os.rename(filename, filename.replace('SAMSUNG_','SSAFY_')) #replace(a,b) a를 b로 바꾼다
        