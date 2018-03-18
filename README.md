# Industry4.0

Utilização do padrão OPC-UA para abstração de um processo fabril

1. Instalar python 3.X

2. Instalar  gerenciador de pacotes python (pip)

3. Clonar o reposiiório do projeto

Dentro do diretório executar o comando

```shell    
git clone https://github.com/JeffeApAlves/industry4.0.git
```

4. Exportar a váriavel (OPCUA_PROJECT_HOME) indicando o home do projeto (onde foi feito o clone) Para isso adicionar a linha abaixo no arquivo .bashrc.

``` shell
export OPCUA_PROJECT_HOME=$WORK_SPACE/industry40
```

5. Carregar o script do projeto onde ficarão algumas definições , alias etc. Para isso adicionar a linha abaixo no arquivo .bashrc.

``` shell
$ source $OPCUA_PROJECT_HOME/tools/opcua.sh
```

6. Criar um ambiente virtual python (opcua)

Seguir esse [Tutorial](https://jeffeapalves.github.io/edocs/python_enviroment.html)

7. Instalar dependencias do projeto

```shell    
pip install -r reqirements.txt
```

8. Cirar um usuário de sistema (opcua)

9. Executando o help (em contrução)

``` shell
$ opcua-manage --help
```

10. Para adicionar novos tipos

* Editar o arquivo ./industry40.conf adicionando o novo tipo

* Mapear , na classe generalista (uaTXXX),  uma constante do string com o nome que foi usado no arquivo .conf

* Implemetar a classe (uaTXXX) que descreve/cria o novo tipo o servidor opcua. Metodos: 'create_methods' ,'create_propert', 'create' , 'create_methods' 

* Implemetar a classe que será aentidade do novo tipo uaXXX   metodos: 'create' e outros especifico ao que cada uma representa

11. Para criar novos objetos editar o arquivo ./config/objects.conf

12. Executar o ambiente python

``` shell
$ workon opcua
```
13. Executando o server

``` shell
$ opcua-manage server
```

14. Executando um device do tipo robo de nome Robot1

``` shell
$ opcua-manage device --type robot --name Robot1 --idx 1
```

15. Fazendo deploy e outras maquinas

Configurar o ip e o diretorio de trabalho respectivo do device ou server no arquivo ./config/objects.conf campo deploy e executar o comando

``` shell
$ opcua-manage deploy
```
