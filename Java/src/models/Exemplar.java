public class Exemplar implements Objeto{
    private int id;
    private int edicao;
    private String editora;
    private Boolean situacao;
    private int idLivro;
    private int idGenero;

    public Exemplar(int id, int edicao, String editora, Boolean situacao, int idLivro, int idGenero){
        setId(id);
        setEdicao(edicao);
        setEditora(editora);
        setSituacao(situacao);
        setIdLivro(idLivro);
        setIdGenero(idGenero);
    }

    public void setId(int id){
        this.id = id;
    }

    public void setEdicao(int edicao){
        if (edicao > 0) this.edicao = edicao;
        else throw new IllegalArgumentException("Edição inválida");
    }

    public void setEditora(String editora){
        if (editora != "") this.editora = editora;
        else throw new IllegalArgumentException("Editora inválida");
    }

    public void setSituacao(Boolean situacao){
        this.situacao = situacao;
    }

    public void setIdLivro(int idLivro){
        this.idLivro = idLivro;
    }

    public void setIdGenero(int idGenero){
        this.idGenero = idGenero;
    }

    public int getId(){
        return this.id;
    }

    public int getEdicao(){
        return this.edicao;
    }

    public String getEditora(){
        return this.editora;
    }

    public Boolean getSituacao(){
        return this.situacao;
    }

    public int getIdLivro(){
        return this.idLivro;
    }

    public int getIdGenero(){
        return this.idGenero;
    }

    public String toString(){
        return String.format("Exemplar \n ID = %s \n Edição = %s \n Editora = %s \n Situacao = %s \n Id Livro = %d \n Id genero = %s", this.id, this.edicao, this.editora, this.situacao, this.idLivro, this.idGenero);
    }
}