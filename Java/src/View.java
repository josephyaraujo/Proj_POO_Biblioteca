import java.util.ArrayList;
import java.util.List;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class View {
    public static Usuario usuarioAutenticar(String email, String senha){
        Usuarios usuModelo = new Usuarios();
        List<Usuario> usuarios = usuModelo.listar();
        for (Usuario u : usuarios) {
            if (u.getEmail().equals(email) && u.getSenha().equals(senha)){
                if (u.getTipoUsuario() == EnumUsuarios.ADMIN || u.getTipoUsuario() == EnumUsuarios.FUNCIONARIO) {
                    return null;
                } else {
                    return u;
                }
            }         
        }
        return null;
    }

    public static void clienteInserir(String nome, String email, String fone, String senha, EnumUsuarios tipoUsuario){
        Usuarios usuModelo = new Usuarios();
        List<Usuario> usuarios = usuModelo.listar();

        for (Usuario u : usuarios) {
            if (u.getEmail() == email) {
                throw new IllegalArgumentException("Email já cadastrado");
            } else if (u.getFone() == fone) {
                throw new IllegalArgumentException("Telefone já cadastrado");
            }
        }

        Usuario usu = new Usuario(0, nome, email, fone, senha, EnumUsuarios.CLIENTE);
        usuModelo.inserir(usu);
    }

    public static List<Exemplar> verExemplares(){
        Exemplares exe = new Exemplares();
        List<Exemplar> exemplares = exe.listar();
        return exemplares;
    }

    public static List<Emprestimo> consultarEmprestimos(int id) {
        Emprestimos emp = new Emprestimos();
        List<Emprestimo> emprestimos = emp.listar();
        List<Emprestimo> emprestimosUsuario = new ArrayList<>();

        for (Emprestimo em : emprestimos) {
            if (em.getIdUsuario() == id) {
                emprestimosUsuario.add(em);
            }
        }
        return emprestimosUsuario;
    }

    public static Exemplar exemplarListarId(int id) {
        Exemplares ex = new Exemplares();
        return ex.listarId(id);
    }

    public static void aumentarPrazo(int prazoExtendido, int id, int idEmprestimo) {
        Emprestimos emp = new Emprestimos();
        List<Emprestimo> emprestimos = emp.listar();
        Emprestimo emAtualizado = null;

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        for (Emprestimo em : emprestimos) {
            if (em.getIdUsuario() == id && em.getId() == idEmprestimo) {
                LocalDate dataDevolucao = LocalDate.parse(em.getDataDevolucao(), formatter);
                LocalDate novaDataDevolucao = dataDevolucao.plusDays(prazoExtendido);
                String novaDataDevolucaoStr = novaDataDevolucao.format(formatter);

                emAtualizado = new Emprestimo(em.getId(), em.getData(), novaDataDevolucaoStr, em.getPrazoExtendido() + prazoExtendido, em.getIdExemplar(), em.getIdUsuario());
                break;
            }
        }
        emp.atualizar(emAtualizado);
    }
}