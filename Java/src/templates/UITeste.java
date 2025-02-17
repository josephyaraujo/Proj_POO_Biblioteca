import java.util.Scanner;

public class UITeste{
    static Scanner input = new Scanner(System.in);
    
    public static void main(String[] args){
        int op = 0;
        while (op != 3){
            System.out.println("------------------------");
            System.out.println("| SISTEMA DE BIBLIOTECA |");
            System.out.println("------------------------");
            System.out.println(
                                "1 - Entrar no sistema\n" + //
                                "2 - Cadastrar-se no sistema como cliente\n" + //
                                "3 - Finalizar o sistema");
            System.out.print("Digite sua opção: ");
            op = input.nextInt();
            input.nextLine();
            if (op == 1) {
                entrarSistema();
            } else if (op == 2) {
                cadastrarSistema();
            } else if (op == 3) {
                System.out.println("Sistema finalizado.");
            }
            
        }
    }

    public static void entrarSistema(){
        System.out.print("Email: ");
        String email = input.nextLine();

        System.out.print("Senha: ");
        String senha = input.nextLine();

        Usuario usuario = View.usuarioAutenticar(email, senha);

        if (usuario == null) {
            System.out.println("Usuario não tem acesso a essa página.\n");
        } else {
            menuCliente(usuario);
        }
    }

    public static void cadastrarSistema(){
        try {
            System.out.print("Nome completo: ");
            String nome = input.nextLine();

            System.out.print("Email (ex: email@gmail.com): ");
            String email = input.nextLine();

            System.out.print("Fone (ex: (xx) xxxxx-xxxx): ");
            String telefone = input.nextLine();

            System.out.print("Senha: ");
            String senha = input.nextLine();

            View.clienteInserir(nome, email, telefone, senha, EnumUsuarios.CLIENTE);
            System.out.println("Cadastro realizado com sucesso! Entre na sua conta|");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void menuCliente(Usuario usuario) {
        int opMenu = 0;
        while (opMenu != 3){
            System.out.println("-----------------------");
            System.out.println("|SISTEMA DE BIBLIOTECA|");
            System.out.println("-----------------------");
            System.out.println("Seja bem-vindo(a) " + usuario.getNome());
            System.out.println("O que deseja?");
            System.out.println("1 - Ver exemplares disponíveis\n2 - Consultar empréstimos\n3 - Sair");
            System.out.print("Digite sua opção: ");

            opMenu = input.nextInt();
            input.nextLine();

            if (opMenu == 1) {
                System.out.println("------EXEMPLARES------");
                View.verExemplares();
            } else if (opMenu == 2) {
                System.out.println("------EMPRÉSTIMOS------");
                Emprestimo e = View.consultarEmprestimo(usuario.getId());
                menuEmprestimo();
                if (e != null){
                    System.out.println(e);
                } else {
                    System.out.println("Não há empréstimos cadastrados.\n");
                }
            } else if (opMenu == 3) {
                return;
            }
        } 
    }

    public static void menuEmprestimo(){
        int opEmprestimo = 0;
        while (opEmprestimo != 3){
            System.out.println("O que deseja?");
            System.out.println("1 - Solicitar aumento de prazo\n2 - Realizar devolução\n 3 - Voltar para tela inicial");
            if (opEmprestimo == 1) {

            } else if (opEmprestimo == 2) {

            } else if (opEmprestimo == 3){
                return;
            }
        }
    }
}