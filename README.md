
Aplicação para Consultar Licitações Publicadas no PNCP

Esta aplicação em Python permite aos usuários buscar todos os pregões eletrônicos por estado e data de publicação, filtrar as licitações cujo objeto possui determinadas palavras-chave e salvar os resultados em um arquivo Excel.

Funcionalidades:
Busca de Licitações: Realiza buscas por pregões eletrônicos em diferentes estados e datas de publicação.
Filtragem por Palavras-Chave: Filtra as licitações com base em palavras-chave definidas pelo usuário.
Exportação para Excel: Salva os resultados da pesquisa geral e da pesquisa filtrada em um arquivo Excel.
Estrutura do Arquivo Excel
Pesquisa Geral: Contém todas as licitações encontradas na busca.
Pesquisa Filtrada: Apresenta as licitações filtradas por palavras-chave.

Como Usar:
Clone o repositório para o seu ambiente local.
Instale as dependências necessárias utilizando pip install -r requirements.txt.
Ajuste os parâmetros de pesquisa:
Intervalo de Data: Defina o intervalo de tempo para a pesquisa.
UFs: Selecione os estados desejados.
Palavras-Chave: Defina as palavras-chave para a filtragem.
Execute o script principal para iniciar a busca e filtrar as licitações.
O arquivo Excel será gerado automaticamente na pasta especificada.
Dados Nacional de Compras Públicas

A Nova Lei de Licitações 14.133/2021 exige que todos os órgãos da administração pública centralizem as informações de suas contratações em um portal nacional. Com acesso a esse portal através da API, nossa aplicação busca oportunidades de negócios verificando as licitações publicadas. O processo envolve:
Filtro por Intervalo de Dias: Pesquise as licitações em um intervalo de tempo específico.
Filtro por Estados: Selecione os estados para a pesquisa.
Filtro por Palavras-Chave: Defina as palavras-chave para filtrar as licitações de interesse.
A aplicação consulta os últimos 500 editais, divididos em páginas de 50 editais por estado.

Contribuições:
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e novas funcionalidades.

Com esta aplicação, esperamos facilitar o trabalho dos profissionais que buscam oportunidades de negócios em licitações públicas, oferecendo uma solução automatizada e eficiente para a consulta e análise de pregões eletrônicos.
