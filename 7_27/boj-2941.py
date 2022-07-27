multiple_alphas_and_symbols = ['c=','c-','dz=','d-','lj','nj','s=','z=']

cro_alpha = input()

for check in multiple_alphas_and_symbols:
    cro_alpha = cro_alpha.replace(check, '1')
print(len(cro_alpha))