#include <stdlib.h>

int maxDepth(char *s)
{
    int max_depth = 0;
    int counter = 0;

    while (*s != '\0')
    {
        if (*s == '(')
        {
            counter++;
            max_depth = (max_depth > counter) ? max_depth : counter;
        }
        else if (*s == ')')
        {
            counter--;
        }
        s++;
    }
    return max_depth;
}

int main()
{
    char *s = "(1)+((2))+(((3)))";
    int result = maxDepth(s);
    printf("%d\n", result);
}