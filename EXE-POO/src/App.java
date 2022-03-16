public class App {
    public static void main(String[] args) throws Exception {
        //Declara e instancia um objeto do tipo Conta
        Conta minhaConta = new Conta();
        Conta outraConta = new Conta();
        
        minhaConta.numero = 1234;
        outraConta.numero = 5678;
        minhaConta.saldo = 5000.0;
        outraConta.saldo = 2000.0;

        minhaConta.visualizarSaldo();
        outraConta.visualizarSaldo();
        
        // if(!minhaConta.depositar(500.0)){
        //     System.out.println("Operacao falhou!");
        // }
        
        // if(!minhaConta.sacar(200.0)){
        //     System.out.println("Operacao falhou!");
        // }
        // minhaConta.visualizarSaldo();
        
        System.out.println("");
        minhaConta.transferirDinheiro(6000.0, outraConta);
        minhaConta.visualizarSaldo();
        outraConta.visualizarSaldo();
        
    }
}
