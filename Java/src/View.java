import java.util.List;

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

    public static void verExemplares(){
        Exemplares exe = new Exemplares();
        List<Exemplar> exemplares = exe.listar();

        for (Exemplar e : exemplares) {
            System.out.println(e);
        }
    }

    public static Emprestimo consultarEmprestimo(int id) {
        Emprestimos emp = new Emprestimos();
        List<Emprestimo> emprestimos = emp.listar();

        for (Emprestimo em : emprestimos) {
            if (em.getIdUsuario() == id) {
                return em;
            }
        }
        return null;
    }
}