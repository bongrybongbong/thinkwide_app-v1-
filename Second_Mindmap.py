import numpy as np
import pandas as pd
import streamlit as st
import datetime
import json
from pyvis.network import Network
from streamlit_markmap import markmap
from page_utils import styled_hashtag, styled_text, render_markdown
from data.second_data import name, meeting_data, data

from datetime import datetime
from PIL import Image
import streamlit as st




# 현재 날짜와 시간을 문자열로 포맷팅
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

# Streamlit 페이지에 제목과 날짜/시간을 추가

st.set_page_config(page_title="markmap", layout="wide")

markdown_content = render_markdown(data)


st.header('🫧 {0}님의 두 번째 마인드맵 :  일본 여행 계획 세우기💡'.format(name))

st.markdown("""---""")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('🪐일본 여행')
    st.markdown('**일시 :** 2022년 11월 10일 오후 6:50')
    st.markdown('**유형 :** 주간 회의')
    st.markdown('**참석자 :** 🧙🏼‍♀️봉그리봉봉님, 👨🏼‍🌾김제니님')
    st.markdown('**회의 요약**')
    st.markdown('일본 여행의 모든 것: 봉남과 제니의 철저한 준비와 설렘 가득한 계획을 세웠어요! :sparkles:')

with col2:
    st.subheader('🪐핵심 키워드')
    hashtags = ["여행 일정", "관광 계획", "#음식 및 식당"]
    colors = ["#FF6B6B", "#6BCB77","#F7B801"]
    for tag, color in zip(hashtags, colors):
        styled_hashtag(tag, color)

with col3:
    st.subheader('🪐추가적인 무언가')
    video_file = open(r'C:\CODE\thinkwide_app-main\img\sample_video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


st.markdown("""---""")
with open(r'C:\CODE\thinkwide_app-main\data\structured_markdown_data2.md', encoding='utf-8') as fp:
    md = fp.read()
markmap(md,height=400)



tab1, tab2, tab3 = st.tabs(["MINDMAP-NODE🫧", "키워드분석📈", "회의분석📊"])

with tab1:
    st.markdown('')
    st.markdown(markdown_content, unsafe_allow_html=True)



with tab2:
    st.markdown(f'#### 가장 많이 언급된 단어에요!')
    st.write("  ")
    st.markdown('🥇 일본')
    st.markdown('🥈 고툐')
    st.markdown('🥉 맛있는 거')


with tab3:
    st.title("일본 여행 계획의 모든 것")
    st.markdown(meeting_data)

