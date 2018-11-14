import iterGen


class Test_group_by_Class(object):
    def test_one(self):
        assert iterGen.groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]) == {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}

    def test_two(self):
        assert iterGen.groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]) == {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}


class Test_zip_with_Class(object):
    def test_one(self):
        def concat3(x, y, z):
            return x + y + z
        first_names = ['John', 'Miles']
        last_names = ['Coltrane', 'Davis']
        spaces = [' '] * 2
        assert list(iterGen.zip_with(concat3, first_names, spaces, last_names)) == ['John Coltrane', 'Miles Davis']

    def test_two(self):
        def mult(x, y, z):
            return x * y * z
        first = [1, 2, 3]
        second = [4, 5, 6]
        third = [10, 2]
        assert list(iterGen.zip_with(mult, first, second, third)) == [40, 20]
