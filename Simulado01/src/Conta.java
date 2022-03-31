//Bruno Bertanha 20.01521-6

public class Conta{
    private int idConta;
    private double saldo;
    private Usuarios usuario;
    private static int contador = 0;
    
    public Conta(double saldo, Usuarios usuario){
        this.idConta = contador;
        this.saldo = saldo;
        this.usuario = usuario;
        contador += 1;
    }

    public void visualizarConta(){
        System.out.println("Dados da Conta: ");
        System.out.println("ID:  " + idConta);
        System.out.println("Saldo:  " + saldo);
        System.out.println("Usuario:  " + usuario.getNome());
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

    public int getIdConta() {
        return idConta;
    }

    public void setIdConta(int idConta) {
        this.idConta = idConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public Usuarios getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuarios usuario) {
        this.usuario = usuario;
    }


}