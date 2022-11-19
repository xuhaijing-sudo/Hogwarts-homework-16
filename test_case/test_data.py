import pytest
import yaml
# @pytest.mark.parametrize('a,b',[(1,2),(19,20),(4,5)])
# class TestCase:
#     def test_case(self,a,b):
#         a=10
#         b=20
#         print(a+b)
#
# if __name__=='__mian__':
#     pytest.main('test_case.py')

#方法二：
class TestData:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a+b)
#
# if __name__=='__mian__':
#     pytest.main('test_data.py')