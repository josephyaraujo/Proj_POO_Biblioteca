import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class UITeste{
    static Scanner input = new Scanner(System.in);
    
    public static void main(String[] args){

        LocalDate dataEmprestimo = LocalDate.now();
        LocalDate dataDevolucao = LocalDate.of(2025, 02, 11);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        String dataEmp = dataEmprestimo.format(formatter);
        String dataDev = dataDevolucao.format(formatter);

        Emprestimo e = new Emprestimo(0, dataEmp, dataDev, 0, 0, 0);
        Emprestimos emp = new Emprestimos();
        emp.inserir(e);
        System.out.println(emp.listar());

        Exemplar ex = new Exemplar(0, 2, "Dark side", true, 0, 0);
        Exemplares exe = new Exemplares();
        exe.inserir(ex);
        System.out.println(exe.listar());

        Usuario usu = new Usuario(0, "manu", "manu@gmail.com", "(84) 98635-9205", "manu123", EnumUsuarios.ADMIN);
        Usuarios u = new Usuarios();
        u.inserir(usu);
        System.out.println(u.listar());

        Livro l = new Livro(0, "amor", "joao", 2025, 1);
        Livros livro = new Livros();
        livro.inserir(l);
        System.out.println(livro.listar());

        Genero g = new Genero(0, "comedia");
        Generos generos = new Generos();
        generos.inserir(g);
        System.out.println(generos.listar());

    }
}