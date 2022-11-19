# content of test_sample.py
import pytest
def func(x):
    return x+1

@pytest.mark.parametrize('a,b',[(1,2),(19,20),(4,5)])
def test_answer(a,b):
    assert func(a)==b

def test_answer1():
    assert func(4)==5

@pytest.fixture()
def login():
    username='jerry'
    return username

class TestDemo:
    def test_a(self,login):
        print(f"a username={login}")
        # print(f"a username={login}.format('xuhaijingzuibang')")

    def test_b(self):
        print("b")

if __name__=='__mian__':
    # pytest.main('test_sample.py')
    pytest.main(['test_sample.py::TestDemo','-v'])