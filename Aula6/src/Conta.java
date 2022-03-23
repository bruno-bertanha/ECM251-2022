public class Conta{
    //Definindo atributos
    private int numero;
    private double saldo;

    public Conta(int numero){
        this.numero = numero;
        saldo = 0;
    }

    //Definindo métodos
    public void visualizarSaldo(){
        System.out.println("Saldo atual na conta "+numero+": R$"+saldo);
    }

    public boolean depositar(double valor) {
        // if (valor > 0) {
        //     saldo += valor;
        //     return true;
        // } else {
        //     return false;
        // }
        if(valor <= 0) return false;
        saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        // if(saldo >= valor){
        //     saldo -= valor;
        // } else{
        //     System.out.println("Valor insuficiente para sacar!);
        // }
        if(valor>saldo || valor<=0) return false;
        saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta contaDestino){
        if(!sacar(valor)) return false;
        if(contaDestino.depositar(valor)) return false;
        return true;
    }
}