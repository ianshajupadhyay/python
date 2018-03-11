def lengs(s):
    if(type(s) == int):
        return "Sorry int type"
    elif(type(s) == float):
        return "Sorry float type"
    else:
        return len(s)

print(lengs(9))
