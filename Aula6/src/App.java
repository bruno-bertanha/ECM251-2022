public class App {
    public static void main(String[] args) throws Exception {
        
        Cliente c1 = new Cliente("Bruno", 
            "123456", 
            "brunod.bertanha@gmail.com", 
            new Conta(23)
        );

        System.out.println("Nome do cliente: "+c1.getNome());
        System.out.println("Email do cliente: "+c1.getEmail());
        System.out.println("CPF do cliente: "+c1.getCpf());
        c1.getConta().visualizarSaldo();

        }
}
