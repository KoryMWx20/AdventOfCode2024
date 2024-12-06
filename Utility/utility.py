
def Read(fileName):
    with open(fileName, 'r') as file:
        return file.read()
    
def PrettyPrint(list):
    for row in list:
        print(row)
        
    