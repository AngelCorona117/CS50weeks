#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask for a number of layers
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // add columns
    for (int i = 0; i < n; i++)
    {
        // add dots/ spaces
        for (int j = 0; j < n - 1 - i; j++)
        {
            printf(" ");
        }
        // add layers
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        // go to next row
        printf("\n");
    }
}
