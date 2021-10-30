#Base
def Format(text):
    Clean_list=[i.strip() for i in text.replace("\n", "").replace("\f", "").split(',')]
    JSON={}
    for index in range(len(Clean_list)):
        JSON[index]=Clean_list[index]
    return JSON
