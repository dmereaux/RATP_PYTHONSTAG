import sys
sys.path.append('src')
from calcul_tarif import calcul_tarif
import pytest
from unittest.mock import Mock


@pytest.fixture
def fix_setUpTearDown():
    print("before")
    yield
    print("after")

def test_enfant_parisien():
    calcul = calcul_tarif()
    y=calcul.tarif(4,True)
    assert y == 1.4
