# Instalando Virtualbox Linux
Eu gosto muito do Debian, diferente de outros sistemas operacionais como o Ubuntu, o Debian vem com poucos softwares instalados e sem softwares proprietarios inclusos.

Alem disso tem uma grande comunidade por tras e com diversos projetos que dão suporte para quem está iniciando.

> Por exemplo:
- https://servidordebian.org/pt/start

> Atenção: Fique a vontade para usar o Linux que se sentir mais a vontade, mas não esqueça de saber o nome e a versão usada.

## O que é o Virtualbox
O Virtualbox é um ótimo produto para nos auxiliar na virtualização e é disponível para X86 e AMD64/Intel64.

Podemos usar ele em uso domestico ou corporativo.

Além de ser um ótimo produto, ele também é a única solução profissional disponível gratuitamente como Software Open Source sob os termos GNU(General Public Licence) Versão 2.

## Disponível em varios hosts
Podemos usar o Virtualbox em diversos hosts, sejam eles:
- Windows
- Linux
- Macintosh
- Solaris

Além de suportar lista gigante de sistemas operacionais convidados, veja um pouco

### Windows
- NT 4.0
- 2000
- XP
- Server 2003
- Vista
- Windows 7
- Windows 8
- Windows 10
- DOS
- Windows 3.x

### Linux
- Debian
- Ubuntu
- Mint
- CentOS
- Arch Linux
- 2.4
- 2.6
- 3.x
- 4.x

### Outras opções
- Solaris
- OpenSolaris
- OpenBSD

## Comunidade e Oracle
Além de novas versões ele sempre tem novas funcionalidades, novos recursos, novos sistemas operacionais convidados e plataformas onde ele é executado.

Atualmente o Virtualbox disponibiliza novas versões com uma certa frequência, tudo isso graças a sua comunidade que é incentivada a contribuir, já a Oracle é a empresa responsável por trás do Virtualbox e ajuda a manter sempre os critérios de qualidade.

## Instalando Virtualbox - DPKG
> Site oficial: https://www.virtualbox.org/

> Link download: https://www.virtualbox.org/wiki/Downloads

### Antes de começar
Nos exemplos eu vou usar o sistema operacional Debian.

Para acompanhar você precisa estar usando um sistema baseado no Debian

### Obtendo o Virtualbox
Vamos para o link.
```sh
 https://www.virtualbox.org/wiki/Linux_Downloads
```

Nesse caso vou usar o Debian bullseye 64 Bits.
```sh
http://download.virtualbox.org/virtualbox/6.1.28/virtualbox-6.1_6.1.28-147628~Debian~buster_amd64.deb
```

### Buscando por outras versões
Caso queira usar uma outra versão antiga podemos usar também o seguinte link
```sh
https://download.virtualbox.org/virtualbox/
```

### Iniciando a instalação
Nesse exemplo estou no diretório
```sh
 /home/greenmind/Downloads
```

Para instalar preciso fazer
```sh
sudo dpkg -i virtualbox-6.1_6.1.28-147628~Debian~bullseye_amd64.deb
```

Após isso o Virtualbox vai estar instalado
```sh
Menu de aplicativos -> Sistema -> Oracle VM VirtualBox
```

## Instalando extension pack
Podemos realizar o download do extension pack no link abaixo.
> https://www.virtualbox.org/wiki/Downloads

A versão atual é a **6.1.28**.
> https://download.virtualbox.org/virtualbox/6.1.28/Oracle_VM_VirtualBox_Extension_Pack-6.1.28.vbox-extpack

Não esqueça de usar o extension pack na mesma versão do virtualbox.
```sh
./Oracle_VM_VirtualBox_Extension_Pack-6.1.28.vbox-extpack
```

## Referencias
- [Linux Donwload](https://www.virtualbox.org/wiki/Linux_Downloads)

- [Old Builds](https://www.virtualbox.org/wiki/Download_Old_Builds)

- [Oracle VirtualBox](https://www.virtualbox.org/wiki/) - 28-08-2018-15:07
