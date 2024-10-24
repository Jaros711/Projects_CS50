#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start, end, years = 0;
    do
    {
        printf("Enter starting population size (minimum9): ");
        scanf("%d", &start);
    }
    while (start < 9);

    // Prompt for end size
    do
    {
        printf("Enter ending population size (minimum %d): ", start);
        scanf("%d", &end);
    }
    while (end < start);

    // Calculate number of years until we reach threshold
    while (start < end)
    {
        start = start + start / 3 - start / 4;
        years++;
    }

    // Print number of years
        printf("Years: %d\n", years);
    return 0;
}