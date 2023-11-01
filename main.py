import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon='👻'
)

menu = st.sidebar.selectbox('menu',['로그인','자기소개','선택과목 조사','기타'])

if menu == '자기소개':
    st.title('자기소개')
    st.video('https://www.youtube.com/watch?v=nuM0Z4a7kMs')
elif menu == ('선택과목 조사'):

    st.subheader('선택과목조사')
    st.caption('4가지를 선택하세요')


    세계사 = st.checkbox('세계사')
    세계지리 = st.checkbox('세계지리')
    윤리와사상 = st.checkbox('윤리와사상')
    정치와법 = st.checkbox('정치와법')
    물리학 = st.checkbox('물리학')
    지구과학 = st.checkbox('지구과학')
    생명과학 = st.checkbox('생명과학')
    화학 = st.checkbox('화학')

    a = ''
    cnt = 0
    if 세계사:
        a = a+('세계사,')
        cnt+=1
    if 세계지리:
        a = a+('세계지리,')
        cnt+=1
    if 윤리와사상 :
        a = a+('윤리와사상,')
        cnt+=1
    if 정치와법:
        a = a+('정치와법,')
        cnt+=1
    if 물리학:
        a = a+('물리학,')
        cnt+=1
    if 지구과학:
        a = a+('지구과학,')
        cnt+=1
    if 생명과학:
        a = a+('생명과학,')
        cnt+=1
    if 화학:
        a = a+('화학')
        cnt+=1
    if cnt>=5:
        st.write("4개만 선택하세요")
    else:
        st.write(a + '을 선택하셨습니다')
    st.subheader('수학or영어')

    선택과목 = st.radio('둘중하나를 선택하세요',['기하학', '진로영어'])
    st.write('당신이 택한 선택과목은 '+선택과목+'입니다.')
    선택과목 = st.radio('둘중하나를 선택하세요',['확률과통계', '영어권문화'])
    st.write('당신이 택한 선택과목은 '+선택과목+'입니다.')
    st.caption('둘다 영어를 택할경우 3학년에 기하학이 필수입니다')


    st.subheader('외국어 선택')
    selectsubject = st.multiselect(
        '2개를 선택하세요',
        ['중국어','한문','일본어']
    )
    st.write(selectsubject)
    st.subheader('최종선택과목')
    finalsubject = st.multiselect('최종선택과목확인',
    ['생물','물리','화학','지구과학','세계지리','세계사','정치와법','윤리화사상','기하학','진로영어','확률과통계','영어권문화','중국어','한문','일본어'])
    st.write(finalsubject)
    st.caption('총7개를 택하여야 합니다.')

    btn = st.button('제출')
    if btn:
        st.write('제출이 완료 되었습니다 감사합니다.')
        link_btn = st.link_button('나가기',"https://naver.com")

    st.image('lion.png')
elif menu == '기타':
    st.title('기타')
elif menu == '로그인':
    st.title('로그인🐺')
    id = st.text_input('아이디', placeholder='아이디를 입력하세요.')
    pw = st.text_input('비밀번호', type='password', placeholder='비밀번호를 입력하세요')
    login = st.button('로그인')
    if login:
        if id == 'test123' and pw == 'qwer1234':
            st.write('로그인 성공')
            st.balloons()
        else:
            st.write(':red[로그인 실패]')


# 짜장면 = st.checkbox('짜장면')
# 탕수육 = st.checkbox('탕수육')
# 짬뽕 = st.checkbox('짬뽕')
# a = ''
# if 짜장면:
#     a = a+' 짜장면 '
# if 탕수육:
#     a = a+' 탕수육'
# if 짬뽕:
#     a = a+' 짬뽕 '
# st.write(a + '을 선택하셨습니다')


# 성별 = st.radio('당신의 성별은?',['남자', '여자'])
# st.write('당신의 성별은 '+성별+'입니다.')

# email = st.selectbox(
#     'E-mail을 선택하세요',
#     ['gmail.com', 'naver.com', 'hanmail.com']
# )

# food = st.multiselect(
#     '당신이 좋아하는 음식은?',
#     ['피자','햄버거','삶은계란','파스타','보쌈']
# )
# st.write(food)

# st.write('한민규의 홈페이지!!')
# st.subheader('this is subheader')
# st.header('this is header')
# st.title('this is title')
# st.caption('this is caption')
# st.code('x = 10+20')

# btn = st.button('클릭')
# if btn:
#     st.write('버튼 클릭!!!')
# text = '이 버튼을 클릭하면 파일을 다운 받을 수 있습니다'
# download_btn = st.download_button('다운로드',text)
# link_btn = st.link_button('네이버',"https://naver.com")
# link_btn = st.link_button('함지고',"https://hamji.dge.hs.kr/hamjih/main.do?sysId=hamjih")
# link_btn = st.link_button('구글',"https://google.com")

# checkbox = st.checkbox('동의')
# if checkbox:
#     st.write('동의하셨습니다.')