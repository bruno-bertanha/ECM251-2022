//Bruno Davidovitch Bertanha 20.1521-6

public class Atividade1 {
    
    public void run(){  
        //Criaçãoe exibição do usuário
        Usuario u1 = new Usuario("Joao");
        System.out.println(u1.toString());

        //Criação e exibição dos veículos
        Carro c1 = new Carro("carro", 1000);
        System.out.println(c1.toString());
        Moto m1 = new Moto("moto", 500);
        System.out.println(m1.toString());
        Bicicleta b1 = new Bicicleta("bicicleta", 100);
        System.out.println(b1.toString());
        Patinete p1 = new Patinete("patinete", 50);
        System.out.println(p1.toString());

        //Realização das trocas de bem
        u1.trocarBem(c1);
        u1.trocarBem(m1);
        u1.trocarBem(b1);
        u1.trocarBem(p1);
        
    }
}