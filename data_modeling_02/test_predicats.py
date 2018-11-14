import predicats


class Test_gt_Class(object):
    def test_one(self):
        a = predicats.gt(0)
        assert a(10) is True

    def test_two(self):
        a = predicats.gt(0)
        assert a(-10) is False

    def test_three(self):
        a = predicats.gt(0)
        assert a(0) is False


class Test_lt_Class(object):
    def test_one(self):
        a = predicats.lt(0)
        assert a(-10) is True

    def test_two(self):
        a = predicats.lt(0)
        assert a(10) is False

    def test_three(self):
        a = predicats.gt(0)
        assert a(-10) is False


class Test_eq_Class(object):
    def test_one(self):
        a = predicats.eq(0)
        assert a(0) is True

    def test_two(self):
        a = predicats.eq(0)
        assert a(10) is False

    def test_three(self):
        a = predicats.eq(0)
        assert a(-10) is False


class Test_of_type_Class(object):
    def test_one(self):
        a = predicats.oftype(int)
        assert a(0) is True

    def test_two(self):
        a = predicats.oftype(str)
        assert a(10) is False

    def test_three(self):
        a = predicats.oftype(str)
        assert a('10') is True


class Test_present_Class(object):
    def test_one(self):
        a = predicats.present()
        assert a(0) is True

    def test_two(self):
        a = predicats.present()
        assert a('10') is True

    def test_three(self):
        a = predicats.present()
        assert a([]) is True

    def test_four(self):
        a = predicats.present()
        assert a(None) is False


class Test_pred_Class(object):
    def test_one(self):
        a = predicats.oftype(int)
        b = predicats.pred(a)
        assert b(0) is True

    def test_two(self):
        a = predicats.oftype(int)
        b = predicats.pred(a)
        assert b('10') is False

    def test_three(self):
        a = predicats.eq(0)
        b = predicats.pred(a)
        assert b([]) is False

    def test_four(self):
        a = predicats.eq(0)
        b = predicats.pred(a)
        assert b(0) is True


class Test_operator_and_Class(object):
    def test_one(self):
        a = predicats.oftype(int)
        b = predicats.gt(0)
        c = a & b
        assert c(10) is True

    def test_two(self):
        a = predicats.oftype(int)
        b = predicats.gt(0)
        c = a & b
        assert c(-10) is False

    def test_three(self):
        a = predicats.eq(0)
        b = predicats.gt(10)
        c = a & b
        assert c(-1) is False

    def test_four(self):
        a = predicats.gt(0)
        b = predicats.eq(2)
        c = a & b
        assert c(2) is True


class Test_operator_or_Class(object):
    def test_one(self):
        a = predicats.oftype(int)
        b = predicats.gt(0)
        c = a | b
        assert c(10) is True

    def test_two(self):
        a = predicats.oftype(int)
        b = predicats.gt(0)
        c = a | b
        assert c(-10) is True

    def test_three(self):
        a = predicats.eq(0)
        b = predicats.gt(10)
        c = a | b
        assert c(-1) is False

    def test_four(self):
        a = predicats.gt(0)
        b = predicats.eq(2)
        c = a | b
        assert c(2) is True


class Test_operator_invert_Class(object):
    def test_one(self):
        a = predicats.oftype(int)
        assert ~a(10) is False

    def test_two(self):
        a = predicats.gt(0)
        assert ~a(10) is True

    def test_three(self):
        a = predicats.eq(0)
        b = predicats.gt(10)
        c = a | b
        assert ~c(-1) is True

    def test_four(self):
        a = predicats.gt(0)
        b = predicats.eq(2)
        c = a | b
        assert ~~c(1) is True


class Test_operator_rshift_Class(object):
    def test_one(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = a >> b
        assert c(10) is False

    def test_two(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = a >> b
        assert c(3) is True

    def test_three(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = a >> b
        assert c(-10) is True

    def test_four(self):
        a = predicats.gt(0)
        b = predicats.lt(-5)
        c = a >> b
        assert c(-2) is True


class Test_for_any_Class(object):
    def test_one(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = predicats.for_any(a, b)
        assert c(10) is True

    def test_two(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = predicats.for_any(a, b, a)
        assert c(10) is True

    def test_three(self):
        a = predicats.gt(0)
        b = predicats.lt(-5)
        c = predicats.for_any(a, b)
        assert c(-3) is False

    def test_four(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = predicats.for_any(a, b)
        assert c(-10) is True


class Test_for_all_Class(object):
    def test_one(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = predicats.for_all(a, b)
        assert c(3) is True

    def test_two(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = predicats.for_all(a, b, a)
        assert c(10) is False

    def test_three(self):
        a = predicats.gt(0)
        b = predicats.lt(5)
        c = predicats.for_all(a, b)
        assert c(-3) is False

    def test_four(self):
        a = predicats.gt(0)
        b = predicats.lt(-5)
        c = predicats.for_all(a, b)
        assert c(-3) is False
