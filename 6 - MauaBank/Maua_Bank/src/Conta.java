public class Conta{
    //Definindo atributos
    private int numero;
    private double saldo;
    private Cliente cliente;

    //Construtor
    public Conta(int numero, Cliente cliente){
        this.numero = numero;
        this.cliente = cliente;
        saldo = 0;
    }

    //Definindo métodos
    public String visualizarSaldo(){
        return String.format("Saldo atual na conta %d: R$%.2f", numero, saldo);
    }

    public boolean depositar(double valor) {
        if(valor <= 0) return false;
        saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if(valor>saldo || valor<=0) return false;
        saldo -= valor;
        return true;
    }

    public boolean transferirDinheiro(double valor, Conta contaDestino){
        if(!sacar(valor)) return false;
        if(contaDestino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Número: "+numero
        +"\nCliente: "+cliente.getNome()
        +"\nSaldo: "+visualizarSaldo();
    }
}