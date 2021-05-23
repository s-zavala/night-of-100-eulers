def lpp():
  largest = 0; I, J = 0,0
  
  for i in range(100, 999):
    for j in range(i+1, 999 ):
      product = str(i*j)
      if product == product[::-1]:
        if int(product) > largest:
          largest = int(product)
          I, J = i, j
          break
  return largest

# print(lpp())

def largest_palindrome():
    search = (num for num in range(999, 101, -1))
    
    

largest_palindrome()