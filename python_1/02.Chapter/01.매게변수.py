#1. 위치 매게변수

#가장 기본적인 매게변수
def my_func(a, b):
    print(a,b)

my_func(2,3)

#2.기본 매게변수
def post_info(title, content = '내용없음'):
    print('제목 :', title)
    print('내용 :',content )

post_info("출석")

def post_info(title, content):
    print('제목 :', title)
    print('내용 :',content )

post_info(content="출석",title = '오늘')