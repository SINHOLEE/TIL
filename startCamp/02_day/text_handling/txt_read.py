# f= open('ssafy.txt','r')
# all_text = f.read() # all text 전체를 불러온다(개행 문자 포함)
# print(all_text)
# f.close() # 종료를 꼭 해야 나중에 문제가 안생김

with open('ssafy.txt','r') as f:
    lines = f.readlines()
    for line in lines :
        print(line.strip())