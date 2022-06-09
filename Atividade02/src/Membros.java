public abstract class Membros implements PostarMensagem{
    //Atributos
    private String userName;
    private String email;
    private enumFuncoes funcao;

    //Construtor
    public Membros(String userName, String email, enumFuncoes funcao) {
        this.userName = userName;
        this.email = email;
        this.funcao = funcao;
    }
    
    //toString
    @Override
    public String toString() {
        return "Membros [email=" + email + ", funcao=" + funcao + ", userName=" + userName + "]";
    }

    //Getters
    public String getUserName() {
        return userName;
    }
}
