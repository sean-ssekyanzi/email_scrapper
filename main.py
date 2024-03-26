def company_reader(filename:str)->str:
    print(f" reading companies in {filename}")
    try:
        with open(filename,'r') as file:
            # read_content = file.read()
            for item in file:
                print(item.rstrip("\n"))
                return item
    except Exception as e:
        print("An error occured:", str(e))

        

def grabs_url(company_name:str)->str:
    print(f"accessing {company_name}")






if __name__ == "main":
    print("This is the main block")
    
    
    