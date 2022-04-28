//Bruno Davidovitch Bertanha 20.1521-6

public class Usuario {
    //Atributos
    private String nome;
    private Veiculo veiculo;

    //Construtor
    public Usuario(String nome) {
        this.nome = nome;
    }

    //Função de troca de bem
    public void trocarBem(Veiculo novoVeiculo) {
        this.veiculo = novoVeiculo;
        testar();
    }

    //Função de teste
    public void testar(){
        System.out.println("ID do bem compartilhado em uso: " + veiculo.getID());
        System.out.println("Custo por hora do bem compartilhado em uso: " + veiculo.getCusto());
    }

    //Getters
    public String getNome() {
        return nome;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    @Override
    public String toString() {
        return "Usuario [nome=" + nome + ", veiculo=" + veiculo + "]";
    }

}
