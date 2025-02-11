import java.util.ArrayList;
import java.util.List;

abstract class Modelo<T extends Objeto>{
    protected List<T> objetos = new ArrayList<>();

    public void inserir(T obj){
        abrir();

        int id = 0;
        for (T objeto:objetos) {
            if (objeto.getId() > id) id = objeto.getId();
        }
        obj.setId(id + 1);

        objetos.add(obj);
        salvar();
    }

    public List<T> listar(){
        abrir();
        
        return objetos;
    }

    public T listarId (int id){
        abrir();
        for (T obj:objetos) {
            if (obj.getId() == id) return obj;
        }

        return null;
    }
    
    public void atualizar(T obj){
        T objeto = listarId(obj.getId());
        if (objeto != null) {
            objetos.remove(objeto);
            objetos.add(obj);
            salvar();
        }
    }

    public void excluir(T obj) {
        T objeto = listarId(obj.getId());
        if (objeto != null){
            objetos.remove(objeto);
            salvar();
        }
    }

    public abstract void salvar();

    public abstract void abrir();
}