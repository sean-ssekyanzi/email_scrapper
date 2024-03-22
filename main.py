def file_reader(filename:str)->str:
    try:
        with open(filename,'r') as file:
            # read_content = file.read()
            for item in file:
                print(item)
    except Exception as e:
        print("An error occured:", str(e))


def grabs_url()->str:
    pass





if __name__ == "main":
    print("This is the main block")
    file_reader("file.txt")