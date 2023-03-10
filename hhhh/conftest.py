import pytest
import allure
@pytest.fixture(scope='session')
@allure.step('步骤1登录')
def login():
    print('前置登录成功')
    yield
    print('后置测试完成')