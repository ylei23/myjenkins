import requests
from hh.common.read_excel import *
from jsonpath import jsonpath
from hh.tstCase.nn import *
from hh.common.myloger import *
import re
import json
class kw:
    def __init__(self):
        self.res=None
        self.ac={}

        self.aaa={'a':1,
                  'b':2}

    def send_requests_post(self,*args,**kwargs):
        '''
        $.data[1].b
        '''
        # print(args)
        # loger.info(args)
        # loger.info(args[0])
        # loger.info('请求参数'+str(args[1]))
        self.res=requests.post(url=args[0],data=args[1],headers=args[2]).text
        # print(self.res)
        # loger.info(self.res)
        # self.aaa={'data':[{"a":1},{"b":(21,2)}]}
        # self.res={'data':1}
        # return self.res
    def assert_contail(self,*args):
        print(self.res+"1111111")
        if args[1] in self.res:
            return True
        else:
            return False
    def vb(self,*args):
        # s=re.search('http-equiv="(.*)"','http-equiv="X-UA-Compatible"')
        # print(s)
        # return  s.groups(1)[0]
        print('正则')
        s=re.search(args[1],self.res)
        self.ac[args[2]]=s.groups(1)[0]
        print('正则结束')
        print(self.ac)
        # return  s.groups(1)[0]






    def aa(self,x):
        print(self.aaa)
        return jsonpath(self.aaa,x)


if __name__ == '__main__':
    # path=r'C:\Users\he\PycharmProjects\woniu233\hh\testCase\222.csv'
    # f=getattr(kw(),'vb')
    # # print(f)
    # print(f())
    ac={"aa":123}
    i="{'hb':ac['aa']}"
    print(eval(i))

    # a=readExcel(path=path).get_data()
    # a=get_csvdata(path).getCsvData()
    # for i in a:
    #     if i[-1]=='高':
    #         a=kw()
    #         a.send_requests_post()
    #         c=i[5]
    #         if i[6]!='toke':
    #             print(eval(i[5]))
    #
    #         # print(eval(c))
    #         if i[6]=='toke':
    #             b=a.aa(c)[0]
    #             print(b)
    #             # global eval(i[6])
    #             vv[i[6]]=b



            # print(vv['toke'])
   #  a=kw()
   #  a.send_requests_post()
   #  b=a.aa('$.data[1].b')
   # # a('$.data[1].b')
   #  print(b)
    # a=json.dumps(a)
    # print(jsonpath(a,'$.data[1].b'))
    # for i in a:
    #     if a[i]:
    #         print('用例开始')
    #         if hasattr(kw,'send_requests_post'):
    #             kww=getattr(kw,'send_requests_post')
    #             kww()
