import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Emprestimos extends Modelo<Emprestimo>{
    @Override
    public void abrir(){
        objetos.clear();  // Limpa a lista antes de carregar
        try {
            FileReader reader = new FileReader("../Arquivos/emprestimos.json");
            Type listType = new TypeToken<List<Emprestimo>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // Se o arquivo não for encontrado, inicia uma lista vazia
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void salvar(){
        try {
            FileWriter writer = new FileWriter("../Arquivos/emprestimos.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer);  // Converte a lista para JSON e escreve no arquivo
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}