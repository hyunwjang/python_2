#1. 위치 가변 매게변수(튜플)

def print_frutis(*args):
    for arg in args:
        print(arg)

print_frutis('apple', 'basd','cagsd','adfsdf')

#.2. 키워드 가변 매개변수(딕셔너리)
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

comment_info(name = '파랭이', content = '정말감사합니다.')

# 매개변수 작성 순서
# 위치 -기본- 위치가변 - 키워드(기본) - 키워드 가변

def post_info(title, contnet, *tags):
    print(f'제목 : {title}')
    print(f'내용 : {contnet}')
    print(f'태그 : {tags}')

post_info( '파이썬함수정리', '다양한 매개변수 사용','파이썬', '함수')