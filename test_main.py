from main import company_reader
def test_company_reader():
    file = "file.txt"
    result = company_reader(file)
    
    assert result ==  ['stanbic\n', 'jesa\n']
