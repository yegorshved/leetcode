def gcdOfStrings(str1: str, str2: str) -> str:
    
    lenstr1 = len(str1)
    lenstr2 = len(str2)
    
    s = str1 if lenstr1 > lenstr2 else str2
    
    divider = ''
    biggest_divider = ''
    for i in s:
        divider += i
        
        if divider in str1 and divider in str2:
            mul1 = lenstr1 // len(divider)
            mul2 = lenstr2 // len(divider)
            if divider * mul1 == str1 and divider * mul2 == str2:
                biggest_divider = divider if len(divider) > len(biggest_divider) else biggest_divider
    
   
    return biggest_divider

str1 = "ABABABAB"
str2 = "ABAB"
output = "ABAB"
print(f'result: {gcdOfStrings(str1, str2)}, expected: {output}')