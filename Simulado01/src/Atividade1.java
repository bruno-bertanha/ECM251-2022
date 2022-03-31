//Bruno Bertanha 20.01521-6

public class Atividade1 {
    
    public void run(){
        Transacoes transacoes = new Transacoes();

        Usuarios u1 = new Usuarios("BrunoSuiça", "senha2", "email2@email.com");
        Usuarios u2 = new Usuarios("Bruno", "senha", "email@email.com");
        Usuarios u3 = new Usuarios("BrunoMaldivas", "senha3", "email3@email.com");

        Conta c1 = new Conta(20_000_000, u1);
        Conta c2 = new Conta(40_000, u2);
        Conta c3 = new Conta(30_000_000, u3);
        c1.visualizarConta();
        System.out.println("");
        c2.visualizarConta();
        System.out.println("");
        c3.visualizarConta();
        System.out.println("");

        String qrCode = transacoes.gerarRequi(c1, 20_000);
        System.out.println(qrCode);
        System.out.println("");

        transacoes.pagarRequi(c2, c1, qrCode);
        transacoes.pagarRequi(c3, c1, qrCode);
        transacoes.pagarRequi(c2, c1, qrCode);

        qrCode = transacoes.gerarRequi(c2, 40_000);
        System.out.println(qrCode);
        System.out.println("");

        transacoes.pagarRequi(c3, c2, qrCode);
        c1.visualizarConta();
        System.out.println("");
        c2.visualizarConta();
        System.out.println("");
        c3.visualizarConta();
        System.out.println("");

    }
}
