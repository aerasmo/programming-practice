#include <cmath>
using namespace std;

bool PythagoreanTriple(const int a, const int b, const int c)
{
  return (pow(c, 2) == (pow(a, 2) + pow(b, 2)));
}