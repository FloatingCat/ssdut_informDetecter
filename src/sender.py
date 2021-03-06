import smtplib
from email.mime.text import MIMEText


def sender(send_info):
    msg_from = 'stugdebug@foxmail.com'  # 发送方邮箱
    passwd = 'gnwbkadqubhuceid'  # 填入发送方邮箱的授权码
    msg_to = 'stug_iii@foxmail.com'  # 收件人邮

    subject = "检测到网页更新"
    content = '以下是您的网页地址链接：\n' + send_info + '\n请点击此链接以确认更新的网页\n如果不是本人操作，请忽略本邮件\n'
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as e:
        print(e)
    finally:
        s.quit()


if __name__ == "__main__":
    sender('stug_iii@foxmail.com', 'test_info')