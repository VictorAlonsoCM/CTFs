from binascii import unhexlify as binario #Repesentacion en hexadecimal de los binarios
from operator import attrgetter as attrget #Obtiene los atributos de un valor

ME_FLAGE = '<censored>'

Entrada_Datos = input
hexa = hex
ord_ = ord #Retorna el valor de un caracter en codigo ascii
open_ = open

def f1(sumador): #invierte los digitos (123 -> 321).
    divisor = 0
    while sumador != 0:
        divisor = (divisor * 10) + (sumador % 10)
        sumador //= 10 #Divisor de enteros
    return divisor

def f2_ord(dato): #los convierte a entero
    sumador = 0 #Este valor se va a retorna
    for conta in dato:
        sumador *= 10
        sumador += ord_(conta) - ord_('0') #'0' = 47
    return sumador

def f3_entrada():
    dato = Entrada_Datos()[:7] #Lee datos a una longitud de 7 como un arreglo
    print(dato)
    #Comprueba que sea un digito
    if not attrget('isdigit')(dato)(): #0 1 2 3 4 5 6 7 8 9 ² ³ ¹ ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ ߀ ߁ ߂ ߃ ߄ ߅ ߆ ߇ ߈ ߉ ० १ २ ३ ४ ५ ६ ७ ८ ९
        print("that's not a number lol")
        return

    varlodefunciones = f1(f2_ord(dato))
    varlodefunciones2 = attrget('zfill')(hexa(varlodefunciones)[2:])(8)[-8:]
    if binario(varlodefunciones2) == attrget('encode')('s0up')(): #El valor en hexa de esta funcion es 0x73307570 = 1932555632 =  2365552391
        print("oh yay it's a flag!", ME_FLAGE)
    else:
        print('oh noes rip u')

if __name__ == '__main__':
    f3_entrada() #७552391 =  2365552391
                            #1932555623

