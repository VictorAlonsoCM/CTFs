//Fuerza bruta
//Liar 70. easectf
#include <stdio.h>

int main(){
	
	int n = 1; //Contador que nos dara el flag
	int i = 0; //Contador general
	int m = 0; //Multiplicador por contador de flag
	int flag = 0; //Variable para la detencion del programa
	
	int f[37]; //Arreglo de valores ya conocidos
	char g[38]; //Arreglo donde se genera y guarda el flag
	
	f[30] = 160;
	f[10] = 47;
	f[13] = 4;
	f[25] = 205;
	f[5] = 87;
	f[24] = 247;
	f[6] = 76;
	f[31] = 176;
	f[7] = 74;
	f[34] = 154;
	f[21] = 231;
	f[32] = 135;
	f[8] = 75;
	f[1] = 102;
	f[9] = 75;
	f[28] = 232;
	f[29] = 148;
	f[3] = 108;
	f[11] = 33;
	f[4] = 127;
	f[14] = 21;
	f[18] = 89;
	f[16] = 3;
	f[26] = 215;
	f[20] = 211;
	f[15] = 8;
	f[17] = 25;
	f[27] = 217;
	f[0] = 101;
	f[33] = 143;
	f[22] = 245;
	f[19] = 241;
	f[12] = 56;
	f[36] = 129;
	f[23] = 206;
	f[2] = 125;
	f[35] = 202;
	
	while(flag==0){
		
		m = n ^ 0x58EB29;
	  	for ( i = 0; i <= 36; ++i ){
	    	g[i] = m * i ^ (unsigned __int64) f[i];
		}
	    g[i] = 0;
	  	if ( g[0] == 101 && g[1] == 97 && g[2] == 115 && g[3] == 121 && g[4] == 99 && g[5] == 116 && g[6] == 102 ){
	  		printf("%d\n", n); //Nos imprime el valor de n que es el correcto
		  	printf("the flag is %s\n", g); //Nos imprime la bandera
		  	flag = 1; //detiene el while
		  }
		else{
			n++;
		}
	}
    
	return 0;
}
