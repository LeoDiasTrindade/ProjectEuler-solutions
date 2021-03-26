#include <stdio.h>

#define LIMIT 1000

int main() {
  int sum = 0;

  for (int i = 1; i < LIMIT; i ++)
    sum += (i % 3 == 0 || i % 5 == 0 ? i : 0);

  printf("Sum of multiples of 3 or 5 bellow %d = %d\n", LIMIT, sum);
  return 0;
}
