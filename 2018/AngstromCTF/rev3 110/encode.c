#include<stdio.h>
#include<conio.h>
 
char* encode(char* str) {
   int i = 0;
 
   while (str[i] != '\0') {
      str[i] = str[i] - 30;  // Subtract 30 From Charcter
      i++;
   }
   return (str);
}
 
void main() {
 
   char *str;
 
   printf("\nEnter the String to be Encode : ");
   gets(str);
 
   str = encode(str);
   printf("\nEncoded String : %s", str);
 
   getch();
}
