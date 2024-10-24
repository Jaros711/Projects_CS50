#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int length;
    do
    {
        length = get_int("Length: ");
    }
    while (length < 1);


    // Declare array
    int twice[length];

    // Set value
    twice[0] = 1;
    printf("%i\n", twice[0]);

    for (int i = 1; i < length; i++)
    {
        // Make multiple 2
        twice[i] = 2 * twice[i - 1];

        // Print
        printf("%i\n", twice[i]);
    }
}