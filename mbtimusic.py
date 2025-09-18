import streamlit as st
import random

# MBTI 유형별 추천 노래 목록 (각 10곡 이상)
# 이 목록은 자유롭게 수정하거나 더 추가하셔도 좋습니다.
mbti_songs = {
    "INFP": [
        "아이유 (IU) - 밤편지",
        "Coldplay - Fix You",
        "Billie Eilish - everything i wanted",
        "잔나비 - 주저하는 연인들을 위해",
        "볼빨간사춘기 - 나의 사춘기에게",
        "NCT DREAM - 고래 (Dive Into You)",
        "Lauv - Paris in the Rain",
        "태연 (TAEYEON) - I",
        "검정치마 - Hollywood",
        "Radiohead - Creep"
    ],
    "INFJ": [
        "이하이 - 한숨",
        "방탄소년단 (BTS) - Spring Day (봄날)",
        "Lana Del Rey - Young and Beautiful",
        "Sam Smith - Stay With Me",
        "태연 (TAEYEON) - Fine",
        "악동뮤지션 (AKMU) - 어떻게 이별까지 사랑하겠어, 널 사랑하는 거지",
        "Adele - Someone Like You",
        "Lo-fi Hip Hop - (다양한 아티스트)",
        "Harry Styles - Sign of the Times",
        "선우정아 - 도망가자"
    ],
    "ENFP": [
        "방탄소년단 (BTS) - Dynamite",
        "TWICE (트와이스) - Dance The Night Away",
        "AKMU (악뮤) - 200%",
        "Pharrell Williams - Happy",
        "레드벨벳 (Red Velvet) - 빨간 맛 (Red Flavor)",
        "Harry Styles - As It Was",
        "Mika - We Are Golden",
        "세븐틴 (SEVENTEEN) - 아주 NICE",
        "ZICO (지코) - 아무노래",
        "저스디스 (JUSTHIS) & Don Malik - 갓 godly"
    ],
    "ENFJ": [
        "Katy Perry - Firework",
        "Imagine Dragons - Believer",
        "소녀시대 (Girls' Generation) - 다시 만난 세계 (Into The New World)",
        "Sia - Unstoppable",
        "Queen - Don't Stop Me Now",
        "에일리 (Ailee) - 보여줄게",
        "The Greatest Showman OST - This Is Me",
        "Coldplay - Viva La Vida",
        "Florence + The Machine - Dog Days Are Over",
        "윤하 (YOUNHA) - 사건의 지평선"
    ],
    "ISTJ": [
        "George Winston - Thanksgiving",
        "Queen - Bohemian Rhapsody",
        "Simon & Garfunkel - Bridge Over Troubled Water",
        "김동률 - 출발",
        "성시경 - 거리에서",
        "Adele - Rolling in the Deep",
        "토이 (Toy) - 내가 너의 곁에 잠시 살았다는 걸",
        "Michael Jackson - Heal the World",
        "Coldplay - The Scientist",
        "Maroon 5 - Memories"
    ],
    "ISFJ": [
        "아이유 (IU) - 무릎",
        "Ed Sheeran - Perfect",
        "어반자카파 - 널 사랑하지 않아",
        "폴킴 - 너를 만나",
        "Bill Withers - Lean on Me",
        "Taylor Swift - Lover",
        "백예린 (Yerin Baek) - 그건 아마 우리의 잘못은 아닐 거야",
        "Jason Mraz - I'm Yours",
        "크러쉬 (Crush) - Beautiful (도깨비 OST)",
        "Bruno Mars - Count on Me"
    ],
    "ESTJ": [
        "Survivor - Eye of the Tiger",
        "Queen - We Will Rock You",
        "Bon Jovi - It's My Life",
        "싸이 (PSY) - GANGNAM STYLE (강남스타일)",
        "BLACKPINK - 뚜두뚜두 (DDU-DU DDU-DU)",
        "Jessie J - Price Tag",
        "AC/DC - Highway to Hell",
        "Katy Perry - Roar",
        "방탄소년단 (BTS) - IDOL",
        "Imagine Dragons - Thunder"
    ],
    "ESFJ": [
        "ABBA - Dancing Queen",
        "Mark Ronson - Uptown Funk (feat. Bruno Mars)",
        "TWICE (트와이스) - CHEER UP",
        "Meghan Trainor - All About That Bass",
        "Kool & The Gang - Celebration",
        "아이유 (IU) - 좋은 날",
        "Pharrell Williams - Happy",
        "Maroon 5 - Sugar",
        "EXO - 으르렁 (Growl)",
        "에이핑크 (Apink) - NoNoNo"
    ],
    "ISTP": [
        "Arctic Monkeys - Do I Wanna Know?",
        "Eminem - Lose Yourself",
        "Imagine Dragons - Radioactive",
        "Linkin Park - Numb",
        "Post Malone - Circles",
        "혁오 (HYUKOH) - 와리가리",
        "The White Stripes - Seven Nation Army",
        "Billie Eilish - bad guy",
        "딘 (DEAN) - D (Half Moon)",
        "방탄소년단 (BTS) - MIC Drop"
    ],
    "ISFP": [
        "백예린 (Yerin Baek) - Square (2017)",
        "Lana Del Rey - Video Games",
        "Hozier - Take Me to Church",
        "Frank Ocean - Thinkin Bout You",
        "Crush - Oasis (feat. ZICO)",
        "태연 (TAEYEON) - Weekend",
        "Troye Sivan - YOUTH",
        "Heize (헤이즈) - 비도 오고 그래서",
        "keshi - like i need u",
        "아이유 (IU) - Palette (Feat. G-DRAGON)"
    ],
    "ESTP": [
        "Rihanna - Don't Stop The Music",
        "Macklemore & Ryan Lewis - Thrift Shop",
        "Cardi B - I Like It",
        "Pitbull - Timber (feat. Ke$ha)",
        "LMFAO - Party Rock Anthem",
        "방탄소년단 (BTS) - 불타오르네 (FIRE)",
        "블락비 (Block B) - HER",
        "JAY-Z & Kanye West - Ni**as In Paris",
        "Flo Rida - GDFR",
        "Lizzo - Juice"
    ],
    "ESFP": [
        "브루노 마스 (Bruno Mars) - 24K Magic",
        "마마무 (MAMAMOO) - 힙 (HIP)",
        "Dua Lipa - Don't Start Now",
        "Beyoncé - Crazy in Love",
        "레드벨벳 (Red Velvet) - 짐살라빔 (Zimzalabim)",
        "Justin Timberlake - Can't Stop the Feeling!",
        "BLACKPINK - 마지막처럼 (AS IF IT'S YOUR LAST)",
        "Lady Gaga - Just Dance",
        "모모랜드 (MOMOLAND) - 뿜뿜",
        "Shakira - Waka Waka"
    ],
    "INTJ": [
        "Radiohead - Paranoid Android",
        "Pink Floyd - Comfortably Numb",
        "Hans Zimmer - Time",
        "Daft Punk - Harder, Better, Faster, Stronger",
        "에픽하이 (EPIK HIGH) - 빈차 (Feat. 오혁)",
        "Massive Attack - Teardrop",
        "Muse - Hysteria",
        "Kendrick Lamar - DNA.",
        "TOOL - Schism",
        "G-DRAGON - 삐딱하게 (Crooked)"
    ],
    "INTP": [
        "Gorillaz - Feel Good Inc.",
        "Daft Punk - Around the World",
        "Tame Impala - The Less I Know The Better",
        "MGMT - Electric Feel",
        "alt-J - Breezeblocks",
        "King Gizzard & The Lizard Wizard - Gamma Knife",
        "San Holo - light",
        "f(x) - 4 Walls",
        "새소년 (SE SO NEON) - 긴 꿈",
        "M83 - Midnight City"
    ],
    "ENTJ": [
        "Kanye West - Stronger",
        "Fall Out Boy - Centuries",
        "CL - 나쁜 기집애 (THE BADDEST FEMALE)",
        "Queen - We Are The Champions",
        "Fort Minor - Remember The Name",
        "방탄소년단 (BTS) - Not Today",
        "Imagine Dragons - Whatever It Takes",
        "Linkin Park - In The End",
        "Jay-Z - Empire State Of Mind (feat. Alicia Keys)",
        "Sia - The Greatest"
    ],
    "ENTP": [
        "Queen - Don't Stop Me Now",
        "PSY - That That (prod. & feat. SUGA of BTS)",
        "OutKast - Hey Ya!",
        "Red Hot Chili Peppers - Can't Stop",
        "Die Antwoord - I Fink U Freeky",
        "노라조 (Norazo) - 슈퍼맨",
        "Panic! At The Disco - High Hopes",
        "OK Go - Here It Goes Again",
        "Eminem - Without Me",
        "지코 (ZICO) - 아티스트 (Artist)"
    ]
}

# --- Streamlit App UI ---

# 앱 제목 설정
st.title("🎧 MBTI별 오늘의 추천곡 🎵")
st.write("당신의 MBTI를 선택하고 오늘의 추천곡을 받아보세요!")

# MBTI 유형 목록 (딕셔너리의 키 값들을 리스트로 변환)
mbti_types = list(mbti_songs.keys())

# 드롭다운 메뉴로 MBTI 선택
selected_mbti = st.selectbox(
    "당신의 MBTI를 선택해주세요.",
    mbti_types
)

# '추천받기' 버튼
if st.button("🎶 노래 추천받기!"):
    if selected_mbti:
        # 선택된 MBTI에 해당하는 노래 리스트 가져오기
        song_list = mbti_songs[selected_mbti]
        
        # 리스트에서 랜덤으로 노래 한 곡 선택
        random_song = random.choice(song_list)
        
        # 결과 출력
        st.subheader(f"'{selected_mbti}' 님을 위한 오늘의 추천 곡은...")
        st.title(f"🎉 {random_song}")
        st.write("이 노래와 함께 즐거운 하루 보내세요! 😊")

        # 유튜브 검색 링크 제공 (선택 사항)
        youtube_search_url = f"https://www.youtube.com/results?search_query={random_song.replace(' ', '+')}"
        st.markdown(f"▶️ [YouTube에서 바로 들어보기]({youtube_search_url})")
