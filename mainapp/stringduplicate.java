import java.util.Scanner;
public class stringduplicate{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print(" Input ? ");
        String a=sc.nextLine();
        char b= sc.next().charAt(0);
        char[] c= a.toCharArray();
          int count=0;
        for (int i=0;i<=c.length;i++){
            if(c[i]== b){
                count=count+1;
        System.out.println(count);  
                }
            }
            
            }
}