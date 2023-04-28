#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{

    // Get input words from both players
    string word1 = get_string("Player 1: ");

    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner

    if (score1 > score2)
    {
        printf("Player 1 Wins!..");
    }
    else if (score2 > score1)
    {
        printf("Player 2 Wins!..");
    }
    else
    {
        printf("Tie!..");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int score = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        word[i] = toupper(word[i]);

        if (isupper(word[i]))
        {
            score += POINTS[toupper(word[i]) - 65];
        }
    }
    return score;
}

for (int l = 0; l < strlen(text); l++)

if (grade > 1 )

    printf("Before grade 1\n");

    else if (grade < 16)

    printf("Grade 16+\n");
    else
    printf("Grade: %f\n", grade);


      for (int i = 0; i < text[i]; i++)
    {
        text[i] = toupper(text[i]);
    }

       // Calculate Coleman-Liau Index Formula

    float L = 100.0 * ((float)letters / (float)words);

    float S = 100.0 * ((float)sentences / (float)words);

    float grade = 0.058 * L - 0.296 * S - 15.8;
    int x = round(grade);

   }

