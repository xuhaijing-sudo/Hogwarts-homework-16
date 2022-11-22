import pytest
def setup_module():
    print("setup:整个test_setup_teardown模块开始时只执行一次")
def teardown_module():
    print("setup:整个test_setup_teardown模块结束时只执行一次")
def setup_function():
    print("setup:不在类中的测试用例开始的时候都会执行")
def teardown_function():
    print("teardown:不在类中的测试用例结束的时候都会执行")
def test_three():
    print("test-three")
def test_four():
    print("test-four")
class TestClass():
    def setup_class(self):
        print("setup：类里面所有用例开始时执行")
    def teardown_class(self):
        print("teardown：类里面所有用例结束时执行")
    def setup_method(self):
        print("steup：每个用例开始执行")
    def teardown_method(self):
        print("teardown：每个用例结束执行")
    def test_one(self):
        print("test_one")
    def test_two(self):
        print("test_two")