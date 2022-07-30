n = eval(input())
def type_det(n):
    
    if type(n)==int:
        return "int"
    elif type(n)==float:
        return "float"   
    else:
        return "str"
     
print(type_det(n))
