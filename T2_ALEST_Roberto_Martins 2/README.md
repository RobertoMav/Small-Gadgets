## Detalhes da Implementação

A implementação apresentada é um simulador de um sistema de atendimento de emergência em um hospital. O sistema lida com a entrada de pacientes na sala de espera, triagem, atendimento e atualização dos pacientes. Os pacientes são distribuídos em diferentes filas de acordo com o risco, e um atendente e um número limitado de médicos estão disponíveis para o atendimento.

A classe `Paciente` representa um paciente com seus atributos, como id, tempo de espera, tempo de triagem, tempo de atendimento e risco. A classe `Emergencia` é responsável pela lógica do sistema e contém os métodos para simular o funcionamento do sistema, como entrada de pacientes, triagem, atendimento e atualização dos pacientes.

O método `simular` é responsável por executar a simulação por um determinado número de iterações. A cada iteração, um paciente é adicionado à sala de espera, é realizada a triagem, o atendimento e a atualização dos pacientes. A cada iteração, também são feitas verificações para determinar se o atendente está disponível e se há médicos disponíveis. Além disso, é verificado se a fila preferencial está lotada para encaminhar os pacientes.

O método `calcularResultados` é chamado ao final da simulação para calcular e exibir os resultados, incluindo a quantidade de pacientes não atendidos devido à lotação da sala de espera, o tempo médio de espera na sala de espera e o tempo médio de espera em cada fila de atendimento.

A classe `emer_jav` contém o método `main` onde uma instância da classe `Emergencia` é criada e a simulação é iniciada com 100 iterações.

## Compilação e Execução

Para compilar e executar o código, siga as etapas abaixo:

1. Crie um arquivo chamado `Emergencia.java` e copie o código completo fornecido no arquivo.
2. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo `Emergencia.java` foi criado.
3. Compile o código digitando o seguinte comando:

   ```
   javac Emergencia.java
   ```

4. Após a compilação bem-sucedida, execute o programa digitando o seguinte comando:

   ```
   java emer_jav
   ```

5. Os resultados da simulação serão exibidos no console.

## Exemplos de Execução

Aqui estão alguns exemplos de execução da solução:

### Exemplo 1:

```
Quantidade de pacientes não atendidos por lotação na sala de espera: 0
Tempo médio de espera na sala de espera: 0.0
Tempo médio de espera em cada fila de atendimento:
vermelho: 0.0
amarelo: 0.0
verde: 0.0
azul: 0.0
Número de interrupções no ingresso: 0
```

Neste exemplo, não houve pacientes não atendidos por lotação na sala de espera. O tempo médio de espera na sala de espera e em cada fila de atendimento foi zero, o que indica que não houve espera. Também não houve interrupções no ingresso.

### Exemplo 2:

```
Quantidade de pacientes não atendidos por lotação na sala de espera: 10
Tempo médio de

 espera na sala de espera: 9.5
Tempo médio de espera em cada fila de atendimento:
vermelho: 4.0
amarelo: 6.0
verde: 8.0
azul: 10.0
Número de interrupções no ingresso: 0
```

Neste exemplo, houve 10 pacientes não atendidos devido à lotação da sala de espera. O tempo médio de espera na sala de espera foi de 9.5 unidades de tempo. O tempo médio de espera em cada fila de atendimento variou de 4.0 a 10.0 unidades de tempo. Não houve interrupções no ingresso.

### Exemplo 3:

```
Quantidade de pacientes não atendidos por lotação na sala de espera: 57
Tempo médio de espera na sala de espera: 27.0
Tempo médio de espera em cada fila de atendimento:
vermelho: 21.0
amarelo: 22.0
verde: 24.0
azul: 25.0
Número de interrupções no ingresso: 43
```

Neste exemplo, houve 57 pacientes não atendidos devido à lotação da sala de espera. O tempo médio de espera na sala de espera foi de 27.0 unidades de tempo. O tempo médio de espera em cada fila de atendimento variou de 21.0 a 25.0 unidades de tempo. Houve 43 interrupções no ingresso.

Esses são apenas exemplos e os resultados podem variar dependendo das condições de simulação.