#내가 푼 스타일
# a=[]
# with open('ssafy.txt','r') as f:
#     lines = f.readlines() # 각 라인을 item으로 list 의 형태로 반환
#     for line in lines :
#         a += line.strip()
# print(len(a))
# b = []
# with open('reversed_ssafy.txt','w') as ff: 
#     for i in range(len(a)) :
#         ff.write(f"{a[len(a)-(i+1)]}\n") a 대신 lines를 쓰면 된거였어!!!

#강사님의 해답
with open('ssafy.txt','r') as f:
    lines = f.readlines() # 각 라인을 item으로 list 의 형태로 반환

lines.reverse()

with open('reversed_ssafy.txt','w') as f: 
    for line in lines :
        f.write(line)