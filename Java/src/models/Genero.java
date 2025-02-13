public class Genero implements Objeto{
    private int id;
    private String descricao;

    public Genero(int id, String d){
        setId(id);
        setDescricao(d);
    }

    public void setId(int id){
        this.id = id;
    }

    public void setDescricao(String d){
        if (d != "") this.descricao = d;
        else throw new IllegalArgumentException("Descrição vazia");
    }

    public int getId(){
        return this.id;
    }

    public String getDescricao(){
        return this.descricao;
    }

    public String toString(){
        return String.format("Genero \n ID = %s \n Descrição = %s\n", this.id, this.descricao);
    }
}