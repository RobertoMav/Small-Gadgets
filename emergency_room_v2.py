import random

class Paciente:
    def __init__(self, id):
        self.id = id
        self.tempo_espera = 0
        self.tempo_triagem = 0
        self.tempo_atendimento = 0
        self.risco = None

class Emergencia:
    def __init__(self):
        self.sala_espera = []
        self.filas_atendimento = {
            'vermelho': [],
            'amarelo': [],
            'verde': [],
            'azul': [],
            'preferencial': []
        }
        self.atendente_disponivel = True
        self.medicos_disponiveis = 3
        self.tempo_total_espera_sala = 0
        self.tempo_total_espera_filas = {
            'vermelho': 0,
            'amarelo': 0,
            'verde': 0,
            'azul': 0,
            'preferencial': 0
        }
        self.pacientes_encaminhados = 0

    def entrada_paciente(self):
        if random.random() < 0.5:
            if len(self.sala_espera) < 50:
                paciente = Paciente(len(self.sala_espera) + 1)
                self.sala_espera.append(paciente)
            else:
                print("Sala de espera lotada. Paciente vai embora.")

    def triagem(self):
        for paciente in self.sala_espera:
            if paciente.tempo_triagem == 0:
                paciente.tempo_triagem = random.randint(1, 3)
            paciente.tempo_triagem -= 1

            if paciente.tempo_triagem == 0:
                paciente.risco = random.choice(['vermelho', 'amarelo', 'verde', 'azul'])
                self.filas_atendimento[paciente.risco].append(paciente)
                self.tempo_total_espera_filas[paciente.risco] += paciente.tempo_espera

    def atendimento(self):
        if self.atendente_disponivel:
            for risco in ['vermelho', 'amarelo', 'verde', 'azul', 'preferencial']:
                if len(self.filas_atendimento[risco]) > 0:
                    paciente = self.filas_atendimento[risco].pop(0)
                    self.atendente_disponivel = False
                    paciente.tempo_atendimento = random.randint(2, 5)
                    break

    def atualizar_pacientes(self):
        for paciente in self.sala_espera:
            paciente.tempo_espera += 1
            if paciente.tempo_espera > 50:
                paciente.risco = 'preferencial'
                self.filas_atendimento['preferencial'].append(paciente)
                self.tempo_total_espera_filas['preferencial'] += paciente.tempo_espera

    def simular(self, num_iteracoes):
        for _ in range(num_iteracoes):
            self.entrada_paciente()
            self.triagem()
            self.atendimento()
            self.atualizar_pacientes()

            if not self.atendente_disponivel and self.medicos_disponiveis > 0:
                self.atendente_disponivel = True
                self.medicos_disponiveis -= 1

            if len(self.filas_atendimento['preferencial']) > 10:
                self.pacientes_encaminhados += len(self.sala_espera)
                self.sala_espera = []
                break

        self.calcular_resultados()

    def calcular_resultados(self):
        nao_atendidos = max(0, len(self.sala_espera) - 50)
        tempo_medio_espera_sala = sum(paciente.tempo_espera for paciente in self.sala_espera) / len(self.sala_espera) if len(self.sala_espera) > 0 else 0
        tempo_medio_espera_filas = {risco: (self.tempo_total_espera_filas[risco] / len(self.filas_atendimento[risco])) if len(self.filas_atendimento[risco]) > 0 else 0 for risco in self.filas_atendimento.keys()}

        print("Quantidade de pacientes não atendidos por lotação na sala de espera:", nao_atendidos)
        print("Tempo médio de espera na sala de espera:", tempo_medio_espera_sala)
        print("Tempo médio de espera em cada fila de atendimento:")
        for risco, tempo_medio in tempo_medio_espera_filas.items():
            print(f"{risco}: {tempo_medio}")
        print("Número de interrupções no ingresso:", self.pacientes_encaminhados)

# Execução da simulação
emergencia = Emergencia()
emergencia.simular(100)
