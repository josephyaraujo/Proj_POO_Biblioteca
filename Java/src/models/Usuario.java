public class Usuario implements Objeto{
    private int id;
    private String nome;
    private String email;
    private String fone;
    private String senha;
    private EnumUsuarios tipoUsuario;

    public Usuario(int id, String nome, String email, String fone, String senha, EnumUsuarios tipoUsuario){
        setId(id);
        setNome(nome);
        setEmail(email);
        setFone(fone);
        setSenha(senha);
        setTipoUsuario(tipoUsuario);
    }

    public void setId(int id){
        this.id = id;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public void setFone(String fone){
        this.fone = fone;
    }

    public void setSenha(String senha){
        this.senha = senha;
    }

    public void setTipoUsuario(EnumUsuarios tipoUsuario){
        this.tipoUsuario = tipoUsuario;
    }

    public int getId(){
        return this.id;
    }

    public String getNome(){
        return this.nome;
    }

    public String getEmail(){
        return this.email;
    }

    public String getFone(){
        return this.fone;
    }

    public String getSenha(){
        return this.senha;
    }

    public EnumUsuarios getTipoUsuario(){
        return this.tipoUsuario;
    }

    public String toString(){
        return String.format("Usuário \n ID = %s \n Nome = %s \n Email = %s \n Fone = %s \n Senha = %s \n Tipo usuário = %s", this.id, this.nome, this.email, this.fone, this.senha, this.tipoUsuario);
    }
}