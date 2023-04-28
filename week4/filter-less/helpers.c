#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop for every single pixel asking what color is that pixel

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gray = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0) * 1.0;
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // define colors before the sepia filter is aplied
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;
            // aply sepia filter for each pixel
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue) * 1.0;
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue) * 1.0;
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue) * 1.0;
            // make sure is less than 255
            image[i][j].rgbtRed = fmin(255, sepiaRed);
            image[i][j].rgbtGreen = fmin(255, sepiaGreen);
            image[i][j].rgbtBlue = fmin(255, sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            // For every pixel on the left side of the screen
            tmp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    // create a temporaty copy of the image
    RGBTRIPLE tmpr[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmpr[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // neighbor pixels within [i][j] as starting value

            float Neighborpixel = 0.00;
            int Red = 0;
            int Green = 0;
            int Blue = 0;
            for (int a = -1; a < 2; a++)
            {
                for (int b = -1; b < 2; b++)
                {
                    int NeighborA = a + i;
                    int NeighborB = b + j;
                    if (NeighborA < 0 || NeighborA > (height - 1) || NeighborB < 0 || NeighborB > (width - 1))
                    {
                        continue;
                    }
                    Red += image[NeighborA][NeighborB].rgbtRed;
                    Green += image[NeighborA][NeighborB].rgbtGreen;
                    Blue += image[NeighborA][NeighborB].rgbtBlue;
                    Neighborpixel++;
                }
                tmpr[i][j].rgbtRed = round(Red / Neighborpixel);
                tmpr[i][j].rgbtGreen = round(Green / Neighborpixel);
                tmpr[i][j].rgbtBlue = round(Blue / Neighborpixel);
            }
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tmpr[i][j].rgbtRed;
            image[i][j].rgbtGreen = tmpr[i][j].rgbtGreen;
            image[i][j].rgbtBlue = tmpr[i][j].rgbtBlue;
        }
    }
    return;
}
