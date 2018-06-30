from binascii import unhexlify as sOup
from operator import attrgetter as souP

ME_FLAGE = '<censored>'

Entrada_Datos = input
hexa = hex
imprimir = print
ord_ = ord
open_ = open

def SoUP(sOUP):
    soup = 0
    while sOUP != 0:
        soup = (soup * 10) + (sOUP % 10)
        sOUP //= 10
    return soup

def SOup(sOUP):
    soup = 0
    for soUp in sOUP:
        soup *= 10
        soup += ord_(soUp) - ord_('0')
    return soup

def SOUP():
    Soup = Entrada_Datos()[:7]
    print(Soup)
    if not souP('isdigit')(Soup)():
        imprimir("that's not a number lol")
        return

    soup = SoUP(SOup(Soup))
    SouP = souP('zfill')(hexa(soup)[2:])(8)[-8:]
    if sOup(SouP) == souP('encode')('s0up')():
        imprimir("oh yay it's a flag!", ME_FLAGE)
    else:
        imprimir('oh noes rip u')

if __name__ == '__main__':
    SOUP()

