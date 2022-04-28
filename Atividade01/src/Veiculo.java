//Bruno Davidovitch Bertanha 20.1521-6

import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {
    //Atributos
    private int ID;
    private String tipo;
    private float custo;

    //Construtor
    public Veiculo(String tipo, float custo) {
        this.ID = ThreadLocalRandom.current().nextInt(10000,100000);
        this.tipo = tipo;
        this.custo = custo;
    }

    //Getters
    public int getID() {
        return ID;
    }

    public String getTipo() {
        return tipo;
    }

    public float getCusto() {
        return custo;
    }

    //toString 
    @Override
    public String toString() {
        return "veiculo [ID=" + ID + ", custo=" + custo + ", tipo=" + tipo + "]";
    }

    
}
