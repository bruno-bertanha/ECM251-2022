public class mobileMembers extends Membros {

    //Construtor
    public mobileMembers(String userName, String email) {
        super(userName, email, enumFuncoes.MOBILE_MEMBER);
    }
    
    //Método postarMensagem
    @Override
    public void postarMensagem() {
        if(Atividade02.getHorario() == enumHorariosAtividades.REGULAR) {
            System.out.println("Happy Coding!" );
        }
        else{
            System.out.println("Happy_C0ding. Maskers" );
        }
    }
}
    
