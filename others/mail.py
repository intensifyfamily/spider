import smtplib
from email.mime.text import MIMEText


class mailhelper(object):
    def __init__(self):
        self.mail_host = 'smtp.163.com'
        self.mail_user = 'itang85@163.com'
        self.mail_pass = 'itang85'
        self.mail_postfix = '163.com'
    def send_mail(self,to_list,sub,content):
        me = 'itang'+'<'+self.mail_user+'@'+self.mail_postfix+'>'
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.set_debuglevel(1)
            server.connect(self.mail_host)
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me,to_list,msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(str(e))
            return False


if __name__ == '__main__':
    mailto_list = ['1094252227@qq.com']
    content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .word{
            font-size: 100px;
            font-family: "黑体";
            color: crimson;
            background: chartreuse;
        }
        .url{
            font-size: 200px;
            font-family: "黑体";
        }
    </style>
</head>
<body>
<div align="center">
    <span class="word">色情网站！！！</span>
<div align="center">
    <span id="sp" class="word">复制下方IP地址!用浏览器打开!</span>
</div>
<div align="center">
    <span class="url">148.70.18.126</span></div>
</div>
<script type="text/javascript">
     function show(){
     var wordid=document.getElementById("sp");
     if(wordid.style.visibility == "visible")
      wordid.style.visibility = "hidden";
     else
      wordid.style.visibility = "visible";
     setTimeout('show()',80);
      }
      show();

</script>
</body>
</html>
    '''
    if mailhelper().send_mail(mailto_list,"色色的邮件",content):
        print("发送成功")
    else:
        print("发送失败")
