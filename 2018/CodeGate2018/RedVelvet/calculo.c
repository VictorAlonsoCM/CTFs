#include <stdio.h>
#include <math.h>

int main(){
	
	long a1;
	long a2;
	long b = 0;
	
	for(a1 = 86; a1 <= 96; a1++){
		
		for(a2 = 97; a2 <= 112; a2++){
			
			if ( (a1 * 2 * (a2 ^ a1) - a2) == 10858){
				
				printf("%ld %ld\n", a1, a2);
				
			}
			
		}
	}
	
	return 0;
}
