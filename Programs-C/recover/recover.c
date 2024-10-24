#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;

void CheckArgumentCount(int argc);
int isJPEG(BYTE buffer[]);

int main(int argc, char *argv[])
{
    CheckArgumentCount(argc);

    FILE *raw = fopen(argv[1], "rb"); // Open in binary mode
    if (raw == NULL)
    {
        fprintf(stderr, "Could not open file %s\n", argv[1]);
        return 1;
    }

    // Allocate necessary memory and initialize variables:
    BYTE buffer[BLOCK_SIZE];

    char filename[12];  // To accommodate filenames like "001.jpg"
    FILE *image = NULL; // Initialize to NULL
    int counter = 0;

    while (fread(buffer, BLOCK_SIZE, 1, raw) == 1)
    {
        if (isJPEG(buffer) == 1)
        {
            if (image != NULL)
            {
                fclose(image);
            }
            sprintf(filename, "%03i.jpg", counter++);
            image = fopen(filename, "wb"); // Open in binary mode
            if (image == NULL)
            {
                fprintf(stderr, "Could not create file %s\n", filename);
                fclose(raw);
                return 2;
            }
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
        else if (counter > 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
    }

    if (image != NULL)
    {
        fclose(image);
    }

    fclose(raw);
    return 0;
}

void CheckArgumentCount(int argc)
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        exit(1);
    }
}

int isJPEG(BYTE buffer[])
{
    return (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0);
}