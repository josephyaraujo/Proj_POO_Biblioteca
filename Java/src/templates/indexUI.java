import java.util.Scanner;
import java.util.List;

public class indexUI{
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
            System.out.println("Cadastro realizado com sucesso! Entre na sua conta.");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void menuCliente(Usuario usuario) {
        int opMenu = 0;
        while (opMenu != 3){
            System.out.println("-----------------------");
            System.out.println("|MENU DO CLIENTE|");
            System.out.println("-----------------------");
            System.out.println("Seja bem-vindo(a) " + usuario.getNome());
            System.out.println("O que deseja?");
            System.out.println("1 - Ver exemplares disponíveis\n2 - Consultar empréstimos\n3 - Sair da conta");
            System.out.print("Digite sua opção: ");

            opMenu = input.nextInt();
            input.nextLine();

            if (opMenu == 1) {
                System.out.println("------EXEMPLARES------");
                List<Exemplar> exemplares = View.verExemplares();
                for (Exemplar e : exemplares) {
                    Livros livros = new Livros();
                    Livro l = livros.listarId(e.getIdLivro());
                    Generos generos = new Generos();
                    Genero g = generos.listarId(e.getIdGenero());
                    String nomeLivro = l.getTitulo(); 
                    String nomeGenero = g.getDescricao();
                    String situacao = e.getSituacao() ? "Disponível" : "Emprestado";
                
                    System.out.println(String.format("ID: %d\nEdição: %d\nEditora: %s\nSituacao: %s\nLivro: %s\nGenero: %s",
                            e.getId(), e.getEdicao(), e.getEditora(), situacao, nomeLivro, nomeGenero));
                    System.out.println("------------------");
                }
            } else if (opMenu == 2) {
                System.out.println("------EMPRÉSTIMOS-----");
                menuEmprestimo(usuario);
                
            } else if (opMenu == 3) {
                return;
            }
        } 
    }

    public static void menuEmprestimo(Usuario usuario){
        int opEmprestimo = 0;
        while (opEmprestimo != 3){
            System.out.println("O que deseja?");
            System.out.println("1 - Solicitar aumento de prazo\n2 - Ver empréstimos\n3 - Voltar para tela inicial");
            System.out.print("Digite sua opção: ");
            opEmprestimo = input.nextInt();
            
            if (opEmprestimo == 1) {
                List<Emprestimo> emprestimos = View.consultarEmprestimos(usuario.getId());

                if (emprestimos.isEmpty()) {
                    System.out.println("Você não possui empréstimos ativos.");
                    return;
                }

                System.out.println("Escolha o empréstimo para aumentar o prazo:");
                for (int i = 0; i < emprestimos.size(); i++) {
                    Emprestimo emp = emprestimos.get(i);
                    Exemplar e = new Exemplares().listarId(emp.getIdExemplar());
                    Livro l = new Livros().listarId(e.getIdLivro());
                    System.out.println((i + 1) + " - Livro: " + l.getTitulo() + ", Edição: " + e.getEdicao() + ", Data de devolução: " + emp.getDataDevolucao());
                }

                System.out.print("Digite o número do empréstimo para o qual deseja aumentar o prazo: ");
                int indiceEmprestimo = input.nextInt() - 1;

                if (indiceEmprestimo < 0 || indiceEmprestimo >= emprestimos.size()) {
                    System.out.println("Opção inválida.");
                    return;
                }
    
                Emprestimo emprestimoSelecionado = emprestimos.get(indiceEmprestimo);

                System.out.print("Digite quantos dias deseja para aumentar o prazo da devolução. (Máximo 10 dias):");
                int prazoExtendido = input.nextInt();

                try {
                    View.aumentarPrazo(prazoExtendido, usuario.getId(), emprestimoSelecionado.getId());
                    System.out.println("Data de devolução alterada");
                } catch (IllegalArgumentException e) {
                    System.out.println(e.getMessage());
                }
            } else if (opEmprestimo == 2) {
                List<Emprestimo> emprestimos = View.consultarEmprestimos(usuario.getId());
                if (emprestimos.isEmpty()) {
                    System.out.println("Você não possui empréstimos ativos.");
                    return;
                }

                for (int i = 0; i < emprestimos.size(); i++) {
                    Emprestimo emp = emprestimos.get(i);
                    Exemplar e = new Exemplares().listarId(emp.getIdExemplar());
                    Livro l = new Livros().listarId(e.getIdLivro());
                    System.out.println((i + 1) + " - Livro: " + l.getTitulo() + ", Edição: " + e.getEdicao() + ", Data de devolução: " + emp.getDataDevolucao());
                }
            } else if (opEmprestimo == 3) {
                return;
            }
        }
    }
}