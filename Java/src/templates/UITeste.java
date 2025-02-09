import java.util.Scanner;
import java.util.List;

public class UITeste{
    static Scanner input = new Scanner(System.in);
    
    public static void main(String[] args){
        

        Livro l = new Livro(0, "amor", "joao", 2025, 1);
        Livros livro = new Livros();
        livro.inserir(l);

        

    }
}