#! /bin/bash
#
#  Gerenciador do projeto
#
#  Steps:
#
#   1  Configurar as variaveis de ambiente PROJECT_NAME e PROJECT_HOME para o respectivo projeto
#   
#   2. Incluir no .bashrc esse script.
#       source <path_tools>/<nome_do_script>.sh e
#       A variavel OPT_MANGE com as opções para o projeto
#
#   3. Conectar o webserver e o computador utilizado para o desenvolvimento em uma mesma rede com acesso a internet
#   4. Acesso ao host
#   5. No diretorio rais do projeto existe um arquivo <nome_do_projeto.conf>


### Definições e parametros do projeto

# nome do projeto
export OPCUA_PROJECT_NAME=industry40

# Local do projeto (obs declarado no .bashrc)
#export  WORKDIR=

# arquivo de configuração do projeto defualt = WORKDIR/PROJECTNAME.conf
# export OPCUA_CONF=

### Alias para os scripts

prj_name_lower=$(echo ${OPCUA_PROJECT_NAME,,})
alias opcua-manage=$OPCUA_PROJECT_HOME/manage.py

### alias aplicação

alias $prj_name_lower="opcua-manage"