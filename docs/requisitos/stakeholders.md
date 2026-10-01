# 2. Mapa de Stakeholders

<svg viewBox="0 0 650 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%; height:auto;">
  <defs>
    <marker id="arrow4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#475569"/>
    </marker>
  </defs>
  <rect x="250" y="105" width="150" height="50" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>
  <text x="325" y="135" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1e3a8a">NSN</text>
  <rect x="20" y="20" width="140" height="50" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="90" y="50" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#166534">Vendedor</text>
  <rect x="20" y="190" width="140" height="50" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="90" y="220" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#166534">Comprador</text>
  <rect x="490" y="20" width="140" height="50" rx="10" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>
  <text x="560" y="50" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#854d0e">Curso (requisitos BLX)</text>
  <rect x="490" y="190" width="140" height="50" rx="10" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>
  <text x="560" y="220" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#854d0e">Desenvolvedora</text>
  <line x1="160" y1="55" x2="248" y2="115" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <text x="185" y="75" font-family="sans-serif" font-size="9" fill="#64748b">anuncia produtos</text>
  <line x1="160" y1="205" x2="248" y2="145" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <text x="185" y="200" font-family="sans-serif" font-size="9" fill="#64748b">faz pedidos</text>
  <line x1="490" y1="55" x2="402" y2="115" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <text x="415" y="75" font-family="sans-serif" font-size="9" fill="#64748b">define requisitos</text>
  <line x1="490" y1="205" x2="402" y2="145" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow4)"/>
  <text x="405" y="200" font-family="sans-serif" font-size="9" fill="#64748b">constrói e mantém</text>
</svg>

**Legenda:** 🟢 verde = usuários diretos do sistema · 🟡 amarelo = origem dos requisitos e manutenção

| Stakeholder | Relação com a solução | Interesse principal | Influência |
|---|---|---|---|
| Vendedor | Usuário final | Anunciar produtos e organizar seus pedidos recebidos | Alta |
| Comprador | Usuário final | Encontrar produtos e acompanhar seus pedidos | Alta |
| Curso TDS Backend (App BLX) | Origem dos requisitos | Servir de base para um projeto real de back-end | Média |
| Desenvolvedora (autora) | Responsável técnica | Entregar uma API correta, organizada e documentada | Alta |

## Observação sobre este mapa

Na plataforma, **a mesma pessoa pode ser vendedora e compradora** ao mesmo tempo: cada
usuário terá uma lista de pedidos recebidos (minhas vendas) e de pedidos feitos
(minhas compras). Os interesses descritos foram inferidos a partir dos requisitos do
curso e do contexto do problema, não de entrevistas reais. Essa é uma limitação
intencional deste documento, coerente com a origem do projeto.

## Histórico de Versão

| Data | Versão | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 2026-10-01 | 1.0 | Criação do mapa de stakeholders | Nayra |
