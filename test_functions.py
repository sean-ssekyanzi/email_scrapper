from main import company_reader,grabs_url
import pytest

def test_company_reader():
    file = "testfile.txt"
    result = company_reader(file)
    expected = ['umeme','stanbic', 'jesa']
    assert result ==  expected

def test_grabs_url():
    expected = 200
    actual = grabs_url(company_reader='testfile.txt')
    assert actual == expected