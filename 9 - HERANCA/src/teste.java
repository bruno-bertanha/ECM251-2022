import java.util.Scanner;
public class teste {
    public static void main(String[] args) {
        Scanner in = new Scanner (System.in);
        int n = in.nextInt();
        System.out.println(Func(n));
        in.close();
    }

    public static int Func(int n) {
    int m = 0;
    for (int i=1; i <= n; i++)
        for (int j = i; j <= n; j++ ) {
            m = m + 1; // Linha 1
        }
    return m;
    }
}
