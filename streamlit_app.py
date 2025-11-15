import streamlit as st

st.title("오늘의 기분 명언")
st.write("오늘 하루 당신의 기분을 알려주세요!")

# 기분별 명언 데이터
quotes = {
    "걱정": "걱정은 미래의 고통을 두 번 맛보는 것이다. 현재에 집중하면 모든 것이 잘될 것이다.",
    "화남": "분노는 우리의 적을 무너뜨리는 것보다 우리 자신을 더 해친다. 차분함을 찾아보세요.",
    "평온": "독서할 때 당신은 항상 가장 좋은 친구와 함께 있다.",
    "기쁨": "기쁨은 인생의 최고의 선물이다. 이 순간을 소중히 여기고 나누어보세요.",
    "만족": "만족은 진정한 부의 근원이다. 가지고 있는 것에 감사하는 마음이 행복을 만든다."
}

# 기분 버튼 생성
st.subheader("당신의 기분을 선택하세요")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("😟 걱정"):
        st.success(quotes["걱정"])

with col2:
    if st.button("😠 화남"):
        st.warning(quotes["화남"])

with col3:
    if st.button("😌 평온"):
        st.info(quotes["평온"])

with col4:
    if st.button("😊 기쁨"):
        st.success(quotes["기쁨"])

with col5:
    if st.button("😄 만족"):
        st.success(quotes["만족"])
