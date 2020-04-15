## SWATPython

Interface python para SWAT. Funcões para controle e automação do SWAT com python. 

Em desenvolvimento, não é recomendado o uso. 

Desenvolvido em PyCharm Community Edition

## Objetivo
Um interface de facil uso para automatizar processamento das variaveis de entrada e 
saida do SWAT.

## Utilização
Veja arquivo de exemplo swat_exemple.py. Projeto desenvolvido na ide pycharm TODO: 
fazer um exemplo rapido de uso aqui

## Estrutura
A interface funciona baseada em módulos. Cada módulo é para uma versão específica do 
SWAT, e conta com as rotinas para processamento dos dados no formato especifico da 
versão, e os executavies SWAT para Linux e Windows quando disponíveis. 
Não é garantido a disponibilidade para os dois sistema operacionais.

Quando a interface é inicializada, o usuario informa a versão do SWAT a ser 
utilizada, o sistema operacional é detectado automaticamente. 
O módulo é carregado automaticamente a partir da versão informada, 
e o executavel correto é carrregado.

# TODO
- Visualização de shapes
- Unidade de teste
-  Gerador de documentação
- Execução assincrona do SWAT
- Leitura e escrita de arquivos importantes 

