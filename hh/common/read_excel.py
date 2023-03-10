import xlrd
import csv
import os
class readExcel:

    def __init__(self,path,sheet_neme='Sheet1'):
        self.excel=xlrd.open_workbook(path)
        self.sheet_neme=sheet_neme
    def get_data(self):
        '''

        :param rowx:
        :return:
        '''
        self.sheet=self.excel.sheet_by_name(sheet_name=self.sheet_neme)

        self.case=[]
        for i in range(1,self.sheet.nrows-1):
            self.data=self.sheet.row_values(i)

            self.case.append(self.data)
        return self.case
    def get_testcase(self):

        self.case=[]
        for i in (1,self.sheet.nrows):

            self.case.append(self.get_data(i))
        return self.case
class get_csvdata:
    def __init__(self,path):
        self.path=path
    def getCsvData(self):
        with open(self.path,"r",encoding="gbk") as f:
            datacase=[]
            csvData=csv.reader(f)
            for i in csvData:
                datacase.append(i)

            datacase=datacase[1:]
            # print(datacase)
        return datacase
        # print(csvData)
    def write_csv(self,i):
        #创建列表标题
        he=['测试标题','模块','测试结果']
        path=os.path.join(os.path.dirname(__file__),'aa.csv')
        with open(path,mode='w',encoding='utf-8',newline="") as f:
            writer=csv.writer(f)
            writer.writerows(i)

if __name__ == '__main__':

    path=r'C:\Users\he\PycharmProjects\woniu233\hh\testCase\222.csv'
    # a=readExcel(path=path).get_data()
    i=[['访问百度首页', '百度', '测试通过'], ['访问百度首页2', '百度', '测试失败']]
    a=get_csvdata(path).write_csv(i=i)
    # possword=122
    # for i,j in enumerate(a):
    #     if  i==0:
    #         d=j[5]
    #         print(eval(d))
    #     else:
    #         pass
    #
    #
    #






