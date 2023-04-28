#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
int l;
int main(int argc, string argv[])

{
    // Ensure single line command line argument
    if (argc != 2)
    {
        printf("Usage:  ./ceasar key\n");
        return 1;
    }

    // reject everything thats not a number
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage:  ./ceasar key\n");
            return 1;
        }
    }
    // convert argument to an integer
    int key = atoi(argv[1]);
    // ask the user for some text
    string plaintext = get_string("plaintext: ");
    // encrypt every given character

    printf("ciphertext: ");
    for (l = 0; l < strlen(plaintext); l++)
    {
        if (isupper(plaintext[l]))
        {
            printf("%c", (plaintext[l] - 65 + key) % 26 + 65);
        }
        else if (islower(plaintext[l]))
        {
            printf("%c", (plaintext[l] - 97 + key) % 26 + 97);
        }
        else
        {
            printf("%c", plaintext[l]);
        }
    }

    // printf the encypher text
    printf("\n");
    return 0;
}

int *max = width - j;
int *min = j;
if (min != max)
{
    int tmp = *min;
    *min = *max;
    *max = tmp;
}

int tmp = (*image)[i][j].rgbtRed;
(*image)[i][j].rgbtRed = (*image)[i][width - j].rgbtRed;
(*image)[i][width - j].rgbtRed = tmp;

./ filter - r images / yard.bmp new.bmp./ filter - r images / 3e.bmp new.bmp./ filter - r 4e.bmp new.bmp

                                                                                        // For every corner case in red

                                                                                        // top left corner

                                                                                        for (int j = 0; j < width; j++)
{
    // For every corner case in red

    // top left corner
    if (i - 1 < 0 && j - 1 < 0)
    {
        image[i - 1][j - 1].rgbtRed = 0;
    }
    // bottom left corner
    if (i + 1 > height && j - 1 > height)
    {
        image[i + 1][j - 1].rgbtRed = 0;
    }
    // top right corner

    if (i - < 0 && j + 1 > width)
    {
        image[i - 1][j + 1].rgbtRed = 0;
    }
    // bottom rigth corner
    if (i + 1 > height && j + 1 > width)
    {
        image[i + 1][j + 1].rgbtRed = 0;
    }

    // For every in between pixel

    // middle left pixel
    if (j - 1 < 0)
    {
        image[i][j - 1].rgbtRed = 0;
    }
    // bottom middle pixel
    if (i + 1 > heigth)
    {
        image[i + 1][j].rgbtRed = 0;
    }
    // middle right pixel
    if (j + 1 > width)
    {
        image[i][j + 1].rgbtRed = 0;
    }
    // top middle pixel
    if (i - 1 < 0)
    {
        image[i - 1][j].rgbtRed = 0
    }
