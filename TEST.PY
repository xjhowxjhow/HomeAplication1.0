
import locale
def _brl_to_usd(valor):
    new_string = valor
    to_remove = "."
    for x in to_remove:
        new_string = new_string.replace(x, '')
        new_string = new_string.replace(',','.')
    return new_string
    
    

def _usd_to_brl(valor):
    valor = float(valor) 
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor, grouping=True, symbol=True)
    return ('%s' % valor)

print(_brl_to_usd('1.004,45'))


