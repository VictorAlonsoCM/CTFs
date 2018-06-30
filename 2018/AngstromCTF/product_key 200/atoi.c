#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   char numPtr[5] = "ABCD";
   char email[32] = "artemis.tosini@example.com";
   char name[32] = "Artemis Tosini";
   char serial[10] = "ABCD-EFGH";
   int arreglo_serial[3];
   int v3 = 0;
   int contador_var_C8 = 0;
   char *nptr;

   printf( "Convirtiendo la cadena \"%s\" en un numero: %d\n", numPtr, atoi(numPtr) );

	for ( nptr = strtok(serial, "-"); nptr; nptr = strtok(0LL, "-") )
  {
    v3 = contador_var_C8++;
    arreglo_serial[v3] = atoi(nptr);
    puts(arreglo_serial[v3]);
  }
  char acumulador[BUFSIZ];

  setbuf( stdout, acumulador );

  printf( "Esto es una prueba\n" );
  printf( "Este mensaje se mostrara a la vez\n" );
  printf( "setbuf, acumula los datos en un puntero\n" );
  printf( "hasta que se llene completamente\n" );

  fflush( stdout );
	
   return 0;
}
