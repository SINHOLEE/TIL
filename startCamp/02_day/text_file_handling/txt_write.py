#open('ssafy.txt',) #파일을 열어주세요. ('파일명', '모드')
# 열기모드
# r: 읽기 , w: 쓰기(write -오버라이트), a: 추가(append)
# f = open('ssafy.txt','w')

# for i in range(10):
#     f.write(f'this is line{i+1} \n')
# f.close() # 다 작업한 다음 무조건 써야합니다.

# with open('with_ssafy.txt','w') as f:# 컨텍스트 매니저라는 친구 - 작업하는 코드 블럭을 생성해준다?
#     # as f의 뜻은 with를 사용할때는 f=open 변수할당을 못하기 떄문에 f라고 할당했다고 생각하자.
#     for i in range(10) : 
#         f.write(f'this is line{1+i} \n') 

#한번에 for문을 작성하는 방법
with open('ssafy.txt','w',encoding='utf-8') as f :
    f.writelines(['0\n','1\n','2\n', '3\n'])