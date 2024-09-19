m = int(input('Digite a distancia em metros: '))
cm = (m*100)
mm = (m*1000)
print('\033[4;30;45m{}m tem {}cm e {}mm.\033[m'.format(m, cm, mm))
