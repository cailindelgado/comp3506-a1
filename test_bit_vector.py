import pytest

from random import randrange as rand
from structures.bit_vector import BitVector as bv

class TestBitVectorBasics:

    @pytest.fixture
    def bit_vector(self):
        return bv()

    def test_init(self, bit_vector):
        assert bit_vector._data._array == [None, None, None, None]
        assert bit_vector._MSB == 0
        assert bit_vector._LSB == 0

    def test_append(self, bit_vector):
        bit_vector.append(3)
        bit_vector.append(3)
        bit_vector.append(0)
        bit_vector.append(3)
        bit_vector.append(3)
        assert bit_vector._MSB == 5
        assert bit_vector._LSB == 0
        assert bit_vector[0] == 1
        print(bit_vector)
        assert bit_vector[1] == 1
        assert bit_vector[2] == 0
        assert bit_vector[3] == 1
        assert bit_vector[4] == 1


# ======= More rigorous testing ======= 
class TestBitVectorAdv:

    @pytest.fixture
    def bit_vector(self):
        return bv()

    def populate(self):
        pass

    def test_adv_append(self):
        pass

    def test_adv_prepend(self):
        pass

    def test_adv_everything(self):
        pass
