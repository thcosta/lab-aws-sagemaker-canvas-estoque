# 📊 Previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

Bem-vindo ao desafio de projeto "Previsão de Estoque Inteligente na AWS com SageMaker Canvas. Neste Lab DIO, você aprenderá a usar o SageMaker Canvas para criar previsões de estoque baseadas em Machine Learning (ML). Siga os passos abaixo para completar o desafio!

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter uma conta na AWS. Se precisar de ajuda para criar sua conta, confira nosso repositório [AWS Cloud Quickstart](https://github.com/digitalinnovationone/aws-cloud-quickstart).


## 🎯 Objetivos Deste Desafio de Projeto (Lab)

![image](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque/assets/730492/72f5c21f-5562-491e-aa42-2885a3184650)

- Dê um fork neste projeto e reescreva este `README.md`. Sinta-se à vontade para detalhar todo o processo de criação do seu Modelo de ML para uma "Previsão de Estoque Inteligente".
- Para isso, siga o [passo a passo] descrito a seguir e evolua as suas habilidades em ML no-code com o Amazon SageMaker Canvas.
- Ao concluir, envie a URL do seu repositório com a solução na plataforma da DIO.


## 🚀 Passo a Passo

### 1. Selecionar Dataset

-   Navegue até a pasta `datasets` deste repositório. Esta pasta contém os datasets que você poderá escolher para treinar e testar seu modelo de ML. Sinta-se à vontade para gerar/enriquecer seus próprios datasets, quanto mais você se engajar, mais relevante esse projeto será em seu portfólio.
-   Escolha o dataset que você usará para treinar seu modelo de previsão de estoque.
-   Faça o upload do dataset no SageMaker Canvas.

### 2. Construir/Treinar

-   No SageMaker Canvas, importe o dataset que você selecionou.
-   Configure as variáveis de entrada e saída de acordo com os dados.
-   Inicie o treinamento do modelo. Isso pode levar algum tempo, dependendo do tamanho do dataset.

### 3. Analisar

-   Após o treinamento, examine as métricas de performance do modelo.
-   Verifique as principais características que influenciam as previsões.
-   Faça ajustes no modelo se necessário e re-treine até obter um desempenho satisfatório.

### 4. Prever

-   Use o modelo treinado para fazer previsões de estoque.
-   Exporte os resultados e analise as previsões geradas.
-   Documente suas conclusões e qualquer insight obtido a partir das previsões.

## 🤔 Dúvidas?

Esperamos que esta experiência tenha sido enriquecedora e que você tenha aprendido mais sobre Machine Learning aplicado a problemas reais. Se tiver alguma dúvida, não hesite em abrir uma issue neste repositório ou entrar em contato com a equipe da DIO.

## 📈 Resultado do Desafio

### Geração dos dados

Para gerar os dados do controle de estoque foi criado um script em Python. O script permite gerar o estoque dos Para rodar o script devem ser seguidos os seguintes passos:
1. Rodar o comando:
```shell
$ python3 stock_generator.py
```
2. No console, prencher as informações de **filename**, **start date**, **end date**, **first product ID**, **last product ID**;
3. Será gerado o arquivo CSV com as colunas **PRODUCT_ID**, **DATE**, **PRICE**, **QUANTITY**.

### Treinamento do Modelo

O modelo foi treinado com o arquivo **stock.csv** no AWS SageMaker Canvas utilizando a coluna **PRODUCT_ID** como a coluna correspondente ao **Item ID**, a coluna **DATE** foi utilizada como a coluna com a informação do **Timestamp** e a coluna **QUANTITY** foi escolida como a coluna do **Target**.

Não foi realizado nenhum tratamento nos dados já que não haviam dados nulos ou *outlayers*.

No treinamento do modelo foi utilizado  **Standard Build** e a duração do treinamento foi de 2h47min.

### Análise

Da análise do treinamento do modelo foram geradas as seguintes métricas:
* **Average Weighted Quantile Loss (Avg. wQL)**: mede a precisão média do modelo nos quantis P10, P50 e P90;
* **Mean Absolute Percentage Error (MAPE)**: mede a média do valor absoluto do erro percentual entre os valores observados e previstos para cada unidade de tempo;
* **Weighted Absolute Percentage Error (WAPE)**: mede o desvio geral dos valores previstos a partir dos valores observados;
* **Root Mean Square Error (RMSE)**: mede a raiz quadrada da média dos erros quadrados; 
* **Mean Absolute Scaled Error (MASE)**: mede o o erro médio por um fator de escalabilidade.

Os valores das métricas obtidas durante o treinamento foram:
* **Average Weighted Quantile Loss (Avg. wQL)**: 0.163;
* **Mean Absolute Percentage Error (MAPE)**: 1.167;
* **Weighted Absolute Percentage Error (WAPE)**: 0.255;
* **Root Mean Square Error (RMSE)**: 22.716; 
* **Mean Absolute Scaled Error (MASE)**: 1.028.

Foi verificada que a coluna **PRICE** contribui negativamente para a acurácia do modelo (-100%). Assim, em um novo treinamento essa coluna deveria ser ignoradas para que a previsão do estoque seja mais precisa.

### Predição

Foi realizada a predição da quantidade dos produtos com identificador **1**, **5**, **10**, **15**, **20** em estoque para o período de 01/01/2024 a 10/01/2024.
Os resultados da predição foram adicionados na pasta **predictions**.