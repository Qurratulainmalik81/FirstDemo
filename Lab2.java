import java.util.*;
public class Lab2 {
    public static void main(String args[]) 
    {
        int[] number = new int[5];
        int max = 0;
        Scanner in = new Scanner(System.in);
        System.out.println("Enter five numbers");
        for(int i =0;i<5;i++)
        {
        number[i] = in.nextInt();
        if(number[i]>max)
        max = number[i];
        }
       System.out.println("largest number is " + max);
   }
}
