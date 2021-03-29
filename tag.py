from pyrogram import Client,filters
import time

def admin_only(func):
    def check(Client, message):
        if message.from_user.id in admin_all:
            func(Client, message)
            print(message.from_user.id)
        else:
            message.reply("**You are not admin**")
    return check
def admin_only_asli(func):
    def check(Client, message):
        if message.from_user.id in list_admin:
            func(Client, message)
        else:
            message.reply("**You are not main admin**")
    return check

api_id =2586462
api_hash = '68542129131999986899b84a10a6170c'
mtx=""
speed=0.1
bot = Client('tager', api_id, api_hash,workers=7)
gap=0
mio=0
stoprep=0
print('amiralirj \n \n amiralirj bmolaaaaaa -------@amiralirjg')
api_id =2586462
api_hash = '68542129131999986899b84a10a6170c'
list3=[1410445908]
rip_text='.'
wwbots=[854021534,175844556]
bot = Client('tager', api_id, api_hash,workers=7)
tag_auto=0
lefti_auto=0
list_lefti={}
suplock=0
admin_all=[1410445908]
tag_auto_time=0
mentiontag=True
is_tagging = {}
shekar=0
man=[1410445908]
auto_tag_time=0
mention = lambda user_id, text: f'<a href=tg://user?id={user_id}>{text}</a>'
list_admin=[1410445908,1653256635]
welcome_groups = set()
welcome_text = '**دسته گل محمدی به جمع ما خوش امدی**'
welcome_sleep = 0
group_admin_id=0
mtx=""
speed=0.01
mtx_admin=''
mentiontag=True
is_tagging = {}
list1=[854021534,916277313,973350686,937705727,903755081,1634013164,1444214125,1639740275,1104936422]

@bot.on_message(filters.command(['settext']) & filters.group )
@admin_only
def sto1p(client, message):
    global mtx
    if message.reply_to_message:
        mtx = message.reply_to_message.text
        message.reply_text("**text setted**")
    else:
        message.reply_text('**『 خطا❗️لطفا این دستور را بر روی پیامی ریپلای کنید ! 』**')
 
@bot.on_message(filters.command(['deltext']) & filters.group )
@admin_only
def sto1p(client, message):
    global mtx
    mtx=''
    message.reply_text("**text deleted**")
    


def add_istagging(chat_id):
    global is_tagging
    if chat_id not in is_tagging:
        is_tagging.update({chat_id: False})


@bot.on_message(filters.regex(r'#players: 0') & filters.group & filters.user(list1))
def tagger(client, message):
    try:
        count=0
        global is_tagging
        
        chat_id = message.chat.id
        add_istagging(chat_id)
        bot.send_message(chat_id,'**tag started :)**')
        if not is_tagging[chat_id]:
            is_tagging[chat_id] = True
            chat_members = client.iter_chat_members(chat_id=chat_id)
            for usr in chat_members:
                if usr['user']['username']:
                    if is_tagging[chat_id]:
                        bot.send_chat_action(chat_id, 'typing')
                        if mentiontag==0:
                            bot.send_message(chat_id, '**{}** {}'.format(mtx,usr.user.mention()))
                        else:
                            bot.send_message(chat_id, '{} @{}'.format(mtx,usr['user']['username']))
                        
                            pass
                        
                        count+=1
                        time.sleep(speed)
                    else:
                        return
            is_tagging[chat_id] = False
    except Exception as e:
        print(e)
tag_auto=0

@bot.on_message(filters.command(['deltag']) & filters.group)
@admin_only
def sto2233p(client, message):
    global tag_auto
    xxy=message.command[1]
    if xxy=='on':
        tag_auto=1
        message.reply_text("**del tag is on**")
    elif xxy=='off':
        tag_auto=0
        message.reply_text("**del tag is off**")


@bot.on_message(filters.regex(r'starttag') & filters.group)
@admin_only
def tagger(client, message):
    try:
        count=0
        global is_tagging
        
        chat_id = message.chat.id
        add_istagging(chat_id)
        bot.send_message(chat_id,'**tag started :)**')
        if not is_tagging[chat_id]:
            is_tagging[chat_id] = True
            chat_members = client.iter_chat_members(chat_id=chat_id)
            for usr in chat_members:
                if usr['user']['username']:
                    if is_tagging[chat_id]:
                        bot.send_chat_action(chat_id, 'typing')
                        if mentiontag==0:
                            bot.send_message(chat_id, '**{}** {}'.format(mtx,usr.user.mention()))
                        else:
                            bot.send_message(chat_id, '{} @{}'.format(mtx,usr['user']['username']))
                        
                            pass
                        
                        count+=1
                        time.sleep(speed)
                    else:
                        return
            is_tagging[chat_id] = False
    except Exception as e:
        print(e)
tag_auto=0

@bot.on_message(filters.command(['deltag']) & filters.group)
@admin_only
def sto2233p(client, message):
    global tag_auto
    xxy=message.command[1]
    if xxy=='on':
        tag_auto=1
        message.reply_text("**del tag is on**")
    elif xxy=='off':
        tag_auto=0
        message.reply_text("**del tag is off**")

@bot.on_message(filters.command(['speedtag']) & filters.group)

def stwerop(client, message):
    global speed
    speed=float(message.command[1])
    message.reply_text(f"**ok setted {speed}**")






@bot.on_message(filters.regex(r'بازی شروع شد') & filters.group & filters.user(list1))
def sto333p(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
    if tag_auto==1:
        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention"):
                        if tagmsg.from_user.id not in wwbots:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.1)
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @amiralirjg 』\n {e}**")


@bot.on_message(filters.regex(r'stoptag') & filters.group & filters.user(list1))
def stoii88p(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
        message.reply_text('stoped')
        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention") and  tag_msgs.id not in list1:
                        if tagmsg.from_user.id not in wwbots:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.1)
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @amiralirjg 』\n {e}**")
    else:
        message.reply_text('tag nmikonam nooob')


@bot.on_message(filters.regex(r'تعداد بازیکنا به پنج') & filters.group & filters.user(list1))
def stoii88p(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention") and  tag_msgs.id not in list1:
                        if tagmsg.from_user.id not in wwbots:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.1)
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @amiralirjg 』\n {e}**")


@bot.on_message(filters.regex(r'چقدر کمین') & filters.group & filters.user(list1))
def stbbhvjbbbop(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False

        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention") and  tag_msgs.id not in list1:
                        if tagmsg.from_user.id not in wwbots:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.1)
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @amiralirjg 』\n {e}**")
###################################
list1=[1410445908,854021534,1289410047,1181120160,1653256635,175844556]

@bot.on_message(filters.regex(r'set main admin') & filters.group & filters.user(list1))
def stkirsirmirop(client, message):
    global admin_all
    global list_admin
    l=message.reply_to_message.from_user.id
    list_admin.append(l)
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    message.reply_text("** 『 !ادمین افزوده شد』**")
    
@bot.on_message(filters.command(['promateadmins']) & filters.group)
@admin_only_asli
def sto3we4srdtp(client, message):
    global list3
    global admin_all
    for i in client.iter_chat_members(gap,filter='administrators'):
        list3.append(i.user.id)
    message.reply_text(f"**انجام شد**")
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)


@bot.on_message(filters.regex(r'set admin') & filters.group )
@admin_only_asli
def sto3wje4srdtp(client, message):
    global list3
    global admin_all
    if message.reply_to_message:
        c=message.reply_to_message.from_user.id
        list3.append(c)
        message.reply_text("** 『 !ادمین افزوده شد』**")
    else:
        message.rep_text('**『 خطا❗️لطفا این دستور را بر روی پیامی ریپلای کنید ! 』**')
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)


@bot.on_message(filters.regex(r'del admin') & filters.group )
@admin_only_asli
def stoami111p(client, message):
    global list3
    global admin_all

    b=message.reply_to_message.from_user.id
    try:
        list3.remove(b)
        message.reply_text("** 『 !ادمین حذف شد』**")
    except:
        message.reply_text("**این یوزر در لیست وجود ندارد **")

    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    


@bot.on_message(filters.regex(r'clean adminlist') & filters.group )
@admin_only_asli
def st9999op(client, message):
    global list3
    global admin_all
    list3=[]
    message.reply_text("** 『 !تمامی ادمین ها حذف شدند』**")
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)

######################################################

@bot.on_message(filters.command(['deltags']) & filters.group)
@admin_only
def stopmanhkman(client, message):
    m=0
    chatid=message.chat.id
    message.reply_text(f"**درحال پاکسازی**")
    try:
        tag_msgs = [msg for msg in bot.iter_history(chatid,limit=1000) if msg.entities]
        for tagmsg in tag_msgs:
            for ent in tagmsg.entities:
                if ent.type in ("mention", "text_mention"):
                    if tagmsg.from_user.id not in wwbots:
                        m+=1
                        tagmsg.delete()
                        time.sleep(0.1)
                time.sleep(0.1)
        message.reply_text(f"**پاکسازی {m} تگ انجام شد**")
    except Exception as e:
        message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @amiralirjg 』\n {e}**")

            

bot.run()
