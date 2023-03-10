from hh.Key_Word.keywords import *
from hh.common.read_excel import *
from hh.common.send_mail import *
import csv
import configparser
class excute_testcase:
    def __init__(self):
        self.passcount=0
        self.failCount=0
        self.res_test=[]
        self.res_test1=[]


    def tt(self):
        #获取测试用例
        tstcase=get_csvdata(path=r'C:\Users\he\PycharmProjects\woniu233\hh\tstCase\222.csv').getCsvData()
        # print(tstcase)
        #执行每条测试案例
        a=kw()
        for i in tstcase:
            #获取关键字
            # print(i[3])
            #获取参数
            # a=i[4:]
            # print(tuple(a),len(a))

            if i[0]:
                self.res_test.append(i[0])
                self.res_test.append(i[1])
            if hasattr(a,i[3]):
                re=getattr(a,i[3])
                res=re(i[4],i[5],i[6])
                if res==True:
                    self.passcount+=1
                    t_res='测试通过'
                    self.res_test.append(t_res)
                    self.res_test1.append(self.res_test[0:])
                    self.res_test.clear()
                elif res==False:
                    self.failCount+=1
                    t_res='测试失败'
                    self.res_test.append(t_res)
                    self.res_test1.append(self.res_test[0:])
                    self.res_test.clear()


    def ava(self):
        self.tt()
        path=r'C:\Users\he\PycharmProjects\woniu233\hh\testCase\222.csv'

        get_csvdata(path).write_csv(i=self.res_test1)

        send_email().se()

        # print(self.res_test1,self.passcount,self.failCount)
def read_ini():
    com=configparser.ConfigParser()
    com.read(r'C:\Users\he\PycharmProjects\woniu233\hh\config\ini',encoding='utf-8')
    rr=com.get("host",'sit')
    return rr


if __name__ == '__main__':
    # excute_testcase().ava()
    print(read_ini())

