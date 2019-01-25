import allure
class Test_001:
    @allure.step(title="1")
    def test_001_1(self):
        print("--->test001")
        assert True
    @allure.step(title="2")
    def test_001_2(self):
        print("222")
        assert False