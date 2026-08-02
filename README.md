# AveDex

Catálogo interativo de aves desenvolvido na disciplina de Boas Práticas de Programação do curso de Análise e Desenvolvimento de Sistemas.

## Funcionalidades

- Menu interativo
- Listagem das aves cadastradas
- Busca de aves por ID
- Busca textual por:
  - Nome popular
  - Nome científico
  - Família
  - Ordem
  - Tipo de dieta
- Busca ignorando diferenças entre letras maiúsculas, minúsculas e acentos
- Exibição detalhada das informações de cada ave
- Tratamento de entradas inválidas
- Exibição da quantidade de resultados encontrados

## Catálogo

Atualmente o sistema possui 9 aves cadastradas:

- Bem-te-vi
- Canário-da-terra
- João-de-barro
- Sabiá-laranjeira
- Tucano-toco
- Arara-azul
- Coruja-buraqueira
- Beija-flor-tesoura
- Garça-branca-grande

## Tecnologias utilizadas

- Python 3
- Biblioteca `unicodedata`

## Como executar

```bash
python avedex.py
```

## Estrutura do projeto

O projeto foi organizado utilizando funções específicas para cada responsabilidade, como:

- listagem de aves;
- busca por ID;
- busca textual;
- exibição dos resultados;
- exibição dos detalhes da ave;
- controle do menu principal.

Essa organização facilita a manutenção e futuras melhorias.

## Testes manuais realizados

- [x] Listagem das aves
- [x] Busca por parte do nome popular
- [x] Busca ignorando acentos
- [x] Busca por nome científico
- [x] Busca por família
- [x] Busca por ordem
- [x] Busca por dieta
- [x] Busca sem resultados
- [x] Busca com entrada vazia
- [x] Seleção de ave por ID existente
- [x] Seleção de ave por ID inexistente
- [x] Tentativa de abrir ID fora dos resultados
- [x] Tratamento de opção inválida
- [x] Encerramento do programa

## Exemplos de buscas

| Busca | Resultado esperado |
|-------|--------------------|
| barro | João-de-barro |
| canario | Canário-da-terra |
| tyrannidae | Bem-te-vi |
| passeriformes | Todas as aves dessa ordem |
| granivora | Canário-da-terra e Arara-azul |
| trochilidae | Beija-flor-tesoura |
| ardeidae | Garça-branca-grande |

## Fontes dos dados

- https://www.wikiaves.com.br