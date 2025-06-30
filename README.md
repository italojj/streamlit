------------------------------------------------ ENGLISH VERSION -----------------------------------------------------------

User Manual: Application for Network Analysis

This manual describes how to use the network analysis tool and its features.
User interface:
All of the network's filtering and customization controls are located in the sidebar.

Main Panel: Shows interactive graph visualization and stats.
1. Options for the Sidebar

1.1. Options for Analysis
Treat as a directed graph: considers links to be arrows (A → B). has an impact on how certain metrics are calculated.
You can concentrate on particular areas of the network by using the display subgraph.
Full Network: Shows the network as a whole.
Only the nodes with the strongest connections are shown in a high-degree subgraph. You can adjust the minimum number of connections using a slider.

1.2. Node Highlighting in Visualization
Select a centrality metric (Degree, Betweenness, etc.) to draw attention to the most significant nodes.
The quantity of nodes to be highlighted (Top-K): Determine the number of top nodes that should be red-highlighted.

1.3. Options for Layout
The layout/physics algorithm regulates how the network looks and moves.
BarnesHut is the default, although it may not perform well on networks with a lot of nodes and edges.
In general, Force Atlas 2 is more stable.
Repulsion: Basic model of repulsion.
The network is frozen in a static view when Physics is disabled.

2. Main Panel Analysis
2.1. Structural Metrics
Nodes and Edges: The total number of nodes and edges in the graph that is shown.
Density/Sparsity: Indicates the degree of network connectivity (0 = sparse, 1 = dense).
Assortativity: Shows if nodes with a lot of connections are connected to other nodes of the same degree (value > 0) or different degree (value < 0). The ability of nodes to form clusters is measured by global clustering.

2.2. Component Analysis
displays how many node "clusters" or "islands" there are. in the network. The analysis varies depending on whether the graph is directed or undirected.

2.3. Degree Distribution
The histogram shows how many nodes have few or many connections. For directed graphs, you can analyze in-degree, out-degree, or total.

2.4. Nodee Centrality Analysis
The table ranks nodes by importance according to several metrics. Click a column header to sort.

2.5. Interactive Visualization
Interact: Zoom, drag nodes, and move the network.
Configuration Panel: Use the panel at the top of the visualization to fine-tune layout, colors, and physics.

---------------------------------------------- VERSÃO EM PORTUGUÊS ------------------------------------------------------

Manual do Usuário: Aplicativo para Análise de Redes

Este manual descreve como usar a ferramenta de análise de redes e seus recursos.
Interface do usuário:
Todos os controles de filtragem e personalização da rede estão localizados na barra lateral.

Painel Principal: Exibe a visualização gráfica interativa e estatísticas.
1. Opções da Barra Lateral

1.1. Opções de Análise
Tratar como um gráfico direcionado: considera os links como setas (A → B). A ferramenta influencia o cálculo de determinadas métricas.
Você pode se concentrar em áreas específicas da rede usando o subgráfico de exibição.
Rede Completa: Exibe a rede como um todo.
Somente os nós com as conexões mais fortes são exibidos em um subgráfico de alto grau. Você pode ajustar o número mínimo de conexões usando um controle deslizante.

1.2. Destaque de Nós na Visualização
Selecione uma métrica de centralidade (Grau, Intermediação, etc.) para destacar os nós mais significativos.
Quantidade de nós a serem destacados (Top-K): Determine o número de nós superiores que devem ser destacados em vermelho.

1.3. Opções de Layout
O algoritmo de layout/física regula a aparência e o movimento da rede.
BarnesHut é o padrão, embora possa não ter um bom desempenho em redes com muitos nós e arestas.
Em geral, o Force Atlas 2 é mais estável.
Repulsão: Modelo básico de repulsão.
A rede fica congelada em uma visão estática quando a Física está desabilitada.

2. Análise do Painel Principal
2.1. Métricas Estruturais
Nós e Arestas: O número total de nós e arestas no grafo que é exibido.
Densidade/Esparsidade: Indica o grau de conectividade da rede (0 = esparsa, 1 = densa).
Assortatividade: Mostra se nós com muitas conexões estão conectados a outros nós do mesmo grau (valor > 0) ou de grau diferente (valor < 0). A capacidade dos nós de formar clusters é medida pelo agrupamento global.

2.2. Análise de Componentes
exibe quantos "clusters" ou "ilhas" de nós existem na rede. A análise varia dependendo se o grafo é direcionado ou não direcionado.

2.3. Distribuição de Graus
O histograma mostra quantos nós têm poucas ou muitas conexões. Para grafos direcionados, você pode analisar em graus de entrada, graus de saída ou total.

2.4. Análise de Centralidade de Nós
A tabela classifica os nós por importância, de acordo com diversas métricas. Clique no cabeçalho de uma coluna para classificar.

2.5. Visualização Interativa
Interagir: Aplique zoom, arraste nós e mova a rede.
Painel de Configuração: Use o painel na parte superior da visualização para ajustar o layout, as cores e a física.
