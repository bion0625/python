# ch07_07_Slack_SendMessage.py
import slack_sdk

slack = slack_sdk.WebClient(token="") # 슬랙 봇 토큰

markdown_text = '''
This message is plain.
*This message is plain.*
'This message is plain.'
_This message is plain._
~This message is plain.~
'''

attach_dict = {
    'color':'#ff0000',
    'author_name':'BION',
    'author_link':'github.com/investar',
    'title':'오늘의 증시 KOSPI',
    'title_link':'https://finance.naver.com/sise/sise_index.naver?code=KOSPI',
    'text':'2.236.13 🔺11.89 (+0.51%)',
    'image_url':'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}

attach_list = [attach_dict]

slack.chat_postMessage(channel="#test", text=markdown_text, 
                       attachments=attach_list)