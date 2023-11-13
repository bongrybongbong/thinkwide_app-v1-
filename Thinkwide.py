from typing import List
import streamlit as st
from markdownlit import mdlit
from streamlit_pills import pills
from streamlit_extras.switch_page_button import switch_page
from data.pages_mt import page_data
from page_utils import chunks
from PIL import Image
from page_utils import styled_hashtag, styled_text
import itertools
from datetime import datetime

# 현재 날짜와 시간을 문자열로 포맷팅
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

def styled_hashtag(tag, color):
    # 해시태그를 HTML 스타일로 스타일링
    return f"<span style='color:{color};'>#{tag}</span>"

colors = ["#FF6B6B", "#6BCB77", "#D65DB1", "#30475E", "#F7B801"]
color_cycle = itertools.cycle(colors)

st.set_page_config("thinkwide's dashboard", "🎪", layout="wide")


# profiler = Profiler()

CATEGORY_NAMES = {
    # Putting this first so people don't miss it. Plus I think's it's one of the most
    # important ones.
    "widgets": "비즈니스 모델",  # 35
    # Visualizations of different data types.
    "charts": "사용자 경험",  # 16
    "image": "UI/UX디자인 ",  # 10
    "video": "여행지 선택",  # 6
    "text": " 운전자 뽑기",  # 12
    "maps": "여행 날짜 맞추기",  # 7
    "dataframe": "강아지 케이크 주문",  # 6
    "science": "초대 손님 ",  # 3
    "graph": "개파티",  # 7
    "3d": "날짜 픽스",  # 1
    "code": "어디로?",  # 4
    # More general elements in the app.
    "navigation": "지겨워",  # 12
    "authentication": "기술 이니셔티브",  # 5
    "style": " IT 프로젝트",  # 3
    # More backend-y/dev stuff.
    # TODO: Should probably split this up, "Developer tools" contains a lot of stuff.
    "development": "시스템 통합",  # 22
    "app-builder": "여행지 선택",  # 3
    # General purpose categories.
    "integrations": "숙소 예약",  # 14
    "collection": "활동 계획",
    "MDO": "더보기...",  # 4
}

CATEGORY_ICONS = [
    "🧰",
    "📊",
    "🌇",
    "🎥",
    "📝",
    "🗺️",
    "🧮",
    "🧬",
    "🪢",
    "🧊",
    "✏️",
    "📃",
    "🔐",
    "🎨",
    "🛠️",
    "🏗️",
    "🔌",
    "📦",
    "➕",
]


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

st.write(
    '<style>button[title="View fullscreen"], h4 a {display: none !important} [data-testid="stImage"] img {border: 1px solid #D6D6D9; border-radius: 3px; height: 200px; object-fit: cover; width: 100%} .block-container img:hover {}</style>',
    unsafe_allow_html=True,
)

icon("🫧")
st.header("봉그리봉봉님의 Thinkwide's World")

description_text = """
봉그리봉봉님, ThinkWide의 세계로 오신 것을 환영합니다! 지난 프로젝트의 경로를 따라 아이디어를 재조명하며 새로운 영감을 발견하세요. 당신의 생각이 총체적인 시각에서 현실로 전환되는 공간, 바로 여기에 준비되어 있습니다.
"""

description = st.empty()
description.write(description_text.format("all"))

col1, col2 = st.columns([2, 1])
search = col1.text_input("Search", placeholder='e.g. "idea" or "내면" or "회의록"')
sorting = col2.selectbox(
    "Sort by", ["⭐️즐겨찾기", "⬇️최신순", "🐣조회순 "]
)

#아이콘, 리스트로 띄우는 것 
category = pills(
    "Category",
    list(CATEGORY_NAMES.keys()),
    CATEGORY_ICONS,
    index=None,
    format_func=lambda x: CATEGORY_NAMES.get(x, x),
    label_visibility="collapsed",
)

# if "screen_width" in st.session_state and st.session_state.screen_width < 768:
st.write("")

if st.button("자세히"):
             switch_page("first mindmap")
st.subheader("⭐️지난 프로젝트")



NUM_COLS = 4
def show_components(page_data, limit=None):
    # 함수 내부 로직...
    components =  list(page_data.values())
    if limit is not None:
        components = components[:limit]
    for i, components_chunk in enumerate(chunks(components, NUM_COLS)):
        cols = st.columns(NUM_COLS, gap="medium")
        for c, col in zip(components_chunk, cols):
            with col:
                image_url = c['img_file']
                image = Image.open(image_url)
                st.image(image,use_column_width=True)
                #st.image(image_url, use_column_width=True)
                title = f"#### {c['title']}"
                st.write(title)
                avatar_path = "https://velog.velcdn.com/images/choonsik_dev/profile/5f77207f-1aa7-433d-9b98-7df99ecf4941/image.jpg"
                namename = "봉봉춘"
                st.caption(f'<img src="{avatar_path}" style="border: 1px solid #D6D6D9; width: 20px; height: 20px; border-radius: 50%"> &nbsp; {namename}',unsafe_allow_html=True,
    )
                st.write(c.get('description'))
                formatted_links = c.get('keywords', [])
                # st.write(" • ".join(formatted_links), unsafe_allow_html=True)
                mdlit(" &nbsp;•&nbsp; ".join(formatted_links))
                st.write("""
                         <div style="display: flex; justify-content: flex-end;">
                         <span style="font-size: small; color: grey; margin-bottom: 10px;">{}</span></div>""".format(current_time), unsafe_allow_html=True)
                st.markdown("""---""")
                st.write("")
                st.write("")
                st.write("")

show_components(page_data)



