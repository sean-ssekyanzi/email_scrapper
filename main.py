# def file_reader(filename:str)->str:
#     print(f" reading files in {filename}")
#     return filename
    

def company_reader(filename:str)->str:
    try:
        with open('file.txt','r') as file:
            # read_content = file.read()
            for item in file:
                print(item.rstrip("\n"))
    except Exception as e:
        print("An error occured:", str(e))


def grabs_url()->str:
    pass





if __name__ == "main":
    print("This is the main block")
    
    
    