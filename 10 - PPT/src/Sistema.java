import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        Jogada jogada1 = sortearJogada();
        Jogada jogada2 = sortearJogada();
        System.out.println("Jogada 1: " + jogada1.getTipo());
        System.out.println("Jogada 2: " + jogada2.getTipo());
        String resultado = avaliaJogadas(jogada1, jogada2);
        System.out.println("Resultado: " + resultado);
    }

    private static Jogada sortearJogada(){
        Jogada jogadas[] = new Jogada[3];
        jogadas[0] = new Tesoura();
        jogadas[1] = new Pedra();
        jogadas[2] = new Papel();
        return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2) {
        if(jogada1.verificarVenceu(jogada2)){
            return "Jogada 1 venceu";
        }
        if(jogada2.verificarVenceu(jogada1)){
            return "Jogada 2 venceu";
        }
        return "Empate";
    }
}
