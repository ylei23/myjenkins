
import allure
@allure.step('步骤这是函数a')
def a():
    print('a1')
@allure.step('步骤这是函数b')
def b():
    print('b1')
@allure.step('步骤这是函数c')
def c():
    print('c')