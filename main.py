import logging

# Configuração do logging
logging.basicConfig(filename='torneio.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Partida:
    def __init__(self, time1, time2, gols_time1, gols_time2):
        self.time1 = time1
        self.time2 = time2
        self.gols_time1 = gols_time1
        self.gols_time2 = gols_time2

    def __str__(self):
        return f"{self.time1} {self.gols_time1} x {self.gols_time2} {self.time2}"

class Torneio:
    def __init__(self):
        self.times = []
        self.partidas = []

    def adicionar_time(self, nome):
        try:
            if not nome or nome.strip() == "":
                raise ValueError("Nome inválido")
            if nome in self.times:
                raise ValueError(f"Time '{nome}' já foi adicionado.")
            self.times.append(nome)
            print(f"✅ Time \"{nome}\" adicionado com sucesso!")
        except ValueError as e:
            print(f"❌ Erro: {e}")
            logging.error(f"Erro ao adicionar time '{nome}': {e}")

    def criar_partida(self, time1, time2, gols_time1, gols_time2):
        try:
            # Verifica se os dois times existem no torneio
            if time1 not in self.times:
                raise ValueError(f"❌ Erro: O time '{time1}' não existe.")
            if time2 not in self.times:
                raise ValueError(f"❌ Erro: O time '{time2}' não existe.")
            if gols_time1 < 0 or gols_time2 < 0:
                raise ValueError("Número inválido de gols")
            partida = Partida(time1, time2, gols_time1, gols_time2)
            self.partidas.append(partida)
            print(f"✅ Partida entre \"{time1}\" e \"{time2}\" criada com sucesso!")
        except ValueError as e:
            print(f"{e}")
            logging.error(f"Erro na criação da partida entre '{time1}' e '{time2}': {e}")

    def jogar(self):
        resultado = ResultadoTorneio()
        for partida in self.partidas:
            resultado.adicionar_resultado(partida)
        return resultado

class ResultadoTorneio:
    def __init__(self):
        self.classificacao = {}
        self.resultados = []

    def adicionar_resultado(self, partida):
        # Atualiza a classificação
        if partida.time1 not in self.classificacao:
            self.classificacao[partida.time1] = 0
        if partida.time2 not in self.classificacao:
            self.classificacao[partida.time2] = 0

        if partida.gols_time1 > partida.gols_time2:
            self.classificacao[partida.time1] += 3
        elif partida.gols_time2 > partida.gols_time1:
            self.classificacao[partida.time2] += 3
        else:
            self.classificacao[partida.time1] += 1
            self.classificacao[partida.time2] += 1

        # Registra o resultado da partida
        self.resultados.append(str(partida))

    def imprimir_classificacao(self):
        print("\nClassificação Final:")
        classificacao_ordenada = sorted(self.classificacao.items(), key=lambda x: x[1], reverse=True)
        for i, (time, pontos) in enumerate(classificacao_ordenada):
            print(f"{i + 1}. {time} ({pontos} pontos)")

    def imprimir_resultados(self):
        print("\nResultados:")
        for resultado in self.resultados:
            print(resultado)

def obter_nome_time():
    while True:
        nome_time = input("Digite o nome do time para adicionar (ou 'sair' para parar): ").strip()
        if nome_time.lower() == 'sair':
            return None
        if nome_time:
            return nome_time
        print("❌ Erro: Nome inválido. Tente novamente.")

def obter_partida(torneio):
    while True:
        time1 = input("Digite o nome do primeiro time para a partida (ou 'sair' para parar): ").strip()
        if time1.lower() == 'sair':
            return None, None, None, None

        time2 = input("Digite o nome do segundo time para a partida: ").strip()
        # Verifica se ambos os times existem no torneio
        if time1 not in torneio.times:
            print(f"❌ Erro: O time '{time1}' não existe no torneio.")
            continue
        if time2 not in torneio.times:
            print(f"❌ Erro: O time '{time2}' não existe no torneio.")
            continue

        try:
            gols_time1 = int(input(f"Digite o número de gols do {time1}: "))
            gols_time2 = int(input(f"Digite o número de gols do {time2}: "))

            # Validação dos gols não podem ser negativos
            if gols_time1 < 0 or gols_time2 < 0:
                print("❌ Erro: Número inválido de gols. O número de gols não pode ser negativo.")
                continue

            return time1, time2, gols_time1, gols_time2
        except ValueError:
            print("❌ Erro: Por favor, insira números válidos para os gols.")

def main():
    torneio = Torneio()

    # Adicionando times
    while True:
        nome_time = obter_nome_time()
        if nome_time is None:
            break
        torneio.adicionar_time(nome_time)

    # Criando partidas
    while True:
        time1, time2, gols_time1, gols_time2 = obter_partida(torneio)
        if time1 is None:
            break
        torneio.criar_partida(time1, time2, gols_time1, gols_time2)

    # Exibe a classificação final e o resultado de cada partida
    resultados = torneio.jogar()
    resultados.imprimir_classificacao()
    resultados.imprimir_resultados()

if __name__ == "__main__":
    main()
