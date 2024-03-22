def file_reader():
    with open("file.txt",'r') as file:
        # read_content = file.read()
        for item in file:
            print(item)







if __name__ == "main":
    print("This is the main block")
    