public class Caneta {
    String modelo;
    String cor;
    int carga;
    double ponta;
    final int CARGA_MAXIMA = 100;

    void iniciarCaneta(String cor, String modelo,  double ponta){
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
        this.carga = CARGA_MAXIMA;
    }

    void escrever(String texto){
        for (int i = 0; i < texto.length(); i++) {
            if(carga > 0){
                System.out.print(texto.charAt(i));
                carga--;
            } else {
                System.out.println("Caneta sem carga!");
                break;
            }
        }
        System.out.println();
    }

    String pegarDados(){
        return "Modelo: " + this.modelo + 
        " - Cor: " + this.cor +
        " - Ponta: " + this.ponta +
        " - Carga: " + this.carga;
    }
}
