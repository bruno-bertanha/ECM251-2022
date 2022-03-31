//Bruno Bertanha 20.01521-6


public class Transacoes {

    public String gerarRequi(Conta pedinte, double valor){
        return pedinte.getIdConta()+";"+pedinte.getUsuario().getNome().toUpperCase()+";"+valor;
    }

    public boolean pagarRequi(Conta pagador, Conta recebedor, String qrCode){
        String [] dados = qrCode.split(";");
        int idContaRecebedor = Integer.parseInt(dados[0]);
        String nomeRecebedor = dados[1];
        double valor = Double.parseDouble(dados[2]);

        if(idContaRecebedor == recebedor.getIdConta() && nomeRecebedor.equals(recebedor.getUsuario().getNome().toUpperCase()) && pagador.sacar(valor)){
            recebedor.depositar(valor);
            return true;
        }
        return false;
    }
    
}
