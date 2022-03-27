public class Profile {
    //Attributes
    private char profileType;
    private String name;
    private String pwd;
    private String email;
    private String bio;
    private String local;

    //Builder
    public Profile(char profileType, String name, String pwd, String email, String bio, String local){
        this.profileType = profileType;
        this.setName(name);
        this.setPwd(pwd);
        this.setEmail(email);
        this.setBio(bio);
        this.setLocal(local);
    }

    //Getters
    public String getLocal() {
        return local;
    }

    
    public String getBio() {
        return bio;
    }
    
    
    public String getEmail() {
        return email;
    }
    
    
    public String getPwd() {
        return pwd;
    }
    
    
    public String getName() {
        return name;
    }

    //Setters
    public void setLocal(String local) {
        this.local = local;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public void setPwd(String pwd) {
        this.pwd = pwd;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}
