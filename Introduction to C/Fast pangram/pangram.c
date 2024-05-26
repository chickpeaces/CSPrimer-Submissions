#include <ctype.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

bool ispangram(char *s);

int main() {
  size_t len;
  ssize_t read;
  char *line = NULL;
  while ((read = getline(&line, &len, stdin)) != EOF) {
    if (ispangram(line))
      printf("%s", line);
  }

  if (ferror(stdin))
    fprintf(stderr, "Error reading from stdin");

  free(line);
  fprintf(stderr, "ok\n");
}

bool ispangram(char *s) {
  int32_t t= 0, alpha_bitset= 0;

  while( s[t] != '\0'){
    if( isalpha( s[t]))
      alpha_bitset|= (0x01 << (tolower(s[t])-'a'));
    t++;
  }

  return (alpha_bitset == 0x03FFFFFF);
}