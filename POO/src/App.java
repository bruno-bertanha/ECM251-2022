public class App {
    public static void main(String[] args) throws Exception {
        //Cria e instancia um objeto do tipo Caneta
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("Azul", "BIC", 1.0);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Vermelha", "Stabillo", 0.4);

        c1.escrever("josjodjjaojsodjojasjdjojaosjodjajsjdiojoaihusihaihuuihdiusauhhdhashdhahshhduasihuiidhuausiiuduhudiasuihudiuiauhsuhdusaiuhdhuuaiusdauihduihuashduias");

        System.out.println("Minha caneta C1: " + c1.pegarDados());

        System.out.println("Minha caneta C2: " + c2.pegarDados());
    }
}
