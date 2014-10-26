#include "reverse_complement.h"

#include <stdio.h>

#define Z16       "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"
#define RVMAJ32   "\0TVGH\0\0CD\0\0M\0KN\0\0\0YSAABW\0R\0\0\0\0\0\0"
#define RVMIN32   "\0tvgh\0\0cd\0\0m\0kn\0\0\0ysaabw\0r\0\0\0\0\0\0"
#define RVC       Z16 Z16 Z16 Z16 RVMAJ32 RVMIN32 Z16 Z16 Z16 Z16 Z16 Z16 Z16 Z16

char xtbl[256] = RVC;

void reverse_complement(char* str, size_t str_len)
{
  if(str_len == 0) return;
  char* i = str;
  char* j = i + str_len - 1;
  
  char c;
  for( ; i <= j ; i++, j--) {
    c = xtbl[(unsigned int)*i] == '\0' ? *i : xtbl[(unsigned int)*i];
    *i = xtbl[(unsigned int)*j] == '\0' ? *j : xtbl[(unsigned int)*j];
    *j = c;
  }
}

void reverse(char* str, size_t str_len)
{
  if(str_len == 0) return;

  char* i = str;
  char* j = i + str_len;
  
  char c;
  for(j-- ; i < j ; i++, j--) {
    c = *i;
    *i = *j;
    *j = c;
  }
}
