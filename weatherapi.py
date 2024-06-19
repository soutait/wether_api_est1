assert 1 == 1
import json #こちらで先ほど作成したjsonファイルをimportしています。
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
#-----------------------天気関係
url = "https://weather.tsukumijima.net/api/forecast/city/120010"  
payload = {"city":"120010"}  #このcityの指定コードだと千葉を指す。その他の県は最初に貼った参考リンクの天気予報APIのサイト参照してください。
tenki_data = requests.get(url, params=payload).json() 

#print(tenki_data)      --すべてのデータがjson形式で出力される


#タイトル(県名出力)
print(tenki_data["title"])

#日付
day="日付 :"+tenki_data["forecasts"][0]["date"]

#天気
weather="天気 :"+tenki_data["forecasts"][0]["telop"]

#気温
celsius = "最高気温 :"+tenki_data["forecasts"][0]["temperature"]["max"]["celsius"]+"°"

#風速
wave="風速 :"  +   tenki_data["forecasts"][0]["detail"]["wave"]

#降水確率 (0時~06時の観測データ)
rain="降水確率 :"  +   tenki_data["forecasts"][0]["chanceOfRain"]["T12_18"]


##-------------------------lineAPI関係

file = open('作成したjsonのファイル名.json','r')   #rはreadモード
info = json.load(file)



CHANNEL_ACCESS_TOKEN = info['3VwMKgnyjwmNXhlSVQgpx2ZB0I1QX2q26dDXm8hm7N6er1HcfwvZBOKQmzi1X+fz6I6+diy2RKr/f0bflJhIJQygX2mXQa7r3rHqa2s+kK2yTB+rMRZSHGh6bQJtx/APQ+AS1eeQv4tuyUJvs9tc6wdB04t89/1O/w1cDnyilFU=']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)



def main():
    USER_ID = info['U63f3f2d8d5aef7827f29ef194440ab09']
    messages = TextSendMessage(text = "今日の天気をお知らせします。\n"
    + day +"\n"+ weather+ "\n"+celsius+"\n"+ wave +"\n"+ rain
)
    
    
    
    #line_bot_api.push_message(USER_ID,messages = messages)  自分のみに送る
    
    #全員に送るブロードキャストテスト
    line_bot_api.broadcast(messages = messages)
    
if __name__ == "__main__":
    main()
    
