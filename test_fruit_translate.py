from translate_fruit import *
from fruits_unicode import *

def test_translate_fruit_Kannada():
	expected_ = "\u0cb8\u0cc7\u0cac\u0cc1"

	assert expected_ == translate_fruit.translate_("Kannada", "Apple")

def test_translate_fruit_Tamil():
	expected_ = "\u0b86\u0b9f\u0bcd\u0baa\u0bcd\u0bb3\u0bcd"

	assert expected_ == translate_fruit.translate_("Tamil", "Apple")


def test_translate_fruit_Malayalam():
	expected_ = "\u0d06\u0d2a\u0d4d\u0d2a\u0d3f\u0d7d"

	assert expected_ == translate_fruit.translate_("Malayalam", "Apple")


def test_bad_input():
	expected_ = "Invalid fruit/language"

	assert expected_ == translate_fruit.translate_("Hindi", "234")
