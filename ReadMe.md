### how to use:
- regularly run /src/detecter.py  
-----
### how to modify:
- change codes in sender.py
```python
    msg_from = 'stugdebug@foxmail.com'  # 发送方邮箱
    passwd = 'gnwbkadqubhuceid'  # 填入发送方邮箱的授权码
    msg_to = msg_to  # 收件人邮箱

    subject = "检测到网页更新"
    content = '以下是您的网页地址链接：\n' + send_info + '\n请点击此链接以确认更新的网页\n如果不是本人操作，请忽略本邮件\n'
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
```