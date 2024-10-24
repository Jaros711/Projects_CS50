#include <cs50.h>
#include <stdio.h>

int main(void)
{
   int cents;
   do
   {
    cents = get_int("How many cents: ");
   }
   while (cents <= 0);
}
