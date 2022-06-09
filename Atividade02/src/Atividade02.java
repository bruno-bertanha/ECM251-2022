import java.util.LinkedList;

public class Atividade02{
    //criação da variável que armazenará o horário de atividade
    private static enumHorariosAtividades horario = enumHorariosAtividades.REGULAR;

    public void run(){
        //criação da lista de membros
        LinkedList <Membros> membros = new LinkedList<Membros>();

        //criação dos membros
        membros.add(new scriptGuys("Scripteiro", "scripteiro@hacker.org"));
        membros.add(new mobileMembers("Tiktoker", "tiktoker@hacker.org"));
        membros.add(new bigBrothers("Irmaourso", "irmaourso@hacker.org"));
        membros.add(new heavyLifters("Wolfgang", "wolfgang@hacker.com"));
        
        //criação do loop que percorre a lista de membros
        for(Membros membro : membros){
            System.out.println(membro.getUserName());
            membro.postarMensagem();
            System.out.println();
        }

        mudarTurno();
        System.out.println("MENSAGENS APÓS MUDANÇA DE TURNO\n");
        for(Membros membro : membros){
            System.out.println(membro.getUserName());
            membro.postarMensagem();
            System.out.println();
        }
        
        mudarTurno();
        System.out.println("MENSAGENS APÓS MUDANÇA DE TURNO E EXCLUSÃO\n");
        membros.remove(3);
        membros.remove(0);
        for(Membros membro : membros){
            System.out.println(membro.getUserName());
            membro.postarMensagem();
            System.out.println();
        }
    }

    //getter do horário
    public static enumHorariosAtividades getHorario() {
        return horario;
    }

    //método que altera o horário
    public void mudarTurno(){
        if(horario == enumHorariosAtividades.REGULAR){
            horario = enumHorariosAtividades.EXTRA;
        }
        else{
            horario = enumHorariosAtividades.REGULAR;
        }
    }

    
}