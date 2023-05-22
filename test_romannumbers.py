import pytest
from romannumbers import entero_a_romano, RomanNumberError

def test_uno_es_palito():
    assert entero_a_romano(1) == 'I'

def test_dos_es_palito_palito():
    assert entero_a_romano(2) == 'II'

def test_tres_es_palito_tres_veces():
    assert entero_a_romano(3) == 'III'

def test_cuatro_es_palito_V():
    assert entero_a_romano(4) == 'IV'

def test_cinco_es_V ():
    assert entero_a_romano(5) == 'V'

def test_seis_es_uve_palito():
    assert entero_a_romano(6) == 'VI'

def test_siete_es_uve_palito_palito():
    assert entero_a_romano(7) == 'VII'

def test_ocho_es_uve_palito_palito_palito():
    assert entero_a_romano(8) == 'VIII'

def test_nueve_es_palito_equis():
    assert entero_a_romano(9) == 'IX'

def test_diez_es_equis():
    assert entero_a_romano(10) == 'X'

def test_veinte_es_dos_equis():
    assert entero_a_romano(20) == 'XX'

def test_resto_de_cadenas():
    assert entero_a_romano(30) == 'XXX'
    assert entero_a_romano(40) == 'XL'
    assert entero_a_romano(50) == 'L'
    assert entero_a_romano(60) == 'LX'
    assert entero_a_romano(70) == 'LXX'
    assert entero_a_romano(80) == 'LXXX'
    assert entero_a_romano(90) == 'XC'
   # assert entero_a_romano(100) == 'C'

def test_once_es_equis_palito():
    assert entero_a_romano(11) == 'XI'

def test_101_es_C_palito():
    assert entero_a_romano(101) == 'CI'

def test_cero_es_nada ():
    assert entero_a_romano (0) == ''

def test_numeros_rarunos():
    assert entero_a_romano (2345) == 'MMCCCXLV'
    assert entero_a_romano (3999) == 'MMMCMXCIX'

def test_4000_es_error():
    with pytest.raises(RomanNumberError):
        
        entero_a_romano(4000)