import java.util.ArrayList;
import java.util.List;

public abstract class Modelo{
    private static List<Modelo> objetos = new ArrayList<>;

    public static void inserir(Modelo obj){
        abrir();

        int id = 0;
        for (Modelo objeto:objetos) {
            if (objeto.getId() > id) id = objeto;getId();
        }
        obj.setId(id + 1);

        objetos.add(obj);
        salvar();
    }

    public static List<Modelo> listar(){
        abrir();

        return objetos;
    }

    public static Modelo listarId (int id){
        abrir();
        
        for (Modelo objeto:objetos) {
            if (objeto.getId() == id) return objeto;
        }

        return null;
    }

    public static void excluir(Modelo obj) {
        Modelo objeto = listarId(obj.getId());
        if (objeto != null){
            objetos.remove(objeto);
            salvar();
        }
    }

    public static abstract void salvar();

    public static abstract void abrir();
}