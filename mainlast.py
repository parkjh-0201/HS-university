from flask import Flask, render_template_string
from telegram import Bot

import urllib.request
import json
import random
import asyncio
import speech_recognition as sr
import threading
import webbrowser

app = Flask(__name__)

API_KEY = "87e1cd68ee2aaadb0f0756d8ce92d229"

BOT_TOKEN = "8737505648:AAExS0gxcQLtOQSUSC2YAA5eqzbcSyuvhFc"

CHAT_ID = "5488401445"


bot = Bot(token=BOT_TOKEN)

current_weather = "없음"
current_song = "없음"

playlists = {

    "Clear": [
        (
            "맑은날 플레이리스트",
            "https://www.youtube.com/watch?v=jfKfPfyJRdk"
        )
    ],

    "Rain": [
        (
            "비오는날 감성 플레이리스트",
            "https://www.youtube.com/watch?v=DWcJFNfaw9c"
        )
    ],

    "Clouds": [
        (
            "잔잔한 음악 플레이리스트",
            "https://www.youtube.com/watch?v=lTRiuFIWV54"
        )
    ],

    "Snow": [
        (
            "겨울 플레이리스트",
            "https://www.youtube.com/watch?v=7NOSDKb0HlU"
        )
    ]
}


def get_weather():

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q=Seoul"
        f"&appid={API_KEY}"
    )

    with urllib.request.urlopen(url) as r:

        data = json.loads(r.read())

    return data["weather"][0]["main"]


async def send_telegram(msg):

    await bot.send_message(
        chat_id=CHAT_ID,
        text=msg
    )


def listen_command():

    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:

        print("🎤 명령을 기다리는 중...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(
            audio,
            language="ko-KR"
        )

        print("인식:", text)

        return text

    except Exception as e:
        print("음성인식 오류:", repr(e))
        return ""


def voice_assistant():

    global current_weather
    global current_song

    while True:

        command = listen_command()
       
        print("받은 명령:", command)

        if (
        "날씨에 맞게 음악 틀어줘" in command
        or "음악 틀어 줘" in command
        or "음악 추천해줘" in command
        ):
           
            print("명령 인식 성공!")

            weather = get_weather()

            if weather not in playlists:
                weather = "Clouds"

            song, url = random.choice(
                playlists[weather]
            )

            current_weather = weather
            current_song = song

            webbrowser.open(url)

            msg = (
                f"[AI 음악 추천]\n\n"
                f"현재 날씨 : {weather}\n"
                f"재생목록 : {song}"
            )

            asyncio.run(
                send_telegram(msg)
            )


@app.route("/")

def home():

    html = f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>AI Music System</title>
    </head>

    <body>

        <h1>🎵 AI 날씨 음악 추천 시스템</h1>

        <h2>현재 날씨 : {current_weather}</h2>

        <h2>현재 재생목록 : {current_song}</h2>

        <p>
        마이크에
        '날씨에 맞게 음악 틀어줘'
        라고 말해보세요.
        </p>

    </body>
    </html>
    """

    return render_template_string(html)


if __name__ == "__main__":

    voice_thread = threading.Thread(
        target=voice_assistant,
        daemon=True
    )

    voice_thread.start()

    app.run(
        host="0.0.0.0",
        port=5000
    )
