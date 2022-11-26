using System;

public static class Kata
{
    public static string MultiTable(int number)
    {
      string[] table = new string[10]; 
      for (int i = 1; i <= 10; i++) {
        table[i-1] = $"{i} * {number} = {i*number}";
      }
      return string.Join("\n", table);
    }
}