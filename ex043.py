p = float(input('Qual o seu peso: '))
a = float(input('Qual sua altura: '))
print('TABELA')
print('='*10)
print('\033[1;33;40mABAIXO DE 18.5:ABAIXO DO PESO\033[m')
print('\033[1;32;107mENTRE 18.5 ATÉ 25:PESO IDEAL\033[m')
print('\033[1;30;107m25 E 30:SOBREPESO\033[m')
print('\033[1;31;40m ATÉ 40:OBESIDADE\033[m')
print('\033[1;31;40mACIMA DE 40:OBESIDADE MORBIDA\033[m')
print('='*10)
c = (p/a**2)
if c <= 18.5:
    print('\033[1;33;40mVocê está abaixo do peso {:.2f}\033[m'.format(c))
elif 18.5 <= c < 25:
    print('\033[1;32;107mPeso normal {:.2f}\033[m'.format(c))
elif 25 <= c < 30:
    print('\033[1;30;107mSobrepeso {:.2f}\033[m'.format(c))
elif 30 <= c < 40:
    print('\033[1;31;40mObesidade {:.2f}\033[m'.format(c))
elif c >= 40:
    print('\033[1;31;40mObesidade Morbida procure ajuda imediatamente você corre graves riscos a saúde! {:.2f}\033[m'.format(c))
