def intToRoman(num: int) -> str:
  rom = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
  arr = []
  nums = num
  div = [1000, 100, 10, 1]
  divi = 0
  res = ''
  while nums > 0:
      temp = nums // div[divi]  
      arr.append(temp * div[divi])
      nums -= temp * div[divi] 
      divi+=1            
  #print(arr)
  for i in range(len(arr)):
      if arr[i] % div[i] == 0:
          temp = arr[i] // div[i] 
          # res += rom[div[i]] * temp
          if div[i] * temp in rom:
            res += rom[div[i] * temp]
          else:
             #print(div[i] * temp)
             if div[i] != 0:
                if div[i] * temp <= 3:
                   res += rom[div[i]] * temp
                elif div[i] * temp <= 8:
                   res += 'V' + 'I' * (temp - 5)
                elif div[i] * temp <= 30:
                   res += rom[div[i]] * temp
                elif div[i] * temp <= 80:
                   res += 'L' + 'X' * (temp - 5)
                elif div[i] * temp <= 300:
                   res += rom[div[i]] * temp
                elif div[i] * temp <= 800:
                   res += 'D' + 'C' * (temp - 5)
                elif div[i] == 1000:
                   res += rom[div[i]] * temp
      else:
          continue 
  return res


print(intToRoman(58)) # LVIII
print(intToRoman(3749)) # MMMDCCXLIX 
#print(intToRoman(49))
print(intToRoman(1994))