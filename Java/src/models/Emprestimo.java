import java.time.LocalDate;

public class Emprestimo implements Objeto{
    private int id;
    private String data;
    private String dataDevolucao;
    private int prazoExtendido;
    private int idExemplar;
    private int idUsuario;

    public Emprestimo(int id, String data, String dataDevolucao, int prazoExtendido, int idExemplar, int idUsuario){
        setId(id);
        setData(data);
        setDataDevolucao(dataDevolucao);
        setPrazoExtendido(prazoExtendido);
        setIdExemplar(idExemplar);
        setIdUsuario(idUsuario);
    }

    public void setId(int id){
        this.id = id;
    }

    public void setData(String data){
        this.data = data;
    }

    public void setDataDevolucao(String dataDevolucao){
        this.dataDevolucao = dataDevolucao;
    }

    public void setPrazoExtendido(int prazoExtendido){
        this.prazoExtendido = prazoExtendido;
    }

    public void setIdExemplar(int idExemplar){
        this.idExemplar = idExemplar;
    }

    public void setIdUsuario(int idUsuario){
        this.idUsuario = idUsuario;
    }

    public int getId(){
        return this.id;
    }

    public String getData(){
        return this.data;
    }

    public String getDataDevolucao(){
        return this.dataDevolucao;
    }

    public int getPrazoExtendido(){
        return this.prazoExtendido;
    }

    public int getIdExemplar(){
        return this.idExemplar;
    }

    public int getIdUsuario(){
        return this.idUsuario;
    }

    public String toString(){
        return String.format("Emprestimo \n ID = %s \n Data = %s \n Data de devolução = %s \n Prazo extendido = %s \n Id exemplar = %d \n Id usuario = %s", this.id, this.data, this.dataDevolucao, this.prazoExtendido, this.idExemplar, this.idUsuario);
    }
}