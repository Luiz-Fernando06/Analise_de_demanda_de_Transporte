# Análise de Padrões de Demanda — Uber (Abril/2014)


## Objetivo:
Identificar os períodos de maior demanda de corridas, tanto por hora quanto por dia da semana.

## Principais insights:

- Horário de pico: Observei que as corridas se concentram principalmente no período noturno, com o maior volume em torno das {horario_maior_demanda.idxmax()}h, indicando forte demanda após o expediente e início da noite.

- Dia da semana com maior movimento: O dia com maior número de corridas foi {semana_maior_demanda.idxmax()}, o que pode refletir um aumento em deslocamentos sociais e de lazer.

- Comportamento semanal: A análise cruzada entre dia da semana e hora do dia (heatmap) evidencia padrões regulares de mobilidade — por exemplo, horários de pico concentrados em dias úteis e aumento mais distribuído nos fins de semana.

## Interpretação do heatmap:

- Cada linha representa um dia da semana, e cada coluna, uma hora do dia (0–23h).

- As células indicam a quantidade de corridas realizadas naquele intervalo.

- Áreas mais escuras (ou com valores mais altos) correspondem a picos de demanda, úteis para otimização de frota e estratégias de preço dinâmico.
