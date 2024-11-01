#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Runs an infinite while loop that sleeps 1 second in each loop
 *
 * Return: 0 always (success)
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: 0 on success
 */
int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid > 0)
        {
            /* Parent process */
            printf("Zombie process created, PID: %d\n", pid);
        }
        else if (pid == 0)
        {
            /* Child process exits to become a zombie */
            exit(0);
        }
        else
        {
            perror("fork");
            return (1);
        }
    }

    infinite_while();
    return (0);
}

