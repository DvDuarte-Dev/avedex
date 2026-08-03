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
- Comparação entre duas aves
- Comparação de:
  - Nome científico
  - Família
  - Ordem
  - Tipo de dieta
  - Habitat
  - Comprimento
  - Peso
  - Status de conservação
- Corte automático de textos longos na comparação
- Indicação de qual ave é mais pesada
- Tratamento de valores indisponíveis
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

O projeto foi organizado utilizando funções específicas para cada responsabilidade:

- listagem de aves;
- busca por ID;
- busca textual;
- comparação entre aves;
- exibição dos resultados;
- exibição dos detalhes da ave;
- controle do menu principal;
- funções auxiliares para comparação;
- constantes para configuração da aplicação.

A organização do código facilita a manutenção, reduz repetições e prepara o projeto para futura separação em módulos.

## Testes de regressão

- [x] Listar aves
- [x] Buscar por parte do nome
- [x] Buscar por família
- [x] Buscar por ordem
- [x] Buscar por dieta
- [x] Ver detalhes por ID
- [x] Comparar duas aves
- [x] Tratar ID inexistente
- [x] Tratar opção inválida no menu
- [x] Encerrar o programa

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
- [x] Comparação entre duas aves
- [x] Comparação da mesma ave
- [x] Comparação com ID inexistente
- [x] Exibição da ave mais pesada
- [x] Tratamento de textos longos na comparação
- [x] Tratamento de opção inválida
- [x] Encerramento do programa

## Exemplos de buscas

| Busca | Resultado esperado |
|-------|--------------------|
| barro | João-de-barro |
| canario | Canário-da-terra |
| tyrannidae | Bem-te-vi |
| passeriformes | Todas as aves da ordem Passeriformes |
| granivora | Canário-da-terra e Arara-azul |
| trochilidae | Beija-flor-tesoura |
| ardeidae | Garça-branca-grande |

## Comparação entre aves

O sistema permite selecionar duas aves do catálogo e comparar lado a lado:

- Nome científico
- Família
- Ordem
- Tipo de dieta
- Habitat
- Comprimento
- Peso
- Status de conservação

Durante a comparação, habitats muito longos são abreviados automaticamente para manter a tabela organizada. Ao final, o programa informa qual das aves é mais pesada.

## Fontes dos dados

- https://www.wikiaves.com.br