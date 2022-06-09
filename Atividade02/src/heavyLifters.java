public class heavyLifters extends Membros {

    //Construtor
    public heavyLifters(String userName, String email) {
        super(userName, email, enumFuncoes.HEAVY_LIFTER);
    }
    
    //Método postarMensagem
    @Override
    public void postarMensagem() {
        if(Atividade02.getHorario() == enumHorariosAtividades.REGULAR) {
            System.out.println("Podem contar conosco!");
        }
        else{
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }
    }
}
