import pytest
from pythoncode.calculator import Calculator
class TestCalc:
    def setup_class(self):
        self.calc=Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [(3,5,8),(1,2,3),(1000,1000,2000)],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect==self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [(13,5,8),(5,2,3),(3000,1000,2000)],ids=["int","minus","bigint"])
    def test_sub(self,a,b,expect):
        assert expect==self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", [(13,5,65),(5,2,10),(3,10,30)],ids=["int","minus","bigint"])
    def test_mul(self,a,b,expect):
        assert expect==self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect", [(10,5,2),(5,2,2.5),(3000,1000,3)],ids=["int","minus","bigint"])
    def test_div(self,a,b,expect):
        assert expect==self.calc.div(a,b)