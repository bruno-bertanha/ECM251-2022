public class bigBrothers extends Membros {

    //Construtor
    public bigBrothers(String userName, String email) {
        super(userName, email, enumFuncoes.BIG_BROTHER);
    }

    //Método postarMensagem
    @Override
    public void postarMensagem() {
        if(Atividade02.getHorario() == enumHorariosAtividades.REGULAR) {
            System.out.println("Sempre ajudando as pessoas membros ou não S2!" );
        }
        else{
            System.out.println("..." );
        }
    }
}