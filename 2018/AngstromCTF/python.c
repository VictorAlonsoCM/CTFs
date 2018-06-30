//Agregamos la librería Python para usar la API
#include <Python.h>
int main () {
        /*Instanciamos un interprete que crea un __main__
        Podemos pasarle argumumentos a ese __main__ pero
        en este caso, lo instanciamos sin pasar nada */
    Py_Initialize();    


        //Aquí podremos usar la API  


        /*Cerramos el interprete, podremos instanciar otro
         más adelante */
    Py_Finalize();

    return 1;
}
