public class scriptGuys extends Membros {
    //Construtor
    public scriptGuys(String userName, String email) {
        super(userName, email, enumFuncoes.SCRIPT_GUY);
    }
    
    //Método postarMensagem
    @Override
    public void postarMensagem() {
        if(Atividade02.getHorario() == enumHorariosAtividades.REGULAR) {
            System.out.println("Prazer em ajudar novos amigos de código!" );
        }
        else{
            System.out.println("QU3Ro_S3us_r3curs0s.py" );
        }
    }
    
}
