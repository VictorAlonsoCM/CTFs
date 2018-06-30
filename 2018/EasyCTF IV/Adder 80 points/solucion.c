#include <stdio.h>

int main(){
	
	int v1, v2, v3;
	
	for(v1 = 0; v1 <= 1337; v1++){
		
		for(v2 = 0; v2 <= 1337; v2++){
			
			for(v3 = 0; v3 <= 1337; v3++){
				
				if((v1+v2+v3) == 1337){
					
					printf("Soluciones 1337 =  %d %d %d\n", v1, v2, v3);
					system("pause");
				}
			}
		}
	}
	
	return 0;
}
