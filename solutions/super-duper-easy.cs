using System;

public class Kata
{
  public static string Problem(String a)
  {
    Console.WriteLine(a);
    try {
      double doubleVal = Convert.ToDouble(a);
      return (doubleVal * 50 + 6).ToString();
    } catch (FormatException e){
      return "Error";
    }
  }
}