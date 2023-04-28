// Implements a dictionary's functionality
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"
#include <string.h>
#include <math.h>
#include <strings.h>

int Nstring = 0;
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1]; // string
    struct node *next;     // pointer to next element
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 3000;

// Hash table
node *table[N];
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int word_s = hash(word);

    node *cursor = table[word_s];

    while (cursor != NULL)
    {
        if ((strcasecmp(cursor->word, word)) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    return false;
}
// if is not in the dictionary

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += toupper(word[i]);
    }
    return round(sum % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // open dictionary file
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // read strings from file one at a time
    char *buffer = malloc(sizeof(char) * LENGTH + 1);
    while (fscanf(input, "%s", buffer) == 1)
    {
        // create a new node for each word
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            printf("Could not open file.\n");
            return 1;
        }
        strcpy(newNode->word, buffer);
        // insert node into hash node at that location
        newNode->next = table[hash(newNode->word)];
        table[hash(newNode->word)] = newNode;
        Nstring++;
    }
    free(buffer);
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    return Nstring;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int j = 0; j < N; j++)
    {
        node *tmp = table[j];
        while (tmp != NULL)
        {
            node *cursor = tmp->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
