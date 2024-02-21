from translate_fruit import *
from fruits_unicode import *

def test_translate_fruit_Kannada():
	expected_ = 'Translation of Apple in Kannada is ಸೇಬು'
	assert expected_ == translate_("Kannada", "Apple")

def test_translate_fruit_Tamil():
	expected_ = 'Translation of Apple in Tamil is ஆட்ப்ள்'

	assert expected_ == translate_("Tamil", "Apple")


def test_translate_fruit_Malayalam():
	expected_ = 'Translation of Apple in Malayalam is ആപ്പിൽ'

	assert expected_ == translate_("Malayalam", "Apple")


def test_bad_input():
	expected_ = "Invalid fruit/language"

	assert expected_ == translate_("Hindi", "234")
