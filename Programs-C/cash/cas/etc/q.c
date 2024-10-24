#include <cs50.h>
#include <stdio.h>

int main(void)
{
   int c;
   do
   {
    c = get_int("How many cents: ");
   }
   while (c <= 0);
   int q;
   do
   

   q = get_int(c / 25);


   printf("%iquarters\n", c / 25);
}