import random

class Paciente:
    def __init__(self, id):
        self.id = id
        self.tempo_espera = 0
        self.tempo_triagem = 0
        self.tempo_atendimento = 0
        self.risco = None

class SalaEspera:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        if len(self.pacientes) < self.capacidade:
            self.pacientes.append(paciente)
        else:
            print(f'Paciente {paciente.id} foi embora por falta de vagas na sala de espera.')

    def remover_paciente(self, paciente):
        self.pacientes.remove(paciente)

    def atualizar_tempos_espera(self):
        for paciente in self.pacientes:
            paciente.tempo_espera += 1

class FilaAtendimento:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def remover_paciente(self, paciente):
        self.pacientes.remove(paciente)

    def atualizar_tempos_atendimento(self):
        for paciente in self.pacientes:
            paciente.tempo_atendimento += 1

class Emergencia:
    def __init__(self):
        self.sala_espera = SalaEspera(50)
        self.fila_vermelha = FilaAtendimento()
        self.fila_amarela = FilaAtendimento()
        self.fila_verde = FilaAtendimento()
        self.fila_azul = FilaAtendimento()
        self.atendente_disponivel = True
        self.medicos_disponiveis = 3
        self.atendimentos_preferenciais = 0
        self.interrupcoes_ingresso = 0
        self.total_pacientes_lotacao = 0
        self.total_tempo_espera_sala_espera = 0
        self.total_tempo_espera_filas = {
            'Vermelho': 0,
            'Amarelo': 0,
            'Verde': 0,
            'Azul': 0
        }
        self.pacientes_atendidos = 0

    def adicionar_paciente_sala_espera(self, paciente):
        if len(self.sala_espera.pacientes) < self.sala_espera.capacidade:
            self.sala_espera.adicionar_paciente(paciente)
        else:
            self.total_pacientes_lotacao += 1
            print(f'Paciente {paciente.id} foi embora por lotação na sala de espera.')

    def realizar_triagem(self, paciente):
        paciente.tempo_triagem = random.randint(1, 3)
        paciente.risco = random.choice(['Vermelho', 'Amarelo', 'Verde', 'Azul'])

        if paciente.risco == 'Vermelho':
            self.fila_vermelha.adicionar_paciente(paciente)
        elif paciente.risco == 'Amarelo':
            self.fila_amarela.adicionar_paciente(paciente)
        elif paciente.risco == 'Verde':
            self.fila_verde.adicionar_paciente(paciente)
        elif paciente.risco == 'Azul':
            self.fila_azul.adicionar_paciente(paciente)

        self.sala_espera.remover_paciente(paciente)

    def atender_pacientes(self):
        if self.atendente_disponivel:
            if self.atendimentos_preferenciais >= 10:
                print('Ingresso bloqueado devido a atendimentos preferenciais.')
                self.interrupcoes_ingresso += 1
                return

            if len(self.fila_vermelha.pacientes) > 0:
                paciente = self.fila_vermelha.pacientes[0]
                if paciente.tempo_atendimento >= 2:
                    self.fila_vermelha.remover_paciente(paciente)
                    self.finalizar_atendimento(paciente)
                else:
                    paciente.tempo_atendimento += 1
            elif len(self.fila_amarela.pacientes) > 0:
                paciente = self.fila_amarela.pacientes[0]
                if paciente.tempo_atendimento >= 2:
                    self.fila_amarela.remover_paciente(paciente)
                    self.finalizar_atendimento(paciente)
                else:
                    paciente.tempo_atendimento += 1
            elif len(self.fila_verde.pacientes) > 0:
                paciente = self.fila_verde.pacientes[0]
                if paciente.tempo_atendimento >= 2:
                    self.fila_verde.remover_paciente(paciente)
                    self.finalizar_atendimento(paciente)
                else:
                    paciente.tempo_atendimento += 1
            elif len(self.fila_azul.pacientes) > 0:
                paciente = self.fila_azul.pacientes[0]
                if paciente.tempo_atendimento >= 2:
                    self.fila_azul.remover_paciente(paciente)
                    self.finalizar_atendimento(paciente)
                else:
                    paciente.tempo_atendimento += 1
            else:
                print('Não há pacientes nas filas de atendimento.')

    def finalizar_atendimento(self, paciente):
        self.medicos_disponiveis += 1
        self.atendente_disponivel = False
        self.pacientes_atendidos += 1

        if paciente.tempo_espera > 50:
            self.atendimentos_preferenciais += 1
        else:
            if paciente.risco == 'Vermelho':
                self.total_tempo_espera_filas['Vermelho'] += paciente.tempo_espera
            elif paciente.risco == 'Amarelo':
                self.total_tempo_espera_filas['Amarelo'] += paciente.tempo_espera
            elif paciente.risco == 'Verde':
                self.total_tempo_espera_filas['Verde'] += paciente.tempo_espera
            elif paciente.risco == 'Azul':
                self.total_tempo_espera_filas['Azul'] += paciente.tempo_espera

        self.total_tempo_espera_sala_espera += paciente.tempo_espera

    def simular_emergencia(self, duracao_simulacao):
        for i in range(duracao_simulacao):
            print(f'\nRodada {i+1}:\n')

            if random.random() <= 0.5:
                paciente = Paciente(i+1)
                self.adicionar_paciente_sala_espera(paciente)

            self.sala_espera.atualizar_tempos_espera()
            self.atender_pacientes()

            print(f'\nPacientes na sala de espera: {len(self.sala_espera.pacientes)}')
            print(f'Pacientes na fila Vermelha: {len(self.fila_vermelha.pacientes)}')
            print(f'Pacientes na fila Amarela: {len(self.fila_amarela.pacientes)}')
            print(f'Pacientes na fila Verde: {len(self.fila_verde.pacientes)}')
            print(f'Pacientes na fila Azul: {len(self.fila_azul.pacientes)}')
            print(f'Médicos disponíveis: {self.medicos_disponiveis}')

        print('\n----- Fim da simulação -----\n')
        print(f'Quantidade de pacientes que não ficaram por lotação na sala de espera: {self.total_pacientes_lotacao}')
        print(f'Tempo médio de espera na sala de espera: {self.total_tempo_espera_sala_espera / self.pacientes_atendidos:.2f} unidades de tempo')

        for cor, tempo_espera in self.total_tempo_espera_filas.items():
            print(f'Tempo médio de espera na fila {cor}: {tempo_espera / self.pacientes_atendidos:.2f} unidades de tempo')

        print(f'Número de interrupções no ingresso: {self.interrupcoes_ingresso}')


# Exemplo de uso
emergencia = Emergencia()
emergencia.simular_emergencia(100)
