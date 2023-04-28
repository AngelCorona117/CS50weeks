#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <stdint.h>
typedef uint8_t BYTE;
BYTE buffer[5];
int main(int argc, char *argv[])
{
    // 0.-accept only 1 command line argument
    if (argc != 2)
    {
        printf("Usage:  ./recover IMAGE\n");
        return 1;
    }

    // 1.-Open Memory Card
    FILE *input = fopen(argv[1], "r");
    {
        if (input == NULL)
        {
            printf("could not use file\n");
            return 1;
        }
    }
    FILE *output = NULL;
    int imagesfound = 0;
    char *name = malloc(8);

    // 2.-Repeat until end of file
    while (fread(buffer, 1, 512, input) == 512)
    {

        // 4.-look for beggining of jpeg

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (imagesfound == 0)
            {
                // if thats true then its the start of a jpeg file then
                // open a new jpeg
                sprintf(name, "%03i.jpg", imagesfound);
                output = fopen(name, "w");
                imagesfound++;
                // write over it
                fwrite(&buffer, 1, 512, output);
            }
            // if is not the first jpeg
            else if (imagesfound > 0)
            {
                fclose(output);
                sprintf(name, "%03i.jpg", imagesfound);
                output = fopen(name, "w");
                imagesfound++;
                // write over it
                fwrite(&buffer, 1, 512, output);
            }
        }
        // if is not the beggining of a new jpeg
        else if (output != NULL)
        {
            fwrite(&buffer, 1, 512, output);
        }
    }
    free(name);
    fclose(input);
    fclose(output);
    return 0;
}
