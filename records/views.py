from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Note, Excerpts
from .myscript.morning_night_login import Morning_punch
import pymysql, time, smtplib
from email.mime.text import MIMEText  # 专门发送正文
from email.mime.multipart import MIMEMultipart  # 发送多个部分
# Create your views here.


def send(receiver, message):
    send_user = ''  # 发件人
    password = ''  # 密码
    receive_users = receiver  # 收件人，可为list
    subject = '回复'  # 邮件主题
    email_text = message  # 邮件正文
    server_address = 'smtp.qq.com'  # 服务器地址
    # 构造一个邮件体：正文 附件
    msg = MIMEMultipart()
    msg['Subject'] = subject  # 主题
    msg['From'] = send_user  # 发件人
    msg['To'] = receive_users  # 收件人
    # 构建正文
    part_text = MIMEText(email_text)
    msg.attach(part_text)  # 把正文加到邮件体里面去
    # 发送邮件 SMTP
    smtp = smtplib.SMTP(server_address, 587)  # 连接服务器，SMTP_SSL是安全传输
    smtp.login(send_user, password)
    smtp.sendmail(send_user, receive_users, msg.as_string())  # 发送邮件
    print('邮件发送成功！')


def index(request):
    # context = {'topics': topics, 'notes': notes}

    notes = Note.objects.all().order_by('-update_date')
    excerpts = Excerpts.objects.all().order_by('update_date')
    context = {'notes': notes, 'excerpts': excerpts}
    return render(request, 'records/index.html', context)


def title(request, note_topic, note_title):
    """晨午晚检"""
    if note_title == '模拟登录-自动填报' and note_topic == 'python':
        return render(request, 'records/morning.html')
    elif note_title == 'Django-blog搭建' and note_topic == 'python':
        return render(request, 'records/first_note.html')


def email(request):
    # 向我发送邮件:
    if request.method == 'POST':
        sender = request.POST['email']
        main_text = request.POST['main_text']
        send('', sender+'\n'+main_text)
        messages.error(request, '成功')
        return HttpResponseRedirect('/email/')
    else:
        return render(request, 'records/email.html')


def morning_night_login(request):
    # 注册晨午晚检
    def save_data(username, password, email, enable):
        # 存储信息
        db = pymysql.connect(host='', user='', password='', port=, db='')
        cursor = db.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS user_data (record_date INT NOT NULL, username INT NOT NULL, password VARCHAR(255) NOT NULL, email VARCHAR(255) ' \
              ', enable VARCHAR(255) NOT NULL)'
        cursor.execute(sql)
        tm = time.localtime()
        date = str(tm.tm_year) + '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday) + '-' + str(tm.tm_hour) + '-' + str(
            tm.tm_min)
        cursor = db.cursor()
        data = {'record_date': date, 'username': username, 'password': password,
                'email': email, 'enable': enable}
        table = 'user_data'
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f'INSERT INTO {table}({keys}) values ({values})'
        try:
            if cursor.execute(sql, tuple(data.values())):
                print('Successful')
                db.commit()
        except:
            print('Failed')
            db.rollback()
        db.close()

    if request.method == 'POST':
        user_username = request.POST['user_username']
        user_password = request.POST['user_password']
        user_email = request.POST['user_email']
        if user_email == '':
            user_email = False
            enable = False
        else:
            enable = True
            try:
                send(user_email, '已完成， 如需取消通知或停止使用，请向本邮箱发送信件。')
            except:
                messages.error(request, '邮箱错误')
                return HttpResponseRedirect("/python/模拟登录-自动填报/")
        demo = Morning_punch(user_username, user_password)
        if demo.run() == '操作成功' or demo.run() == '您已上报过' or demo.run() == '未到上报时间':
            save_data(user_username, user_password, user_email, enable)
            messages.error(request, '成功')
            return HttpResponseRedirect("/python/模拟登录-自动填报/")
        else:
            print(demo.run())
            messages.error(request, '账号或密码不正确')
            return HttpResponseRedirect("/python/模拟登录-自动填报/")
