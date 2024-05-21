from main import company_reader,grabs_page
import pytest
from unittest.mock import patch, MagicMock
import unittest




def test_company_reader():
    file = "testfile.txt"
    result = company_reader(file)
    expected = ['umeme','stanbic', 'jesa']
    assert result ==  expected

@patch('functions.grabs_page')
def test_grabs_page(mock_requests):
    company = "new vision"
    mock_response = MagicMock()
    mock_response.text = "success"
    mock_requests.get.return_value = mock_response
    actual = grabs_page(company)
    assert mock_response == actual  