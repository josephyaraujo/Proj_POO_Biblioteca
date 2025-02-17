import java.util.regex.Matcher;
import java.util.regex.Pattern;

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
        if (nome != "") this.nome = nome;
        else throw new IllegalArgumentException("Nome não pode ser vazio");
    }

    public void setEmail(String email){
        if (email == null || email.isEmpty()) {
            throw new IllegalArgumentException("Email inválido");
        }

        //Expressão regular \\ - dispensa o . $ - fim da string ^ - começo da string
        String regex = "^[a-zA-Z0-9._%+-]+@gmail\\.com$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(email);
        
        if (matcher.matches()) {
            this.email = email;
        } else {
            throw new IllegalArgumentException("Email inválido");
        }
    }

    public void setFone(String fone){
        if (fone != "") this.fone = fone;
        else throw new IllegalArgumentException("Numero de telefone não pode ser vazio");
    }

    public void setSenha(String senha){
        if (senha != "") this.senha = senha;
        else throw new IllegalArgumentException("Senha não pode ser vazia.");
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