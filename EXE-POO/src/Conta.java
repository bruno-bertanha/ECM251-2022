public class Conta{
    //Definindo atributos
    int numero;
    String titular;
    double saldo;
    String cpf;

    //Definindo métodos
    void visualizarSaldo(){
        System.out.println("Saldo atual na conta "+numero+": "+saldo);
    }

    boolean depositar(double valor) {
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
    boolean sacar(double valor){
        // if(saldo >= valor){
        //     saldo -= valor;
        // } else{
        //     System.out.println("Valor insuficiente para sacar!);
        // }
        if(valor>saldo || valor<=0) return false;
        saldo -= valor;
        return true;
    }
    boolean transferirDinheiro(double valor, Conta contaDestino){
        if(!sacar(valor)) return false;
        if(contaDestino.depositar(valor)) return false;
        return true;
    }
}