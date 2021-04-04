import re
def printer_error(s):
    '''Cuenta el número de errores de impresora (indicados por una letra que no está en a-m)'''
    matches = re.findall(r'[a-m]',s)
    return str(len(s)-len(matches))+'/'+str(len(s))