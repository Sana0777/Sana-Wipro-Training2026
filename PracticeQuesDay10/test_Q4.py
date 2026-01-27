import pytest
from Q2_calculator import add,mul

def setup_module(module):
    print("\nSetup Module: testing")


def teardown_module(module):
    print("\nTeardown Module: testing")


def setup_function(function):
    print("\nSetup Function")


def teardown_function(function):
    print("\nTeardown Function")


def test_add_basic(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_mul_basic(sample_numbers):
    a, b = sample_numbers
    assert mul(a, b) == 50

