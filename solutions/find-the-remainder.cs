using System;

public class Kata
{
  public static int Remainder(int a, int b)
  {
    try {
      return a > b ? a % b : b % a;
    } catch (DivideByZeroException e ) {
      throw(e);
    }
  }
}
