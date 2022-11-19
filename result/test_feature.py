import pytest
import allure

@allure.feature("搜索模块")
class TestSearch():
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")

@allure.feature("登陆模块")
class TestLogin():
    @allure.story("登陆成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登陆页面"):
            print("登陆页面")
        with allure.step("步骤3：输入用户名和密码"):
            print("用户名密码")
            pass

    @allure.story("登陆失败")
    def test_login_success_b(self):
        print("这是登陆：测试用例，登陆失败")
        pass