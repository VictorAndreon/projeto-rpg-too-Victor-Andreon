from personagem import Personagem
from item import Item, TipoItem
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao

personagem = Personagem("Andreon")

print("=== Personagem criado ===")
personagem.exibir_dados()

print()
personagem.mostrar_inventario()

print()
print("=== Adicionando itens ao inventário ===")
cajado  = Item("Cajado Mágico",    "Amplifica poder arcano",  25, TipoItem.ARMA)
capa    = Item("Capa das Sombras", "Oferece proteção furtiva", 15, TipoItem.VESTIMENTA)
amuleto = Item("Amuleto da Sorte", "Aumenta a resistência",   5,  TipoItem.UTILITARIO)

personagem.add_item(cajado)
personagem.add_item(capa)
personagem.add_item(amuleto)

personagem.mostrar_inventario()

print()
print("=== Equipando itens para a missão ===")
arma       = personagem.inventario[0]
vestimenta = personagem.inventario[1]
utilitario = personagem.inventario[2]

ataque_total, vida_total = personagem.equiparItens(arma, vestimenta, utilitario)

print(f"Arma equipada:       {arma.nome} (+{arma.atributo} de ataque)")
print(f"Vestimenta equipada: {vestimenta.nome} (+{vestimenta.atributo}% de vida)")
print(f"Utilitário equipado: {utilitario.nome} (+{utilitario.atributo}% de vida)")
print(f"\nStatus para a missão:")
print(f"  Ataque total: {ataque_total}  (base {personagem.ataque_base} + {arma.atributo} da arma)")
print(f"  Vida total:   {vida_total}/{personagem.vida_maxima}  (base {personagem.vida_base} + {vestimenta.atributo + utilitario.atributo}%)")

print()
print("=== Substituindo arma equipada (swap) ===")
ataque_total, vida_total = personagem.equiparItens(cajado, vestimenta, utilitario)
print(f"Nova arma: {cajado.nome}")
print(f"  Ataque total: {ataque_total}  |  Vida total: {vida_total}")

print()
print("=== Missões ===")
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
