#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char pad[64];
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  char name[48]; // [rsp+10h] [rbp-90h]
  char email[48]; // [rsp+40h] [rbp-60h]
  char serial[40]; // [rsp+70h] [rbp-30h]
  unsigned __int64 v7; // [rsp+98h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  printf("Name: ", argv, envp, argv);
  fgets(name, 33, stdin);
  name[strcspn(name, "\n")] = 0;
  printf("Email: ", "\n");
  fgets(email, 33, stdin);
  email[strcspn(email, "\n")] = 0;
  printf("Product key: ", "\n");
  fgets(serial, 33, stdin);
  serial[strcspn(serial, "\n")] = 0;
  if ( (unsigned __int8)verify_key((__int64)name, (__int64)email, serial) )
  {
    puts("Windows has been activated");
    result = 0;
  }
  else
  {
    puts("Invalid product key");
    result = -1;
  }
  return result;
}
int verify_key(__int64 name, __int64 email, char *serial)
{
  int v3; // ebx
  int v5_var_98; // ST58_4
  int v6; // ebx
  int v7; // ebx
  unsigned __int8 v8; // [rsp+27h] [rbp-C9h]
  int contador_var_C8; // [rsp+28h] [rbp-C8h]
  int v11; // [rsp+2Ch] [rbp-C4h]
  signed int i; // [rsp+30h] [rbp-C0h]
  int j; // [rsp+34h] [rbp-BCh]
  signed int k; // [rsp+38h] [rbp-B8h]
  signed int l_var_B4; // [rsp+3Ch] [rbp-B4h]
  signed int l; // [rsp+40h] [rbp-B0h]
  signed int m; // [rsp+44h] [rbp-ACh]
  signed int n; // [rsp+48h] [rbp-A8h]
  signed int jj_var_A4; // [rsp+4Ch] [rbp-A4h]
  signed int length_e_1_v19; // [rsp+50h] [rbp-A0h]
  const char *nptr; // [rsp+60h] [rbp-90h]
  char *v21; // [rsp+68h] [rbp-88h]
  __int64 e_v22; // [rsp+70h] [rbp-80h]
  __int64 n_v23; // [rsp+78h] [rbp-78h]
  int arreglo_serial[8]; // [rsp+80h] [rbp-70h]
  int v25; // [rsp+A0h] [rbp-50h]
  int v26; // [rsp+A4h] [rbp-4Ch]
  int v27; // [rsp+A8h] [rbp-48h]
  int v28; // [rsp+ACh] [rbp-44h]
  int v29; // [rsp+B0h] [rbp-40h]
  int v30; // [rsp+B4h] [rbp-3Ch]
  int v31; // [rsp+C0h] [rbp-30h]
  int v32; // [rsp+C4h] [rbp-2Ch]
  int v33; // [rsp+C8h] [rbp-28h]
  int v34; // [rsp+CCh] [rbp-24h]
  int v35; // [rsp+D0h] [rbp-20h]
  int v36; // [rsp+D4h] [rbp-1Ch]
  unsigned __int64 v37; // [rsp+D8h] [rbp-18h]

  v37 = __readfsqword(40u);
  contador_var_C8 = 0;
  for ( nptr = strtok(serial, "-"); nptr; nptr = strtok(0LL, "-") )
  {
    v3 = contador_var_C8++;
    arreglo_serial[v3] = atoi(nptr);
  }
  if ( contador_var_C8 != 6 )
    return 0LL;
  v11 = 0;
  e_v22 = email;                                // lenght 26
  n_v23 = name;
  for ( i = 0; i <= 1; ++i )                    // ejecuta 2 veces
  {
    v21 = (char *)*(&e_v22 + i);
    length_e_1_v19 = strlen((const char *)*(&e_v22 + i));// longitud correo +1
    if ( length_e_1_v19 <= 31 )                 // true
    {
      for ( j = 0; j < 32 - length_e_1_v19; ++j )// se ejecuta 5 veses si es 26 si no 4
        v21[length_e_1_v19 + j] = pad[v11 + j];
      v11 = 32 - length_e_1_v19;
      v21[32] = 0;
    }
  }
  for ( k = 0; k <= 31; ++k )
  {
    (k + email) ^= 5u;
    (k + name) ^= 0xFu;
  }
  for ( l_var_B4 = 0; l_var_B4 <= 5; ++l_var_B4 )
  {
    v5_var_98 = sumChars(email, 0, 32, l_var_B4 + 2);
    arreglo_serial[l_var_B4] -= (signed int)((unsigned __int64)sumChars(email, l_var_B4 + 1, 32, l_var_B4 + 2)
                                           * v5_var_98)
                              % 10000;
    v6 = sumChars(name, 0, 32, 2);
    arreglo_serial[l_var_B4] += 4 * (v6 - (unsigned __int64)sumChars(name, 1, 32, 2));
  }
  swapArr((__int64)arreglo_serial, 3, 4);
  swapArr((__int64)arreglo_serial, 2, 5);
  swapArr((__int64)arreglo_serial, 1, 5);
  swapArr((__int64)arreglo_serial, 2, 3);
  swapArr((__int64)arreglo_serial, 0, 5);
  swapArr((__int64)arreglo_serial, 4, 5);
  for ( l = 0; l <= 5; ++l )
  {
    arreglo_serial[l] += sumChars(name, 0, 32, 1);
    arreglo_serial[l] += sumChars(email, 0, 32, 1);
  }
  for ( m = 0; m <= 5; ++m )
  {
    v7 = sumChars(email, 4 * m, 4 * m + 1, 1);
    arreglo_serial[m] += v7 % (signed int)sumChars(name, 4 * m + 2, 4 * m + 3, 1);
  }
  v25 = 2;
  v26 = 4;
  v27 = 6;
  v28 = 8;
  v29 = 7;
  v30 = 5;
  v31 = sumChars(email, 0, 10, 1);
  v32 = sumChars(email, 10, 25, 1);
  v33 = sumChars(email, 25, 32, 1);
  v34 = sumChars(name, 0, 13, 1);
  v35 = sumChars(name, 13, 20, 1);
  v36 = sumChars(name, 20, 32, 1);
  for ( n = 0; n <= 5; ++n )
    *(&v31 + n) = *(&v31 + n) * *(&v25 + n) % 10000;
  v8 = 1;
  for ( jj_var_A4 = 0; jj_var_A4 <= 5; ++jj_var_A4 )
  {
    if ( arreglo_serial[jj_var_A4] != *(&v31 + jj_var_A4) )
      v8 = 0;
  }
  return v8;
}
