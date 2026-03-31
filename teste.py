from status import Status
from missao_coleta import MissaoColeta
from missao_combate import MissaoCombate
from missao_exploracao import MissaoExploracao

# --- Missão de Coleta ---
coleta = MissaoColeta(
    nome="Coleta de Ervas",
    descricao="Coletar ervas medicinais na floresta encantada",
    recompensa=20,
    item_necessario="Erva Medicinal",
    quantidade_item=10,
    status=Status.PENDENTE
)
coleta.iniciar_missao()
coleta.concluir_missao()
coleta.exibir_dados()

print()

# --- Missão de Combate ---
combate = MissaoCombate(
    nome="Caça aos Orcs",
    descricao="Eliminar os orcs que invadiram a vila",
    recompensa=50,
    tipo_inimigo="Orc",
    inimigos_a_derrotar=5,
    status=Status.PENDENTE
)
combate.iniciar_missao()
combate.concluir_missao()
combate.exibir_dados()

print()

# --- Missão de Exploração ---
exploracao = MissaoExploracao(
    nome="Ruínas do Norte",
    descricao="Explorar as antigas ruínas ao norte do reino",
    recompensa=35,
    regiao_destino="Ruínas do Reino Glacial",
    distancia_em_km=120.5,
    status=Status.PENDENTE
)
exploracao.iniciar_missao()
exploracao.concluir_missao()
exploracao.exibir_dados()
