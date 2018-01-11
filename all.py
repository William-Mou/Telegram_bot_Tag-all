import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from random import choice
import json

TOKEN = ''

bot = telepot.Bot(TOKEN)
telBot=telepot.Bot (TOKEN) 
Bot_inf=telBot.getMe()

def print_msg(msg):
    print(json.dumps(msg, indent=10))

def on_chat(msg):
    #print_msg(msg)
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    header = telepot.glance(msg, flavor="chat",long =True)
    if "@all" in msg["text"]:
        admins_list=[]
        admins_dict=telBot.getChatAdministrators (msg["chat"]["id"])
        chat_name=msg["chat"]["title"].encode('utf8')
        print(admins_dict)
        for admin in admins_dict:
            if 'username' in admin['user']:
                admins_list.append('@'+str(admin['user']["username"])+" ")
            else:
                user_id=admin["user"]["id"]
                '''
                try :
                    first_name=admin["user"]["first_name"].encode('utf8')
                    last_name=admin["user"]["last_name"].encode('utf8')
                    admins_list.append(first_name+" "+last_name)
                    admins_list.append(first_name)
                    admins_list.append(last_name)
                except:
                    pass
                bot.sendMessage(user_id, f"You was mentioned on {chat_name}")
                '''
        send=""
        for admin in admins_list:
            send+= admin + " "
        bot.sendMessage(header[2], send)
        #print(admins_list)
    
    
MessageLoop(bot, {
    'chat': on_chat,
    #'callback_query': on_callback_query,
}).run_as_thread()

print('Listening ...')