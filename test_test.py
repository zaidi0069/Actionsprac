from main import StudentsInMLOps

import pytest

@pytest.fixture
def mlops_class():
    return StudentsInMLOps()

def test_enrollStudents(mlops_class):
    mlops_class.enrollStudents(5)
    assert mlops_class.getTotalStrength() == 5

def test_dropStudents(mlops_class):
    mlops_class.enrollStudents(10)
    mlops_class.dropStudents(3)
    assert mlops_class.getTotalStrength() == 7

def test_getTotalStrength(mlops_class):
    assert mlops_class.getTotalStrength() == 0

def test_getClassName(mlops_class):
    assert mlops_class.getClassName() == "StudentsInMLOps"
