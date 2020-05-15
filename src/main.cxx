#include <iostream>

#include "header.hxx"

int main(int, char**) {
  Header head;
  Header header('h', 'z');
  header.hello("main");

  printf("SHORT MAX\t\t= %d\n", MAX(33, 42));
  printf("CHAR MAX\t\t= %c\n\n", MAX('h', 'z'));
  printf("SHORT MAX\t\t= %d\n", maxShort(33, 42));
  printf("CHAR MAX\t\t= %c\n\n", head.maxChar());
  printf("CHAR MAX\t\t= %c\n\n", header.maxChar());

  std::cout << "SECONDS_IN_DAY:\t\t" << SECONDS_IN_DAY << std::endl;
  std::cout << "MILISECONDS_IN_DAY:\t" << MILISECONDS_IN_DAY << std::endl;

  return 0;
}
