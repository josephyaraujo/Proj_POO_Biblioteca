public class Genero implements Objeto{
    private int id;
    private String descricao;

    public Genero(int id, String descricao){
        setId(id);
        setDescricao(descricao);
    }

    public void setId(int id){
        this.id = id;
    }

    public void setDescricao(String descricao){
        if (descricao != "") this.descricao = descricao;
        else throw new IllegalArgumentException("Descrição vazia");
    }

    public int getId(){
        return this.id;
    }

    public String getDescricao(){
        return this.descricao;
    }

    public String toString(){
        return String.format("ID = %s \n Descrição = %s\n", this.id, this.descricao);
    }
}