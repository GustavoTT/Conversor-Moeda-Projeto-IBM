# Conversor de Moedas - Projeto Acadêmico
> Projeto desenvolvido em grupo com fins acadêmicos, desenvolvido perante demanda para conclusão da Trilha de Desenvolvimento Web, parceria entre o programa Match e a IBM.

## Informações do projeto
Foi solicitado um projeto final para conclusão do 2° módulo da Trilha de Desenvolvimento Web (parceria entre o programa Match e a IBM), dentre as opções de projetos, escolhemos o "Projeto 4: Conversor de Moedas com Validação de Dados".
Diante disso, desenvolvemos em Python uma aplicação que:
- Recebe os dados referente a conversão solicitada pelo usuário
- Se conecta com uma API (Awesome API) que fornecerá os dados de cotação
- Realiza a conversão com base nos dados previamente coletados
- Retorna ao usuário o resultado do cálculo, ou, em caso de erro, retorna um aviso

## Funcionamento ⚙️
Optamos por utilizar a API de cotações da AwesomeAPI (https://docs.awesomeapi.com.br/api-de-moedas). 
Utilizamos as rotas: 
- Retorna a ultima ocorrência das moedas solicitadas, através da rota (Ex.: https://economia.awesomeapi.com.br/last/USD-BRL), utilizamos dos atributos 'name' e 'bid'.
- Para captação das moedas fornecidas pela API, utilizamos da rota (https://economia.awesomeapi.com.br/xml/available/uniq) juntamente com inteligência artificial, para tratar e retirar do formato xml somente as abreviações das moedas.

## Observações 🛈
### 1° - Limitações de funcionamento
A aplicação é limitada perante os dados disponibilizados pela API, no momento em que a API não fornece as cotações das moedas solicitadas pelo usuário, a aplicação entende e retorna um aviso, cabendo ao usuário alterar as moedas de interesse.
### 2° - Requisições para o funcionamento
Para o perfeito funcionamento do conversor, em caso de utilizar o código fonte, atente-se às bibliotecas necessárias e ao arquivo 'uniq.xml' que também deve ser importado para o funcionamento, nesse caso, não é necessário o arquivo executável (main.exe).
### 3° - ⚠️ Arquivo executável ⚠️
Para melhor acessibilade, geramos um arquivo executável do projeto. Podendo ser utilizado sem a necessidade de ter o Python instalado em seu computador. 👉 PORÉM, para seu funcionamento, é necessário que o arquivo 'uniq.xml' esteja no mesmo local que o executável,
assim, ele funcionará sem erros. Ao executar, pode ser que o antivírus do seu computador bloqueie o funcionamento do arquivo. ⚠️ Não recomendamos a utilização do executável em ambientes mobile ⚠️.

## Grupo 🧑🧑👩👩👩👩
- Gustavo Teles
