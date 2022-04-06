import java.time.LocalDate;
import java.time.Period;

public class Sistema {
    
    public void run(){
        Cliente cliente = new Cliente("Endevour", "456789", "putzsousegundo@gamil.com");
        Conta conta = new Conta(9865, cliente);
        System.out.println(conta);

        Titulo titulo = new Titulo(686.97, LocalDate.of(2022, 03, 30), 5);

    }
    
    boolean pagarTitulo(Titulo titulo, Conta conta){
        LocalDate prazo = titulo.getData();
        LocalDate hoje = LocalDate.now();
        double valor;
        if(prazo.isBefore(hoje)){
            valor = titulo.getValor();
        } else {
            int diasAtraso = Period.between(hoje, prazo).getDays(); 
            valor = titulo.getValor() + titulo.getValor()*titulo.getMultaDiaria()/100*diasAtraso;
        }


        return true;
    }
}
