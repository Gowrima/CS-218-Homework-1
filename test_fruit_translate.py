from translate_fruit import *
from fruits_unicode import *

def test_translate_fruit_Kannada():
	expected_ = "Translation of Apple in Kannada is \xe0\xb2\xb8\xe0\xb3\x87\xe0\xb2\xac\xe0\xb3\x81"

	assert expected_ == translate_("Kannada", "Apple")

def test_translate_fruit_Tamil():
	expected_ = "\Translation of Apple in Tamil is \xe0\xae\x86\xe0\xae\x9f\xe0\xaf\x8d\xe0\xae\xaa\xe0\xaf\x8d\xe0\xae\xb3\xe0\xaf\x8d"

	assert expected_ == translate_("Tamil", "Apple")


def test_translate_fruit_Malayalam():
	expected_ = "Translation of Apple in Malayalam is \xe0\xb4\x86\xe0\xb4\xaa\xe0\xb5\x8d\xe0\xb4\xaa\xe0\xb4\xbf\xe0\xb5\xbd"

	assert expected_ == translate_("Malayalam", "Apple")


def test_bad_input():
	expected_ = "Invalid fruit/language"

	assert expected_ == translate_("Hindi", "234")
