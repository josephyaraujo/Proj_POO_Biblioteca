import java.util.Scanner;

public class UITeste{
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args){
        int op = 0;
        while (op != 3){
            System.out.println("SISTEMA DE BIBLIOTECA\n 1 - Entrar no sistema\n 2 - Cadastrar-se no sistema como cliente\n 3 - Finalizar");
            op = input.nextInt();
            input.nextLine();
            if (op == 1) {
                entrarSistema();
            } else if (op == 2) {
                cadastrarSistema();
            } else if (op == 3) {
                System.out.println("Sistema finalizado");
            }
            
        }
    }

    public static void entrarSistema(){
        System.out.print("Email: ");
        String email = input.nextLine();

        System.out.print("Senha: ");
        String senha = input.nextLine();

        if (View.usuarioAutenticar(email, senha) == null) {
            System.out.println("Usuario não tem acesso a essa página.");
        };
    }

    public static void cadastrarSistema(){
        System.out.print("Nome completo: ");
        String nome = input.nextLine();

        System.out.print("Email (ex: email@gmail.com): ");
        String email = input.nextLine();

        System.out.print("Fone (ex: (xx) xxxxx-xxxx): ");
        String telefone = input.nextLine();

        System.out.println("Senha: ");
        String senha = input.nextLine();

        View.clienteInserir(nome, email, telefone, senha, EnumUsuarios.CLIENTE);
    }
}