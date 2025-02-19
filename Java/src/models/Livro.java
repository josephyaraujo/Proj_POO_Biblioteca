public class Livro implements Objeto{
    private int id;
    private String titulo;
    private String autor;
    private int ano;
    private int idGenero;

    public Livro(int id, String titulo, String autor, int ano, int idGenero){
        setId(id);
        setTitulo(titulo);
        setAutor(autor);
        setAno(ano);
        setIdGenero(idGenero);
    }

    public void setId(int id){
        this.id = id;
    }

    public void setTitulo(String titulo){
        if (titulo != "") this.titulo = titulo;
        else throw new IllegalArgumentException("Título do livro não pode ser vazio");
    }

    public void setAutor(String autor){
        if (autor != "") this.autor = autor;
        else throw new IllegalArgumentException("Autor não pode ser vazio");
    }

    public void setAno(int ano){
        this.ano = ano;
    }

    public void setIdGenero(int idGenero){
        this.idGenero = idGenero;
    }

    public int getId(){
        return this.id;
    }

    public String getTitulo(){
        return this.titulo;
    }

    public String getAutor(){
        return this.autor;
    }

    public int getAno(){
        return this.ano;
    }

    public int getIdGenero(){
        return this.idGenero;
    }

    public String toString(){
        return String.format("ID = %s \n Título = %s \n Autor = %s \n Ano = %s \n Id genero = %s", this.id, this.titulo, this.autor, this.ano, this.idGenero);
    }

}