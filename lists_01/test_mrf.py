import mapReduceFilterEtc


# content of mapReduceFilterEtc.py
class Test_task_1_Class(object):
    def test_one(self):
        assert mapReduceFilterEtc.task_1(5, 9) == [6, 8]

    def test_two(self):
        assert mapReduceFilterEtc.task_2('alAbaLaPyThoN') == ['A', 'L', 'P', 'T', 'N']

    def test_three(self):
        assert mapReduceFilterEtc.task_3(3, 5) == {3: 3, 4: 4, 5: 0}

    def test_four(self):
        assert mapReduceFilterEtc.task_4(["one", "two", "three", "four"]) == {'one': 3, 'two': 3, 'three': 5, 'four': 4}

    def test_five(self):
        assert mapReduceFilterEtc.task_5([1, 2, 3, -5, -4, 0, 3, 8]) == 2

    def test_six(self):
        assert mapReduceFilterEtc.task_6("alAbaLaPyThoN") == 5

    def test_seven(self):
        assert mapReduceFilterEtc.task_7(2, 6) == 90
