public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("" + validadorCPF.validar("11111111111"));  
        System.out.println("" + validadorCPF.validar("11111111112"));  
        System.out.println("" + validadorCPF.validar("52998224725"));
        System.out.println("" + validadorCPF.validar("52998224735"));
        System.out.println("" + validadorCPF.validar("52998224726"));
    }
}
