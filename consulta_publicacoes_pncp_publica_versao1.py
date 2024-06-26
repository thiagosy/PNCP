#!/usr/bin/env python
# coding: utf-8

# ## APLICAÇÃO PARA CONSULTAR LICITAÇÕES PUBLICADAS NO PNCP (versão1)
# ### Faz a busca de todos os pregões eletrônicos por estado e data de publicação;
# #### Filtra as licitações cujo objeto possui alguma/algumas das palavras definidas e salva tudo em Excel, tanto a pesquisa geral quanto a filtrada por palavra chave. ***A aplicação consulta os últimos 500 editais, divididos em páginas de 50 editais por estado.***
# 
# ###### Como usar:
#         1. Ajuste de data (intervalo de tempo para pesquisa); 
#         2. Defina as UFs; 
#         3. Defina as palvras-chave (palavras_chave);
#         4. Se necessário, mude o código da modalidade (padrão 6: pregão eletrônico);

# ### Dados do Portal Nacional de Compras Públicas (PNCP):
# * **A Nova Lei de Licitações 14.133/2021 exige que todos os órgãos da administração pública centralizem as informações de suas contratações em um portal nacional. Com acesso a esse portal através da API, nossa aplicação busca oportunidades de negócios verificando as licitações publicadas.** O processo envolve:
# 
# ### Contribuições:
# * Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e novas funcionalidades.
# 
# ***Com esta aplicação, esperamos facilitar o trabalho dos profissionais que buscam oportunidades de negócios em licitações públicas, oferecendo uma solução automatizada e eficiente para a consulta e análise de pregões eletrônicos.***

# In[2]:


# importando os módulos 
import pandas as pd
import requests
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns


# In[3]:


# parâmetros - pesquisa por data de publicação 

data_inicial = 20240625
data_final = 20240626
codigo_modalidade = 6 # pregão eletrônico
codigo_municipio_ibge = '' 
cnpj = ''  
codigo_unidade_administrativa = '' 
tamanho_pagina = 50


# In[4]:


# URL para pesquisa de processos publicados - somente com os parâmetros obrigatórios:
# páginas 1 A[a] 10

base_url = 'https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao'
tamanho_pagina = 50  # Defina o tamanho da página conforme necessário
urls = []

for pagina in range(1, 11):  
    for uf in ['PE', 'PB', 'AL', 'SE', 'BA', 'RN', 'CE']:  
        url = f'{base_url}?dataInicial={data_inicial}&dataFinal={data_final}&codigoModalidadeContratacao={codigo_modalidade}&uf={uf}&tamanhoPagina={tamanho_pagina}&pagina={pagina}'
        urls.append(url)


# # requisitando 
# 
# response1 = requests.get(url_padrao1)
# response2 = requests.get(url_padrao2)
# response3 = requests.get(url_padrao3)
# response4 = requests.get(url_padrao4)
# response5 = requests.get(url_padrao5)
# response6 = requests.get(url_padrao6)

# In[ ]:


# requisitando e criando o DF com os dados
# Lista para armazenar todos os processos
processos = []

# Iterar sobre as URLs e realizar as requisições
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        dados_dict = response.json()['data']  # Assumindo que 'data' contém os processos
        
        # Iterar sobre os processos retornados
        for processo in dados_dict:
            sequencial = processo['sequencialCompra']
            orgao = processo['orgaoEntidade']['razaoSocial']
            uf = processo['unidadeOrgao']['ufSigla']
            inclusao = processo['dataInclusao']
            amparo_legal = processo['amparoLegal']['descricao']
            abertura = processo['dataAberturaProposta']
            encerramento = processo['dataEncerramentoProposta']
            n_processo = processo['processo']
            objeto = processo['objetoCompra']
            link = processo['linkSistemaOrigem']
            valor_estimado = processo['valorTotalEstimado']
            valor_homologado = processo['valorTotalHomologado']
            disputa = processo['modoDisputaNome']
            plataforma = processo['usuarioNome']
            situacao = processo['situacaoCompraNome']
            srp = processo['srp']
            
            # Adicionar os dados formatados à lista de processos
            processos.append([
                sequencial, orgao, uf, inclusao, amparo_legal, abertura, encerramento, n_processo, objeto, link,
                valor_estimado, valor_homologado, disputa, plataforma, situacao, srp
            ])
    #else:
        print(f"Erro na requisição para {url}: {response.status_code} - {response.text}")

# Criar o DataFrame
df = pd.DataFrame(processos, columns=[
    'sequencial', 'orgao', 'uf', 'inclusao', 'amparo_legal', 'abertura', 'encerramento', 'n_processo', 'objeto', 'link',
    'valor_estimado', 'valor_homologado', 'disputa', 'plataforma', 'situacao', 'srp'
])


# In[ ]:


print(dados_dict)


# In[ ]:


pd.set_option('display.max_rows', None)  

df.head(1) 
df.shape


# In[ ]:


# organizando os dados

df['valor_estimado'] = pd.to_numeric(df['valor_estimado'], errors='coerce')

# data formatada

df['abertura'] = pd.to_datetime(df['abertura'], format='%Y-%m-%dT%H:%M:%S')
df['inclusao'] = pd.to_datetime(df['inclusao'], format='%Y-%m-%dT%H:%M:%S')
df['encerramento'] = pd.to_datetime(df['encerramento'], format='%Y-%m-%dT%H:%M:%S')


# In[ ]:


# filtrando pelas palavras de interesse 

palavras_chave = [
    'alimentício', 'alimento'
]

palavras_chave = [palavra.lower() for palavra in palavras_chave]

filtro = df['objeto'].str.lower().str.contains('|'.join(palavras_chave), na=False)

df_filtrado = df[filtro].reset_index()


# In[ ]:


df_filtrado[['objeto']]


# In[ ]:


df_filtrado[['link']]


# ### Estrutura do Arquivo Excel:
# * Pesquisa Geral: Contém todas as licitações encontradas na busca.
# * Pesquisa Filtrada: Apresenta as licitações filtradas por palavras-chave.

# In[ ]:


# salvar o arquivo no excel 

data_atual = datetime.now().strftime('%d_%m_%Y')

nome_arquivo_excel = f'licitacoes_{data_atual}.xlsx'

with pd.ExcelWriter(nome_arquivo_excel) as writer:
    df.to_excel(writer, sheet_name='Todos', index=False)

    df_filtrado.to_excel(writer, sheet_name='Filtrados', index=False)

print(f'DataFrame salvo com sucesso em {nome_arquivo_excel}')

