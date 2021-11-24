# Materiais indexados na internet
Atualmente graças ao motores de busca conseguimos encontrar diversos sites na internet com muita facilidade, é possivel encontrar blogs que nos ajuda com noticias, sites de instituições, foruns para busca por informações e lojas virtuais.

## Motores de busca
Temos atualmente diversos sites que nos auxilia nessa busca, entre os principais estão:

- Google;

- Bing;

- yandex;

- Duck Duck Go;

- Entre outros.

> Nessa oficina vou focar apenas no Google, mas em breve vou disponibilizar um material completo com diversos motores e busca.

### Google Dorks
Para um melhor exito em nossas buscas podemos usar palavras especificas e operadores que nos auxilia.
> [Podemos ver mais sobre Google Hacking](https://github.com/ABase-BR/osint_garoa_aphack/tree/master/GoogleHacking)

#### Palavras chaves e Dorks
Eu recomendo sempre ser o maximo acertivo nas palavras usadas, vamos focar no nome da marca e o titulo da pagina oficial.

Quando encontramos uma pagina na internet um dos pontos que a grande maioria de paginas possui, são os titulos. Tambem conhecidos no HTML como **<title>Titulo da pagina</title>**.

Para realizar a busca por titulos podemos usar o operador:

- intitle
```sh
intitle:"Nome do titulo"
```

Para buscar por algo especifico podemos usar o operador **"nome"**, dessa forma é possivel buscar por uma frase especifica.

- "palavras chaves"

O operador site vai nos retornar resultados de um site especifico, por exemplo:
```sh
site:badbank.com.br
```

Já o operador **-** é negação, ele vai recursar qualquer resultado que esteja no **-site**.

- Operador -site

Agora podemos somar informações do tituto de uma pagina oficial, negando o site verdadeira e assim analisando os resultados em busca de paginas suspeitas.
```sh
intitle:"Nome do titulo" "badbank" -site:badbank.com.br
```

Para finalizar podemos usar informações de uma url especifica, por exemplo:
- badbank.com.br/novos-clientes-badbank
```sh
inurl:novos-clientes-badbank
```
