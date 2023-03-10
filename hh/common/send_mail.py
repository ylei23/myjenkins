import yagmail
'''
yagmail.SMTP()创建yagmail对象：
user是自己的邮箱，password是自己QQ邮箱的密钥，host是smtp针对qq的服务器域名
'''
class send_email():
    def se(self,to=['1849962014@qq.com']):
        my_yagmail=yagmail.SMTP(user='1576565903@qq.com',password='zuegqavmkcznjgfi',host='smtp.qq.com') #password是发送账户的授权码
        print(my_yagmail)
        #发送邮件，邮件主题，
        my_yagmail.send(subject='测试邮件',#这是邮件主题
                        #收件人，多个用列表
                        to=to,
                        contents='测试邮件',#这是邮件正文
                        attachments=r'C:\Users\he\PycharmProjects\woniu233\hh\tstCase\222.csv' #附件路径
                        )
        my_yagmail.close()
if __name__ == '__main__':
    pass