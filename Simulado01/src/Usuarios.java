//Bruno Bertanha 20.01521-6

public class Usuarios {
    private String nome;
    private String senha;
    private String email;

    public Usuarios(String nome, String senha, String email){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
    }

    public void visualizarUsuario(){
        System.out.println("Dados do Usuario: ");
        System.out.println("Nome:  " + nome);
        System.out.println("Senha:  " + senha);
        System.out.println("Email:  " + email);
    }

    //Getters
    public String getNome(){
        return nome;
    }
    
    public String getSenha(){
        return senha;
    }

    public String getEmail(){
        return email;
    }

    //Setters
    public void setNome(String nome){
        this.nome = nome;
    }

    public void setSenha(String senha){
        this.senha = senha;
    }

    public void setEmail(String email){
        this.email = email;
    }
}
