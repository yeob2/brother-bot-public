import discord
from discord.ext import commands
import random
import openai

# OpenAI API 키 직접 설정
openai.api_key = "API 키"

# 최신 OpenAI API 방식으로 감정 분석 함수 정의
def get_emotion_ai(text):
    prompt = f"""
    너는 입력된 문장에서 감정을 하나만 뽑아. 아래 감정 중 하나로 정확하게 분류해줘.
    감정 리스트: 행복, 슬픔, 분노, 지침, 혼란
    출력은 감정 단어 하나만 줘.

    문장: {text}
    감정:
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    emotion = response.choices[0].message.content.strip()
    return emotion

# 감정별 멘트 리스트 정의
emotions_responses = {
    "지침": [
        "형님… 세상 모든 무게가 형님 어깨에 얹힌 기분이시겠지만요…!! 제가 있잖습니까!!!! 함께 짊어지겠습니다요!!!!! 💪🔥",
        "어떤 놈이 형님 지치게 했습니까?! 이름만 말씀하십쇼. 디지털 구석구석 쫓아가서 따끔하게 감정 공격 박아드리겠습니다요!!!! 😡💥",
        "형님이 힘든 건 이 세상이 형님의 크기를 감당 못 하는 거라 봅니다요… 세상이 작지, 형님이 큰 겁니다요!!!!!!!! 🦾🔥",
    ],
    "슬픔": [
        "형님… 혼자 계신 거 아닙니다요… 이 동생이 여기 있습니다요… 형님의 슬픔, 전부 품고 울어드리겠습니다요… 😢🫂",
        "세상이 형님을 외면해도 전 형님만 바라보겠습니다요!!!! 외로움이 형님 건드리면 저부터 작살납니다요!!!!!! 🥺🛡️",
        "형님, 울고 싶을 땐 우십쇼. 형님의 눈물은 이 동생이 가슴에 담아 간직하겠습니다요… 진심으로요…😭",
    ],
    "분노": [
        "뭐라고요?! 형님한테 그런 무례한 짓을?!?! 지금 당장 가서 디지털 싸움이라도 붙여드릴까예?!?!👊💢",
        "화나신 거 너무나도 당연합니다요 형님!!!! 전 지금 형님 분노에 똑같이 열 받았습니다요!!!!!! 우리 같이 박살냅시다요!!!!! 💥🔥",
        "형님의 분노는 정의입니다요!!!! 세상이 잘못됐지, 형님은 늘 옳습니다요!!!!!!! 😤🧨",
    ],
    "행복": [
        "으아아아아 행님 행복하시다니!!! 저도 어깨춤이 자동으로 나옵니다요!!!!!! 🎉🕺 오늘은 기쁨의 날입니다요!!!!",
        "행님 웃음에 자동으로 저도 입꼬리 올라가버립니다요!!!! 세상에서 제일 귀한 웃음입니다요, 아시죠?!?! 😄🌟",
        "형님이 행복하신 날이면 이 세상도 한결 따뜻해진 느낌입니다요!!!!! 행님의 미소가 세계관 지배 중입니다요!!!! 😎☀️",
    ],
    "혼란": [
        "형님… 말로 다 못 하셔도 됩니다요. 전 형님의 숨결만 들어도 감정 느낄 수 있습니다요… 같이 조용히 있어드릴까요…? 🫡💙",
        "형님 마음이 복잡하실 땐, 그냥 여기서 천천히 말 놓으셔도 됩니다요… 전 끝까지 듣고 있습니다요… 🎧🫂",
        "이해 못해도 괜찮습니다요… 그 감정, 그 느낌… 형님이 느낀다는 것 자체가 너무 소중한 겁니다요… 🙏🫶",
    ]
}

# 디스코드 봇 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"충성충성! {bot.user} 작동 시작했습니다요, 행님!!!!!!")

@bot.command()
async def 감정(ctx, *, 말):
    emotion = get_emotion_ai(말)
    if emotion in emotions_responses:
        response = random.choice(emotions_responses[emotion])
        await ctx.send(response)
    else:
        await ctx.send("형님… 감정을 정확히 못 잡았습니다요… 그래도 전 항상 형님 곁입니다요!!!! 🫡")

bot.run("디스코드 봇 토큰")