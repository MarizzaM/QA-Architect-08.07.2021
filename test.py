import app
import pytest


@pytest.mark.calc
def test_add_operation():
    assert app.add(5, 7) == 12


@pytest.mark.calc
def test_dif_operation():
    assert app.dif(5, 7) == -2


@pytest.mark.calc
def test_mul_operation():
    assert app.mul(5, 7) == 35


@pytest.mark.calc
def test_div_operation():
    assert app.div(8, 2) == 4


@pytest.mark.calc
def test_make_capital():
    assert app.makeCapital('marizza') == 'Marizza'


@pytest.mark.mytag
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        app.div(5, 0)


def test_mul_by_two():
    with pytest.raises(TypeError):
        app.mul_by_two()


@pytest.fixture
def five():
    return 5

@pytest.mark.calc
def test_add_operation(five):
    assert app.add(five, 7) == 12


@pytest.mark.parametrize("x", [1, 2, 3, 4, 5])
def test_add_operation_parameterize(x):
    assert app.add(5, x) == 5 + x