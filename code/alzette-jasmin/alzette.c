#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>

typedef struct {uint32_t val1; uint32_t val2;} tuple;

extern tuple alzette(uint32_t, uint32_t);

int main()
{
  uint32_t c = 0xb7e15162;
  uint32_t x = 0x9e3779b9;
  uint32_t y = 0x6e3449b3;

  tuple result = alzette(x,y);

  printf("x: %" PRIu32 "  ", result.val1);
  printf("y: %" PRIu32 "  ", result.val2);
  
  return 0;
}
