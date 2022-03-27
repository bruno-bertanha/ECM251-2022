public class Account {
    //Attributes
    private int code;
    private double balance;
    private Profile profile;

    //Builder
    public Account(int code, Profile profile){
        this.code = code;
        this.profile = profile;
        balance = 0;
    }

    //Defininf methods
    public String seeBalance(){
        return String.format("Your current balance is: $%.2f", balance);
    }

}

