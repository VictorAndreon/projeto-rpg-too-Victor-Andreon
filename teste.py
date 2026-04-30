from personagem import Personagem
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao

personagem = Personagem("Andreon")

missao_coleta = MissaoColeta(
    nome="Coleta de Ervas",
    descricao="Colete ervas medicinais na floresta",
    recompensa=30,
    item_necessario="Erva Medicinal",
    quantidade_item=10
)

missao_conquista = MissaoExploracao(
    nome="Travessia do Deserto",
    descricao="Explore e atravesse o deserto de Arenor",
    recompensa=50,
    regiao_destino="Deserto de Arenor",
    distancia_em_km=100.0
)

personagem.add_missao(missao_coleta)
personagem.add_missao(missao_conquista)

arma       = personagem.inventario[0]
vestimenta = personagem.inventario[1]
utilitario = personagem.inventario[2]

print("=== Iniciando missão de coleta ===")
personagem.iniciar_missao(missao_coleta, arma=arma, vestimenta=vestimenta, utilitario=utilitario)
print()
personagem.exibir_dados()

print()
print("=== Concluindo missão de coleta (sucesso) ===")
personagem.concluir_missao(missao_coleta, 15)
print()
personagem.exibir_dados()

print()
print("=== Iniciando missão de exploração ===")
personagem.iniciar_missao(missao_conquista, arma=arma, vestimenta=vestimenta, utilitario=utilitario)
print()
print("=== Concluindo missão de exploração (fracasso) ===")
personagem.concluir_missao(missao_conquista, 60.0)
print()
personagem.exibir_dados()
