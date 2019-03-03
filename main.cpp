#include <cstdio>

int main(int argc, char** argv)
{
    fprintf(stdout, "start:\n");
    char buf[1024*1024];
    while(!feof(stdin)) {
        auto l = fread(buf, 1, sizeof(buf), stdin);
        fwrite(buf, 1, l, stdout);
    }
    fprintf(stdout, "stop:\n");
    return 0;
}