
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

class Paciente {
private int id;
private int tempo_espera;
private int tempo_triagem;
private int tempo_atendimento;
private String risco;

public Paciente(int id) {
    this.id = id;
    this.tempo_espera = 0;
    this.tempo_triagem = 0;
    this.tempo_atendimento = 0;
    this.risco = null;
}

public int getId() {
    return id;
}

public int getTempoEspera() {
    return tempo_espera;
}

public int getTempoTriagem() {
    return tempo_triagem;
}

public int getTempoAtendimento() {
    return tempo_atendimento;
}

public String getRisco() {
    return risco;
}

public void setRisco(String risco) {
    this.risco = risco;
}

}

class Emergencia {
private List<Paciente> sala_espera;
private Map<String, List<Paciente>> filas_atendimento;
private boolean atendente_disponivel;
private int medicos_disponiveis;
private int tempo_total_espera_sala;
private Map<String, Integer> tempo_total_espera_filas;
private int pacientes_encaminhados;

public Emergencia() {
    this.sala_espera = new ArrayList<>();
    this.filas_atendimento = new HashMap<>();
    this.filas_atendimento.put("vermelho", new ArrayList<>());
    this.filas_atendimento.put("amarelo", new ArrayList<>());
    this.filas_atendimento.put("verde", new ArrayList<>());
    this.filas_atendimento.put("azul", new ArrayList<>());
    this.filas_atendimento.put("preferencial", new ArrayList<>());
    this.atendente_disponivel = true;
    this.medicos_disponiveis = 3;
    this.tempo_total_espera_sala = 0;
    this.tempo_total_espera_filas = new HashMap<>();
    this.tempo_total_espera_filas.put("vermelho", 0);
    this.tempo_total_espera_filas.put("amarelo", 0);
    this.tempo_total_espera_filas.put("verde", 0);
    this.tempo_total_espera_filas.put("azul", 0);
    this.tempo_total_espera_filas.put("preferencial", 0);
    this.pacientes_encaminhados = 0;
}

public void entradaPaciente() {
    Random random = new Random();
    if (random.nextDouble() < 0.5) {
        if (sala_espera.size() < 50) {
            Paciente paciente = new Paciente(sala_espera.size() + 1);
            sala_espera.add(paciente);
        } else {
            System.out.println("Sala de espera lotada. Paciente vai embora.");
        }
    }
}

public void triagem() {
    for (Paciente paciente : sala_espera) {
        if (paciente.getTempoTriagem() == 0) {
            paciente.setTempoTriagem(new Random().nextInt(3) + 1);
        }
        paciente.setTempoTriagem(paciente.getTempoTriagem() - 1);

        if (paciente.getTempoTriagem() == 0) {
            String risco = getRandomRisco();
            paciente.setRisco(risco);
            filas_atendimento.get(risco).add(paciente);
            tempo_total_espera_filas.put(risco, tempo_total_espera_filas.get(risco) + paciente.getTempoEspera());
        }
    }
}

public void atendimento() {
    if (atendente_disponivel) {
        for (String risco : new String[]{"vermelho", "amarelo", "verde", "azul", "preferencial"}) {
            List<Paciente> filaAtendimento = filas_atendimento.get(risco);
            if (!filaAtendimento.isEmpty()) {
                Paciente paciente = filaAtendimento.remove(0);
                atendente_disponivel = false;
                paciente.setTempoAtendimento(new Random().nextInt(4) + 2);
                break;
            }
        }
    }
}

public void atualizarPacientes() {
    for (Paciente paciente : sala_espera) {
        paciente.setTempoEspera(paciente.getTempoEspera() + 1);
        if (paciente.getTempoEspera() > 50) {
            paciente.setRisco("preferencial");
            filas_atendimento.get("preferencial").add(paciente);
            tempo_total_espera_filas.put("preferencial", tempo_total_espera_filas.get("preferencial") + paciente.getTempoEspera());
        }
    }
}

public void simular(int num_iteracoes) {
    for (int i = 0; i < num_iteracoes; i++) {
        entradaPaciente();
        triagem();
        atendimento();
        atualizarPacientes();

        if (!atendente_disponivel && medicos_disponiveis > 0) {
            atendente_disponivel = true;
            medicos_disponiveis--;
        }

        if (filas_atendimento.get("preferencial").size() > 10) {
            pacientes_encaminhados += sala_espera.size();
            sala_espera.clear();
            break;
        }
    }

    calcularResultados();
}

public void calcularResultados() {
    int nao_atendidos = Math.max(0, sala_espera.size() - 50);
    double tempo_medio_espera_sala = sala_espera.isEmpty() ? 0 : sala_espera.stream().mapToInt(Paciente::getTempoEspera).average().orElse(0);
    Map<String, Double> tempo_medio_espera_filas = new HashMap<>();
    for (String risco : filas_atendimento.keySet()) {
        List<Paciente> filaAtendimento = filas_atendimento.get(risco);
        double tempo_medio = filaAtendimento.isEmpty() ? 0 : filaAtendimento.stream().mapToInt(Paciente::getTempoEspera).average().orElse(0);
        tempo_medio_espera_filas.put(risco, tempo_medio);
    }

    System.out.println("Quantidade de pacientes não atendidos por lotação na sala de espera: " + nao_atendidos);
    System.out.println("Tempo médio de espera na sala de espera: " + tempo_medio_espera_sala);
    System.out.println("Tempo médio de espera em cada fila de atendimento:");
    for (String risco : tempo_medio_espera_filas.keySet()) {
        System.out.println(risco + ": " + tempo_medio_espera_filas.get(risco));
    }
    System.out.println("Número de interrupções no ingresso: " + pacientes_encaminhados);
}

private String getRandomRisco() {
    String[] riscos = {"vermelho", "amarelo", "verde", "azul"};
    return riscos[new Random().nextInt(riscos.length)];
}
}

public class Main {
public static void main(String[] args) {
Emergencia emergencia = new Emergencia();
emergencia.simular(100);
}
}