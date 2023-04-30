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
