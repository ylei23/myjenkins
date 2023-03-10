from hhhh.test_h1.d import *
import pytest
import allure
from hhhh.api.aa import *
@allure.feature('这是TEST1')
class Test1:
    @allure.story('用例Test1_test1')
    def test_1(self):
        a()
        b()
        assert 1==1
    @allure.story('用例Test1_test2')
    def test_2(self):
        a()
        c()
        assert 1==2

@allure.feature('这是TEST2')
class Test2:
    @allure.story('用例Test2_test1')
    def test_1(self):
        a()
        b()
        assert 1==1
    @allure.story('用例Test2_test2')
    def test_2(self):
        b()
        c()
        assert 1==2


if __name__ == '__main__':
    pytest.main(['-sq','--alluredir=./allure_report',__file__])