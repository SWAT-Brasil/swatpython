## SWATPython

Interface python para SWAT. Funcões para controle e automação do SWAT com python. 

Em desenvolvimento, não é recomendado o uso. 

Desenvolvido em PyCharm Community Edition

## Objetivo
Um interface de facil uso para automatizar processamento das variaveis de entrada e 
saida do SWAT.

## Utilização
Veja arquivo de exemplo swat_exemple.py. Projeto desenvolvido na ide pycharm.

## Estrutura
A interface funciona baseada em módulos. Cada módulo é para uma versão específica do 
SWAT, e conta com as rotinas para processamento dos dados no formato especifico da 
versão, e os executavies SWAT para Linux e Windows quando disponíveis. 
Não é garantido a disponibilidade para os dois sistema operacionais.

Quando a interface é inicializada, o usuario informa a versão do SWAT a ser 
utilizada, o sistema operacional é detectado automaticamente. 
O módulo é carregado automaticamente a partir da versão informada, 
e o executavel correto é carrregado.

## Problemas conhecidos
- Aparentemente o código compilado com GFrotran não funciona corretamente, ele falha já na hora de
ler os arquivos de dados. Não foi possível fazer o swat funcionar com nenhuma compilação feita com 
GFortran. O SWAT é originalmente compilado com intel fortran.
- O arquivo *Tmp1.Tmp* vem sempre com as letras maiúsculas do Windows, mas não funciona no linux,
precisa renomear para *tmp1.tmp* para funcionar no Linux. Renomear o arquivo não deve
impedir o funcionamento no windows, pois isso não faz diferença no windows.


# TODO
- Visualização de shapes
- Unidade de teste
- Gerador de documentação
- Leitura e escrita de arquivos importantes 
- A versão swat2012rev637 para linux não esta funcionando. Encontrar uma versão q funcione 

