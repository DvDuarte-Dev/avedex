# AveDex

Catálogo interativo de aves desenvolvido na disciplina de Boas Práticas de Programação do curso de Análise e Desenvolvimento de Sistemas.

## Funcionalidades

- Menu interativo
- Listagem das aves cadastradas
- Busca de aves por:
  - Nome popular
  - Nome científico
  - Família
  - Ordem
  - Dieta
- Visualização dos detalhes de uma ave
- Comparação entre duas aves
- Validação do dataset
- Tratamento de erros no carregamento do JSON
- Verificação das dependências do ambiente

## Dependências

As dependências opcionais estão listadas em `requirements.txt`.

Para instalar:

```bash
pip install -r requirements.txt

## Catálogo

Atualmente o sistema possui 9 aves cadastradas:

- Bem-te-vi
- João-de-barro
- Canário-da-terra
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

## Testes defensivos realizados
- [x] JSON carregado corretamente
- [x] Arquivo JSON ausente
- [x] JSON mal formatado
- [x] Campo obrigatório ausente
- [x] ID duplicado
- [x] Campo numérico inválido
- [x] Entrada inválida no ID
- [x] Verificação de ambiente

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