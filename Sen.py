import os
import playsound
import pyaudio
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch

language = 'vi'
path = ChromeDriverManager().install()
wikipedia.set_lang('vi')

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow = False) #chuyển văn bản thành âm thanh theo ngôn ngữ nhận dạng tiếng việt 
    tts.save("sound.mp3.mp3") #rồi lưu về máy tính dữ liệu âm thanh dưới file
    playsound.playsound("sound.mp3.mp3", False) #đọc file sound.mp3 trên máy tính
    os.remove("sound.mp3.mp3")
    #đọc xong xóa file để tránh lỗi khiđọc một đoạn văn bản khác cũng được lưu lại dưới file sound.mp3.mp3
    
def get_voice():
    r = sr.Recognizer() #nhận dạng giọng nói để chuyển âm thanh thành văn bản
    with sr.Microphone() as source:
        #đọc vào microphone của máy tính sau đó được xử lý qua hàm listen của sr.Recognition 
        #rồi lưu dữ liệu âm thanh vào biến audio
        print("Me: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("┐(￣ヘ￣;)┌........")
            return 0

def stop():
    speak("Dạ vâng, cần gì bạn lại ới Sen nhé. Hẹn gặp lại bạn yêu ạ!")

def get_text(): # nhận dạng âm thanh của người đọc tối đa 3 lần cho đến khi máy tính hiểu
    for i in range(3):
        text = get_voice()
        if text:
            return text.lower()
        elif i < 2:
            speak("Sen không nghe rõ, bạn có thể nói lại không ạ?")
    time.sleep(10)
    stop()
    return 0

def talk(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Tất nhiên rồi, tôi thích nói chuyện với bạn mà. Chào buổi sáng {}. Chúc bạn ngày mới tốt lành!".format(name))
    elif day_time < 18:
        speak("Tất nhiên rồi, tôi thích nói chuyện với bạn mà. Chào buổi chiều {}! Bạn đã dự định gì cho chiều nay chưa? ".format(name))
        time.sleep(1)
    else:
        speak("Tất nhiên rồi, tôi thích nói chuyện với bạn mà. Chào buổi tối {}! Chắc hẳn bạn đã có một ngày tuyệt vời đúng không?".format(name))
        time.sleep(1)
    time.sleep(7)
    speak("Nói chuyện với tôi, bạn thấy thế nào ?")
    ans = get_voice()
    if ans:
        if "không" in ans or "chán" in ans or "nhạt" in ans:
            speak("Ok, tôi sẽ cố gắng hơn ạ")
        elif "tốt" in ans or "vui" in ans or "được" in ans:
            speak("Có chi đâu bấy bề, đó là nhiệm vụ của tôi mà!")
        else:
            speak("Ok, tôi sẽ cố gắng hơn ạ")
    time.sleep(4)
    speak("Bạn có muốn nghe chuyện cười Sen kể?")
    ans = get_voice()
    if ans:
        if "có" in ans or "ok" in ans:
            speak("""Dạ vâng, câu chuyện như thế này:
                    Một bà vợ đòi ly dị chồng vì anh ta suốt ngày uống rượu. Quan tòa hỏi:
                    - Chồng bà bắt đầu uống rượu từ khi nào?
                    - Từ trước khi chúng tôi cưới nhau.
                    - Thế sao lúc đó bà vẫn quyết định cưới ông ấy?
                    - Vì lúc đó tôi nghĩ chắc hẳn anh ta phải có rất nhiều tiền nên mới uống rượu mỗi ngày như thế.
                    Ha ha ha """)
            time.sleep(27)
            speak("Bạn muốn nghe chuyện cười Sen kể nữa?")
            ans = get_voice()
            if ans:
                if "có" in ans or "ok" in ans:
                    speak(""" Dạ vâng, câu chuyện thứ hai như thế này:
                              Một người đứng cạnh miệng cống và quăng tiền giấy xuống.
                              Người đi qua thấy lạ liền thắc mắc .
                              - Ông đang làm gì thế?
                              - Tôi đánh rơi một đồng xu xuống cống.
                              - Nhưng sao ông lại ném thêm tiền xuống nữa?
                              - Tôi không muốn người ta nói rằng tôi chui xuống cống chỉ vì một đồng xu. 
                              Ha ha ha """)
                    time.sleep(30)
                elif "không" in ans or "thôi" in ans or "no" in ans:
                    speak("Dạ vâng ạ, hẹn lần sau bạn nhé!")
                time.sleep(2)
        elif "không" in ans or "thôi" in ans or "no" in ans:
            speak("Dạ vâng ạ, hẹn lần sau bạn nhé!")
            time.sleep(2)
    time.sleep(2)     
    speak("Bạn thấy Sen nói chuyện khá hơn chưa ạ?")
    ans = get_voice()
    if ans:
        if "không" in ans or "chán" in ans or "nhạt" in ans:
            speak("Ok, tôi sẽ cố gắng hơn ạ")
        elif "tốt" in ans or "vui" in ans or "được" in ans:
            speak("Có chi đâu bấy bề, đó là nhiệm vụ của tôi mà!")
        else:
            speak("Ok, tôi sẽ cố gắng hơn ạ")
    time.sleep(4)
    speak("Ngày hôm nay của bạn thế nào?")
    ans = get_voice()
    if ans:
        if "có" in ans or "khoẻ" in ans or "tốt"  in ans or "ổn" in ans :
            speak("Thật là tốt, mong ngày mai bạn cũng nhiều năng lượng như vậy!")
        elif "không" in ans or "mệt" in ans:
            speak("Vậy à, bạn nên nghỉ ngơi sớm đi nhé! Mong ngày mai bạn sẽ khoẻ mạnh và nhiều năng lượng hơn!")
            time.sleep(2)
        else:
            speak("Chà, mong ngày mai bạn sẽ khoẻ mạnh và nhiều năng lượng hơn nhé!")
    ans = get_voice()
    time.sleep(3)
    if ans:
            speak("Lúc nào tôi cũng vui khi được giúp đỡ bạn mà. Sen luôn bên bạn, đừng lo nhé!")
    time.sleep(8)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def google_search(text):
    search_for = text.split("tìm", 1)[1]
    speak("Ô kê la, có ngay đây ạ. Google tìm kiếm đã sẵn sàng")
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    query = driver.find_element_by_xpath("//input[@name='q']")
    query.send_keys(str(search_for))
    query.send_keys(Keys.RETURN)
    time.sleep(8)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def get_time(text):
    now = datetime.datetime.now()
    speak("Dạ vâng có ngay đây ạ, bạn muốn xem gì ạ ?")
    ans = get_voice()
    if ans:
        if "giờ" in ans:
            speak("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
        elif "ngày" in ans:
            speak("Hôm nay là ngày %d tháng %d năm %d " % (now.day, now.month, now.year))
            time.sleep(2)
        else:
            speak("Sen không hiểu, bạn có thể nói lại được không?")
            time.sleep(5)
    time.sleep(4)
    speak("Bạn có muốn xem thời gian nữa?")
    ans = get_voice()
    if ans:
        if "thôi" in ans or "không" in ans :
            speak("Dạ vâng ạ")
        elif "có" in ans or "tiếp" in ans:
            speak("Dạ vâng, mời bạn đặt câu hỏi ạ!")
            ans = get_voice()
            if ans:
                if "giờ" in ans:
                    speak("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
                if "ngày" in ans:
                    speak("Hôm nay là ngày %d tháng %d năm %d " % (now.day, now.month, now.year))
                else:
                    speak("Sen không hiểu, bạn có thể nói lại được không?")
                    time.sleep(5)
        elif "giờ" in ans:
            speak("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
        elif "ngày" in ans:
            speak("Hôm nay là ngày %d tháng %d năm %d " % (now.day, now.month, now.year))
        else:
            speak("Sen không hiểu, bạn có thể nói lại được không?")
            time.sleep(2)
    time.sleep(5)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def play_youtube():
    speak("Xin mời bạn chọn bài hát")
    time.sleep(3)
    my_song = get_text() #lấy thông tin tên bài hát muốn phát rồi lưu vào biến my_song
    while True:
        result = YoutubeSearch(my_song, max_results = 10).to_dict()
        if result:
            break;
    url = 'https://www.youtube.com' + result[0]['url_suffix'] #lưu đường dẫn đến kết quả đầu tiên khi tìm kiếm trên Youtube
    webbrowser.open(url)
    #mở đường dẫn url đến video vừa được tìm kiếm trên Google Chrome để phát nhạc.
    speak("Bài hát của bạn đã được mở, hãy thưởng thức nó!")
    time.sleep(8)
    speak("Bạn cần Sen giúp gì nữa không ạ?")
    
def weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ?") 
    time.sleep(3)
    url = "http://api.openweathermap.org/data/2.5/weather?" #lưu đường đẫn đến api của trang web
    city = get_text() #lấy thông tin thành phố cần truy vấn thời tiết rồi lưu vào biến city
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = url + "appid=" + api_key + "&q=" + city + "&units=metric"
    #lưu đường dẫn đầy đủ để truy vấn bao gồm thông tin tên thành phố city và api_key mình đã lấy ở trên.
    response = requests.get(call_url)
    #ấy thông tin truy vấn được từ trang web
    # lưu vào biến response. response.json() sẽ chuyển dữ liệu thuần về kiểu dữ liệu json rồi lưu vào biến data
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temp = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        sun_time  = data["sys"]
        sun_rise = datetime.datetime.fromtimestamp(sun_time["sunrise"])
        sun_set = datetime.datetime.fromtimestamp(sun_time["sunset"])
        wther = data["weather"]
        weather_des = wther[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day, month = now.month, year= now.year, hourrise = sun_rise.hour, minrise = sun_rise.minute,
                                                                           hourset = sun_set.hour, minset = sun_set.minute, 
                                                                           temp = current_temp, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(25)
    else:
        speak("Không tìm thấy thành phố!")
    time.sleep(8)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def open_application(text):
    if "chrome" in text:
        speak("Ô kê la, có ngay đây ạ. Google Chrome đã sẵn sàng")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        speak("Ô kê la, có ngay đây ạ. Mở Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
    elif "excel" in text:
        speak("Ô kê la, có ngay đây ạ. Mở Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
    elif "powerpoint" in text:
        speak("Mở Microsoft PowerPoint")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk')
    else:
        speak("Phần mềm của bạn chưa được cài đặt!")
    time.sleep(8)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def tell_me():
    try:
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe tiếp hay không ?")
            ans = get_text()
            if "có" not in ans:
                break
            speak(content)
            time.sleep(10)
        speak("Cảm ơn bạn đã lắng nghe!")
    except:
        speak("Sen không định nghĩa được ngôn ngữ của bạn!")
    time.sleep(5)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "D:\Download\BaoCaoAI\image.png")
    image=os.path.join("D:\Download\BaoCaoAI\image.png")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak('Hình nền máy tính vừa được thay đổi')
    time.sleep(5)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def help():
    speak("""Sen có thể làm những việc sau:
    1. Trò chuyện cùng bạn
    2. Hiển thị thời gian
    3. Chơi nhạc trên Youtube
    4. Dự báo thời tiết
    5. Mở Google tìm kiếm
    6. Mở Application
    7. Định nghĩa với Wikipedia
    8. Thay hình nền Laptop
    9. Gửi thư qua Gmail""")
    time.sleep(25)
    speak("Bạn cần Sen giúp gì nữa không ạ?")
    
def send_mail(text):
    speak("Bạn muốn gửi gmail cho ai ạ?")
    recipient = get_text()
    if "ngọc" in recipient:
        speak('Ô kê la, hãy nói cho Sen nội dung bạn muốn gửi là gì?')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('charliehoang2302@gmail.com', '123ngoc123')
        mail.sendmail('charliehoang2302@gmail.com', 'ngochieu230201@gmail.com', str(content).encode("utf-8"))
        mail.close()
        speak('Sen đã hoàn thành nhiệm vụ xuất sắc. Bạn check lại email nhé hihi.')
    else:
        speak('Sen không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không ạ?')
    time.sleep(7)
    speak("Bạn cần Sen giúp gì nữa không ạ?")

def call_sen():
    speak("Xin chào, bạn tên là gì nhỉ?")
    time.sleep(2)
    name = get_text()
    if name:
        speak("Chào bạn {}, người dùng yêu quý. Tôi chính là trợ lý ảo Sen. Cần gì bạn chỉ việc hô, tôi sẽ lập tức bay vô giúp liền!".format(name))
        time.sleep(10)
        speak("Bạn cần Sen giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            elif "trò chuyện" in text or "nói chuyện" in text:
                talk(name)
            elif "thời gian" in text or "xem ngày" in text or "xem giờ" in text:
                get_time(text)
            elif "dừng" in text or "nghỉ" in text or "thôi" in text:
                stop()
                break
            elif "chơi nhạc" in text or "mở youtube" in text:
                play_youtube()
            elif "thời tiết" in text or "nhiệt độ" in text:
                weather()
            elif "hình nền" in text:
                change_wallpaper()
            elif "định nghĩa" in text:
                tell_me()
            elif "làm gì" in text:
                help()
            elif "mở" in text:
                if "mở google" in text:
                    google_search(text)
                else:
                    open_application(text)     
            elif "gửi thư" in text or "gmail" in text or "email" in text:
                send_mail(text)

call_sen()