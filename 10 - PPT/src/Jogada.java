public class Jogada {
    private enumJogadas venco1, venco2;

    public Jogada(enumJogadas venco1, enumJogadas venco2) {
        this.venco1 = venco1;
        this.venco2 = venco2;
    }

    public boolean verificarVenceu(Jogada jogada){
        if(jogada.getTipo().equals(venco1) || jogada.getTipo().equals(venco2)){
            return true;
        }
        return false;
    }

    public enumJogadas getTipo() {
        return enumJogadas.PAPEL;
    }
}
