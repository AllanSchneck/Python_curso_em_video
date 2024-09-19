s = float(input('Qual seu salário atual?'))
m = (s/100*10+s)
m1 = (s/100*15+s)
if (s<=1250):
    print('\033[1;30;42mSeu salário teve aumento de {} Parabéns!\033[m'.format(m1))
else:
    print('\033[1;30;44mSeu salário teve aumento de {} Parabéns!\033[m'.format(m))