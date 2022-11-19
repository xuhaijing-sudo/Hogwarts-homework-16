import unittest

class Search:

    def search_fun(self):
        print("woswhixuhaijing")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.search=Search()

    def setUp(self) -> None:
        print("setup_方法级别")
        self.search=Search()

    def tearDown(self) -> None:
        print("teardown 方法级别")
    def test_search1(self):
        print("search1")
        search=Search()
        assert True==search.search_fun()

    def test_search2(self):
        print("search2")
        search=Search()
        assert True==search.search_fun()

    def test_search3(self):
        print("search3")
        search=Search()
        assert True==search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"断言1==1")

    def test_notequal(self):
        print("断言相等")
        self.assertNotEqual(1,2,"断言1==1")
if __name__ == '__main__':
    unittest.main()
    #执行一个测试套件，testsuite()
    suite=unittest.TestSuite()
    suite.addTest(TestSearch("test_search1"))
    suite.addTest(TestSearch("test_search3"))
    unittest.TextTestRunner().run(suite)

    #方法三：执行某个测试类，将测试类添加到测试套件里面，批量执行测试类
    suite1=unittest.TestLoader().loadTestsFromTestCase(TestSearch)
