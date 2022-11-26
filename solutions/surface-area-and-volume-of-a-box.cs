using System;

public class Kata
{
    public static int[] Get_size(int w,int h,int d)
    {
        
        return new int[] { 2*w*h + 2*w*d + 2*h*d , w*h*d };
    }
}