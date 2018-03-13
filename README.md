# Industry4.0

Utilização do padrão OPC-UA para abstração de um processo fabril

1. Instalar python 3.X

2. Instalar  gerenciador de pacotes python (pip)

3. Clonar o reposiiório do projeto

Dentro do diretório executar o comando

```shell    
git clone https://github.com/JeffeApAlves/industry4.0.git
```

4. Instalar dependencias do projeto

```shell    
pip install reqirements.txt
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

7. Cirar um usuário de sistema (opcua)

8. Executando o help (em contrução)

``` shell
$ opcua-manage --help
```

9. Para adicionar novos tipos

* Editar o arquivo ./industry40.conf adicionando o novo tipo

* Adicionar , na classe generalista (uaTXXX),  uma constante com o nome que foi usado no arquivo conf

* Implemetar as classes do novo tipo uaTXXX  (create) e uaXXX (create) (create_methods,create_pro,create)

10. Para criar novos objetos editar o arquivo ./config/objects.conf

11. Executar o ambiente python

``` shell
$ workon opcua
```
11. Executando o server

``` shell
$ opcua-manage server
```

12. Executando um device do tipo robo de nome Robot1

``` shell
$ opcua-manage device --type robot --name Robot1 --idx 1
```

13. Fazendo deploy e outras maquinas

Configurar o ip e o diretorio de trabalho respectivo do device ou server no arquivo ./config/objects.conf campo deploy e executar o comando

``` shell
$ opcua-manage deploy
```
