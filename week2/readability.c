#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{

    // ask the user for Input
    string text = get_string("Text: ");

    // calculate number of letters

    int count_letters(char *text);

    int letters = 0;
    int l;

    for (l = 0; l < strlen(text); l++)
    {
        if (isalpha(text[l]))

        {
            letters++;
        }
    }

    // calculate number of words

    int count_words(char *text);

    int words = 1;
    int w;

    for (w = 1; w < strlen(text); w++)

    {
        if (text[w] == ' ')
        {
            words++;
        }
    }

    // calculate number of sentences
    int count_words(char *text);
    int sentences = 0;
    int s;

    for (s = 0; s < strlen(text); s++)

    {
        if (text[s] == '!' || text[s] == '.' || text[s] == '?')
        {
            sentences++;
        }
    }

    // Calculate Coleman-Liau Index Formula

    float L = 100.0 * ((float)letters / (float)words);

    float S = 100.0 * ((float)sentences / (float)words);

    float grade = (0.0588 * L - 0.296 * S - 15.8);
    int x = round(grade);
    // grade 16+
    if (x > 16)
    {
        printf("Grade 16+\n");
    }
    // grade before grade 1
    else if (x < 1)
    {
        printf("Before Grade 1\n");
    }

    // anything in between 1 and 16
    else
    {
        printf("Grade %i\n", x);
    }
}

 plaintext;
      for (i = 0; i < n; i++)
            if (isalpha(argv[1][i]))
            {

                  printf( "%i+ %i", character);
            }


x=grade
if x > 16:
    print("Grade 16+";
elif x < 1:
    print("Before Grade 1")
 else:
    print(f"Grade {x}");


x=round(grade)
if x > 16:
    print("Grade 16+")
elif x < 1:
    print("Before Grade 1")
 else:
    print(f"Grade {x}")
