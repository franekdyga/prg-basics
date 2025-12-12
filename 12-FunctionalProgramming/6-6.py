employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

print('\n'.join(list(map(lambda x:x[0].upper() + ',' + x[1], employees))))