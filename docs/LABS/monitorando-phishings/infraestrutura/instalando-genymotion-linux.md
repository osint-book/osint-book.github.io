# Genymotion
## O que é o Genymotion ?
O Genymotion é um projeto que tem como objetivo a emulação gratuita de sistemas operacionais Android.

Como ele podemos usar diversas versões, os respectivos aplicativos disponiveis e usar de forma virtualizada sem a necessacidade de ter diversos dispositivos fisicos.

## O que podemos fazer ?
Com o Genymotion podemos realizar diversas ações, por exemplo:
- Emular um dispositivo Android;
- Obter root no dispositivo;
- Realizar download do APK.

Neste laboratorio iremos:
- Criar o dispositivo Android para o laboratorio;

## Instalação
O Genymotion tem como pré-requisito a instalação do VirtualBox, dependendo da versão for realizado o download o mesmo já no instalador.

### Criando conta
1. Criação de Conta:
- https://www-v1.genymotion.com/account/create/

![](images/genymotion-create.png)
> Vou usar um email temporario https://10minutemail.com/

### Realizando download
2. Download:
- https://genymotion.com/download
![](images/genymotion-download.png)

### Documentação
3. Documentação
- https://docs.genymotion.com/desktop/latest/
![](images/genymotion-create-2.png)

Chegou o email. Nesse caso meu email é o gqvfauvcxsmlrvtdtu@pp7rvv.com.
![](images/genymotion-create-3.png)

Agora vamos escolher qual versão usar, vou usar gratuita por 30 dias e que tem o nome de **TRY FOR 30 DAYS**.
![](images/genymotion-create-4.png)

### Observações
Podemos usar online e pagamos por hora Android e IOS.
> IOS só na nuvem

> É recomendado o uso de um dispositivo fisico devido a estabilidade, velocidade e minimizar possiveis problemas.

### Comandos para instalação
Para instalar:
```sh
cd /tmp
wget -c https://dl.genymotion.com/releases/genymotion-3.2.1/genymotion-3.2.1-linux_x64.bin
chmod +x genymotion-3.2.1-linux_x64.bin
sudo ./genymotion-3.2.1-linux_x64.bin
```

Vamos criar um script com as informações acima e dar o nome de **install_genymotion.sh**.
![](images/genymotion-install-1.png)

Vamos dar permissão de execução usando **chmod**.
```sh
chmod +x install_genymotion.sh
```

Podemos ver o resultado.
![](images/genymotion-install-2.png)

1. Vamos realizar o login na conta.
![](images/genymotion-01.png)

> Caso não tenha feito conta pode ir até **CREATE ACCOUNT**. Vamos ser redirecionados.
> https://www-v1.genymotion.com/account/create/

2. Vamos setar **personal Use**.
![](images/genymotion-02.png)

3. Vamos aceitar a licença.
![](images/genymotion-03.png)

4. Essa é a pagina principal.
![](images/genymotion-04.png)

5. Vamos clicar no **+**, vamos setar o valor **Samsung Galaxy s9**. Vamos selecionar o **Samsung Galaxy** da sua escolha, em seguida vamos clicar em **Next**.
![](images/genymotion-05.png)

6. Agora vamos dar um nome para esse ambiente e clicar em **Install**.
![](images/genymotion-06.png)

7. Download está sendo realizado.
![](images/genymotion-07.png)

8. Após será realizado a criação do laboratorio.
![](images/genymotion-08.png)

> DICA
É recomendado que seja alterado para o local.
```sh
/opt/genymobile/genymotion/tools
```

9. Iniciando maquina podemos clicar com o botão direito em cima da maquina e clicar em **start** para iniciar.
![](images/genymotion-09.png)

> Por padrão a maquina  
> Caso tenha algum problema ou ja tenha usado a maquina clique **Reset Factory**.

10. A maquina vem com a configuração de rede NAT por padrão.
![](images/genymotion-10.png)

11. Podemos ver que nossa maquina com Android foi criada.
![](images/genymotion-11.png)
