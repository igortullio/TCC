# TCC
## Objetivo Geral
Desenvolver um aplicativo para smartphone simples, que possa conversar com um
dispositivo eletrônico no futuro, usando um ambiente de desenvolvimento em Python
## Autores e Principais Contribuidores
* [Caio Leandro](https://github.com/Caio820) (Construção da estrutura da aplicação)
* [Pedro Paul](https://github.com/ppaul804) (Construção da estilização e dos protótipos da aplicação)
* [Igor Túllio](https://github.com/igortullio) (Construção do bando de dados e integração com a aplicação)
# Sobre a aplicação
## Instalação
Segue a seguir a lista dos passos necessários para instalar as ferramentas necessárias para a execução da aplicação:
### Windows
1. Faça download do [Git](https://git-scm.com/download/win) e o instale.
2. Faça download do [Python](https://www.python.org/downloads/windows/) e o instale.
3. Abra o prompt de comando do Windows apertando `Win`+`r`.
Para testar se o Git e o Python foram instalados corretamente execute ``git version`` e ``python --version`` respectivamente.
4. Atualize o `pip` e o `wheel` 
```bat
python -m pip install --upgrade pip wheel setuptools
```
Obs.: Caso o comando `python` não funcione, tente mudá-lo para `py`.

5. Instale as depedências do Kivy
```bat
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
```

6. Instale o Kivy
```bat
python -m pip install kivy
```
### Linux
0. Abra o terminal do linux
1. Instale o Git
```sh
sudo apt-get install git
```
2. O Python já vem instalado em algumas distribuições linux, porém, caso ele não esteja instalado, instale-o.
```sh
sudo apt-get install python3
```
Obs.: Troque o ``python3`` para ``python`` para a versão Python2

3. Adicione o PPAs (Personal Package Archives) do Kivy estável
```sh
sudo add-apt-repository ppa:kivy-team/kivy
```
4. Atualize sua lista de pacotes usando seu gerenciador de pacotes
```sh
sudo apt-get update
```

5. Instale o Kivy
```sh
sudo apt-get install python3-kivy
```
Obs.: Troque o ``python3-kivy`` para ``python-kivy`` para a versão do Kivy para Python2

## Execução
Segue a seguir as listas dos passos necessários para executar a aplicação:
1. Faça o clone deste projeto
```git
git clone https://github.com/igortullio/tcc.git
```
2. Execute o arquivo ``main.py``
```git
python main.py
```
## Restrições

## Referências
* [Python](https://www.python.org/)
* [Kivy](https://kivy.org/)
