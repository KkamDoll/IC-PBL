# 시작화면 & 종료화면 코드 임포트
from Start_Screen import start_screen
#from End_screen import end_screen

# 경고화면 출력코드 임포트
from Warning_Screen import warning

#시작화면 출력
start_input = start_screen()

#StudentList: 미리 저장된 학생 정보 / 형식: key = 학번, value = [name, email, adult]
StudentList = {'22206425' : ['토끼','mail1',True], '20206243' : ['나비','mail2',True], 
        '20212444' : ['캥거루','mail3',False], '202454544' : ['부엉이','mail4',True]}

#Student_INFO: QR코드로부터 얻은 학생 정보
Student_INFO = "22206425" #고도원이 만들 예정

#Student_login: 로그인 기능 함수
def Student_login():
    global Student_INFO

    while True:
        try: 
            #추후에 qr코드 인식기능 구혀 예정
            if Student_INFO in StudentList: # 1.로그인 정보가 올바른 경우
                Student_Name = StudentList[Student_INFO][0]
                print(f"                    안녕하세요, {Student_Name}님")
                break
        except: # 2.로그인 정보가 올바르지 않은 경우
            print("잘못된 정보 입니다, 다시 입력해주세요.")
            Student_INFO = ""

Student_login()
warning()

def menu():
    pass