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

print()

# Sucesso: coletou 15, precisava de 10
personagem.concluir_missao(missao_coleta, 15)

# Fracasso: percorreu 60 km, precisava de 100 km
personagem.concluir_missao(missao_conquista, 60.0)

print()
personagem.exibir_dados()

print()
missao_coleta.exibir_dados()
print()
missao_conquista.exibir_dados()
