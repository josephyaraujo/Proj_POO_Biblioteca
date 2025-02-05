import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Generos extends Modelo{
    public static void abrir(){
        objetos.clear();  // Limpa a lista antes de carregar
        try {
            FileReader reader = new FileReader("generos.json");
            Type listType = new TypeToken<List<Cliente>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // Se o arquivo não for encontrado, inicia uma lista vazia
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void salvar(){
        try {
            FileWriter writer = new FileWriter("generos.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer);  // Converte a lista para JSON e escreve no arquivo
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}