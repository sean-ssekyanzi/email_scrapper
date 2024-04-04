def company_reader(filename:str)->list:
    print(f" reading companies in {filename}")
    companies = []
    try:
        with open(filename,'r') as file:
            for item in file:
                companies.append(item)
                # print(item.rstrip("\n"))
                print(companies)
                
    except Exception as e:
        print("An error occured:", str(e))
    return companies
        

# def grabs_url(company_name:str)->str:
#     print(f"accessing {company_name}")






if __name__ == "main":
    print("Initialising")
    
    
    