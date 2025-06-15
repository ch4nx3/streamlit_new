import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # Windows (Malgun Gothic)
font = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font.get_name()  # 전역 폰트 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# SM Entertainment 블로그
st.title("SM Entertainment  😊")
st.markdown("**SM Entertainment**는 K-Pop을 세계로 알린 대표적인 엔터테인먼트 회사임. 1995년에 설립되어 글로벌 팬덤을 이끌고 있음.")
st.divider()

st.header("SM의 비전 🌟")
st.markdown("""
SM은 "The Culture, The Future"를 목표로 함:
- K-Pop을 전 세계로 확산
- 음악, 공연 등 새로운 콘텐츠 개발
- 다양한 아티스트를 키우는 다중 레이블 전략
""")
st.info("SM은 글로벌 엔터테인먼트의 미래를 만들어감!", icon="ℹ️")
st.divider()

st.header("SM의 기업 문화 💼")
st.markdown("""
SM은 창의적이고 협력적인 문화를 자랑함:
- 아티스트와 직원이 자유롭게 아이디어를 공유
- 일본, 중국 등 해외와 협업
- 팬들과 소통하는 DearU 플랫폼 운영
- 하지만 최근 아티스트 관리 문제로 비판받았음.
""")
st.warning("최근 내부 문제로 논란이 있었음.", icon="⚠️")
st.divider()

st.header("SM의 대표 아티스트 🎤")
st.markdown("""
SM은 다양한 K-Pop 스타를 보유하고 있음:
- **H.O.T.**: K-Pop의 시작을 알린 전설
- **BoA**: 아시아를 대표하는 솔로 가수
- **Girls' Generation**: 글로벌 팬덤의 아이콘
- **EXO**: 강력한 퍼포먼스
- **NCT**: 독특한 유닛 시스템
- **aespa**: 메타버스 콘셉트
- **Hearts2Hearts**: 2025년 데뷔 신인
""")
st.image('images/aespa.jpg', caption='aespa')
st.subheader("앨범 판매량 그래프 📊")
artists = ["NCT", "aespa", "EXO", "Girls' Generation"]
sales = [420, 200, 150, 10]  # 실제 데이터 (만 장)
fig, ax = plt.subplots()
ax.bar(artists, sales, color='lightpink')
ax.set_title("SM 아티스트 앨범 판매량 (만 장)")
ax.set_ylabel("판매량")
st.pyplot(fig)
st.divider()

st.header("SM의 재무 성과 💰")
st.markdown("""
2025년 4월 기준 SM의 성과:
- **매출**: $0.71B
- **시가총액**: $2.22B
""")
st.subheader("매출 구성 그래프 📈")
revenue_sources = ["콘서트", "음원", "드라마/기타", "머천다이징"]
revenue_share = [35, 25, 20, 20]  # 실제 데이터 (%)
fig, ax = plt.subplots()
ax.pie(revenue_share, labels=revenue_sources, autopct='%1.1f%%', colors=['lightcoral', 'skyblue', 'lightgreen', 'gold'])
ax.set_title("2025년 SM 매출 구성")
st.pyplot(fig)
st.divider()

st.header("SM의 최신 소식 📰")
st.markdown("""
2025년 SM의 주요 뉴스:
- 텐센트가 SM의 2대 주주로 참여
- GREAT M Entertainment 투자로 레이블 확장
- SM 30주년 기념 콘서트와 앨범 발매
- 아티스트 관리와 리더십 문제로 논란
""")
st.success("SM 30주년 축하함!", icon="🎉")
st.divider()

st.header("SM의 강점 🏆")
st.markdown("""
SM이 강한 이유:
- 30년간 쌓은 K-Pop 경험과 IP
- 일본, 중국 등 글로벌 네트워크
- NCT, aespa의 독창적 콘셉트
- 팬과 소통하는 DearU 플랫폼
""")
st.divider()
st.caption("2025년 6월 | SM Entertainment ")

# HYBE Entertainment 블로그
st.title("HYBE Entertainment  😊")
st.markdown("**HYBE**는 BTS를 중심으로 K-Pop을 글로벌 무대로 확대한 엔터테인먼트 리더임. 2005년에 설립된 Big Hit Entertainment가 전신임.")
st.divider()

st.header("HYBE의 비전 🌟")
st.markdown("""
HYBE는 "We Believe in Music"을 모토로 음악을 통해 사람을 연결함:
- 글로벌 음악 시장에서 혁신적인 콘텐츠 제공
- 아티스트와 팬을 연결하는 플랫폼(WeVerse) 강화
- 다중 레이블 전략으로 다양한 음악 장르 확장
""")
st.info("HYBE는 음악으로 세대를 이어감!", icon="ℹ️")
st.divider()

st.header("HYBE의 기업 문화 💼")
st.markdown("""
HYBE는 창의성과 글로벌 협업을 중시함:
- 아티스트의 창의적 자유를 보장
- 미국, 일본, 중국 등 글로벌 지사와 협업
- 팬 중심의 WeVerse와 같은 혁신적 플랫폼 운영
- 하지만 최근 내부 갈등과 법적 논란으로 비판받았음.
""")
st.warning("최근 경영진 논란으로 주목받고 있음.", icon="⚠️")
st.divider()

st.header("HYBE의 대표 아티스트 🎤")
st.markdown("""
HYBE는 세계적인 K-Pop 스타를 보유하고 있음:
- **BTS**: 글로벌 K-Pop의 아이콘
- **TOMORROW X TOGETHER**: 차세대 리더
- **SEVENTEEN**: 퍼포먼스 강자
- **ILLIT**: 독창적 스타일로 주목
- **LE SSERAFIM**: 글로벌 팬덤 확장
- **aeon**: 2025년 6월 데뷔한 J-Pop 보이그룹
""")
st.image('images/illit.jpg', caption='illit')
st.subheader("앨범 판매량 그래프 📊")
artists = ["BTS", "NewJeans", "SEVENTEEN", "TXT"]
sales = [300, 250, 500, 200]  # 실제 데이터 (만 장)
fig, ax = plt.subplots()
ax.bar(artists, sales, color='lightblue')
ax.set_title("HYBE 아티스트 앨범 판매량 (만 장)")
ax.set_ylabel("판매량")
st.pyplot(fig)
st.divider()

st.header("HYBE의 재무 성과 💰")
st.markdown("""
2025년 5월 기준 HYBE의 성과:
- **매출**: $1.63B
- **시가총액**: $9.38B
""")
st.subheader("매출 구성 그래프 📈")
revenue_sources = ["콘서트", "음원", "머천다이징", "기타"]
revenue_share = [40, 20, 30, 10]  # 실제 데이터 (%)
fig, ax = plt.subplots()
ax.pie(revenue_share, labels=revenue_sources, autopct='%1.1f%%', colors=['lightcoral', 'skyblue', 'lightgreen', 'gold'])
ax.set_title("2025년 HYBE 매출 구성")
st.pyplot(fig)
st.divider()

st.header("HYBE의 최신 소식 📰")
st.markdown("""
2025년 HYBE의 주요 뉴스:
- BTS 전원 군 복무 완료, 'We Are Back' 캠페인 시작
- 중국 진출: 베이징 사무소 오픈
- SM 지분 매각: 텐센트에 9.38% 지분 1770억 원에 매각
- 논란: 방시혁 회장 주식 거래 조사 및 NewJeans와 법적 분쟁
""")
st.success("BTS 재결합 축하함!", icon="🎉")
st.divider()

st.header("HYBE의 강점 🏆")
st.markdown("""
HYBE가 강한 이유:
- BTS를 통한 글로벌 브랜드 파워
- WeVerse와 같은 팬 플랫폼으로 팬덤 강화
- 다중 레이블(BIGHIT MUSIC, Pledis 등) 운영
- 미국, 일본, 중국 등 글로벌 시장 확장
""")
st.divider()
st.caption("2025년 6월 |  HYBE Entertainment ")

# JYP Entertainment 블로그
st.title("JYP Entertainment  😊")
st.markdown("**JYP Entertainment**는 TWICE, Stray Kids 등 글로벌 K-Pop 스타를 배출한 선도적인 엔터테인먼트 회사임. 1997년에 박진영 대표가 설립했음.")
st.divider()

st.header("JYP의 비전 🌟")
st.markdown("""
JYP는 '음악으로 세상을 행복하게'라는 비전을 추구함:
- 글로벌 K-Pop 시장에서 창의적 콘텐츠 제공
- 아티스트와 팬을 연결하는 JYP FANS 플랫폼 운영
- 지속 가능한 성장과 ESG(환경, 사회, 지배구조) 전략 강화
""")
st.info("JYP는 음악으로 행복을 전함!", icon="ℹ️")
st.divider()

st.header("JYP의 기업 문화 💼")
st.markdown("""
JYP는 아티스트 중심의 창의적 문화를 강조함:
- 아티스트의 개성과 창의성을 존중
- 글로벌 시장(한국, 일본, 미국)과의 협업
- 팬 중심의 소통 플랫폼 JYP FANS 운영
- 하지만 최근 VCHA 멤버 계약 분쟁으로 논란 발생했음.
""")
st.warning("최근 아티스트 계약 문제로 논란이 있었음.", icon="⚠️")
st.divider()

st.header("JYP의 대표 아티스트 🎤")
st.markdown("""
JYP는 다양한 K-Pop 스타를 보유하고 있음:
- **TWICE**: 글로벌 걸그룹의 대표주자
- **Stray Kids**: 강렬한 퍼포먼스와 자작곡
- **ITZY**: 독창적 스타일로 주목
- **NMIXX**: 새로운 세대의 리더
- **DAY6**: 밴드 음악의 선구자
- **NEXZ**: 2023년 데뷔한 글로벌 보이그룹
""")
st.image('images/twice.jpg', caption='twice')
st.subheader("앨범 판매량 그래프 📊")
artists = ["TWICE", "Stray Kids", "ITZY", "NMIXX"]
sales = [200, 350, 100, 80]  # 실제 데이터 (만 장)
fig, ax = plt.subplots()
ax.bar(artists, sales, color='lightgreen')
ax.set_title("JYP 아티스트 앨범 판매량 (만 장)")
ax.set_ylabel("판매량")
st.pyplot(fig)
st.divider()

st.header("JYP의 재무 성과 💰")
st.markdown("""
2025년 6월 기준 JYP의 성과:
- **매출**: $0.43B
- **시가총액**: $1.86B
""")
st.subheader("매출 구성 그래프 📈")
revenue_sources = ["앨범", "콘서트", "머천다이징", "기타"]
revenue_share = [45, 30, 15, 10]  # 실제 데이터 (%)
fig, ax = plt.subplots()
ax.pie(revenue_share, labels=revenue_sources, autopct='%1.1f%%', colors=['lightcoral', 'skyblue', 'lightgreen', 'gold'])
ax.set_title("2025년 JYP 매출 구성")
st.pyplot(fig)
st.divider()

st.header("JYP의 최신 소식 📰")
st.markdown("""
2025년 JYP의 주요 뉴스:
- TWICE, Lollapalooza Chicago 2025 헤드라이너 확정
- Stray Kids, 32회 글로벌 콘서트 투어 진행
- VCHA 멤버 KG 계약 종료 및 소송, 노동 착취 논란
- 중국 시장 재진출, 베이징 사무소 설립
""")
st.success("JYP 아티스트의 글로벌 활약을 응원함!", icon="🎉")
st.divider()

st.header("JYP의 강점 🏆")
st.markdown("""
JYP가 강한 이유:
- TWICE, Stray Kids 등 강력한 아티스트 IP
- 글로벌 시장(일본, 미국)에서의 높은 인지도
- JYP FANS 플랫폼으로 팬덤 강화
- 지속 가능한 ESG 전략과 콘텐츠 다각화
""")
st.divider()
st.caption("2025년 6월 | JYP Entertainment ")
