---
created: 2023-12-30 08:35:00
modified:
title: Tecnologias Descentralizadas
---

# Resumo da P1 de Blockchain e Tecnologias Descentralizadas

**Resumo P1 Blockchain**

[**Aula 2A - Serviços de Segurança 2**](#_il20pgkubrmz)

[Serviços básicos de segurança 2](#_rxsnq0iuzwhr)

[Ataques aos serviços 2](#_q3a7zfhjg8ar)

[**Aula 2D - Certificação digital e Certificação de Tempo 2**](#_44irznudrg2k)

[Certificados Digitais 2](#_tnb4eq24bdp2)

[Modelo PKI 2](#_nhc9j2cd7oc)

[Tipos de certificados 2](#_jix4ekbf1pyh)

[Processo de certificação 2](#_jnug4cqbrzgq)

[Processo de carimbo de tempo 2](#_6ig33ybg8f9o)

[Descentralizando autoridades 2](#_1fxdmne0vomf)

[**Aula 2E - Construções Avançadas com hashes 2**](#_m1i1c6wrny)

[Relembrando 2](#_tfl3zgnuk2jm)

[Comprometimento 2](#_itzjb9ipwuhk)

[Usos 3](#_29ycj788ain)

[**Aula 3A - Motivação para Blockchains 3**](#_sbkngk7devd2)

[Ordenação de Eventos 3](#_miesw1evze33)

[Blockchain = ACT distribuído 3](#_rs2pekosrmkh)

[**Aula 3B - Blockchain sem o hype - Funcionamento 3**](#_p7fniobqal2a)

[Bitcoin 3](#_9shgmzl7r9lf)

[Blockchain: Processando Eventos 3](#_7pd6u2wgamkw)

[Blockchain: Encadeando Eventos 3](#_nrwi49czhr0f)

[Blockchain: Consenso 3](#_sdfwvf86i6ux)

[Blockchain: Módulos 3](#_6e8kmq89ps4d)

[**Aula 3C - Logs Transparentes 4**](#_mnskhyqcmxb5)

[Log Transparente 4](#_kui99qyp0lki)

[Transparência de Certificados 4](#_2hc7cymxmpxe)

[Log Transparente: Registro de ativos 4](#_ryh9p1fk4ld8)

[**Aula 3D - Lendas (?) sobre Blockchains 5**](#_hgus119ose7v)

["Imutabilidade" 5](#_tdlrk3qwliez)

["Irretratabilidade" 5](#_8vigw4ogtar4)

["Veracidade" 5](#_dtj96r3gat0s)

["Depósito de dados" 5](#_eyomgxqbaytt)

["O" Blockchain 5](#_y1vmoy4vn4km)

["Aberto e anônimo" 5](#_47cpcz94n2i0)

["Leve e eficiente" 5](#_5u1ewowf7loa)

["Pesado" 5](#_7d12if97q1ia)

[Bitcoin leve? 5](#_8jxdflb6l48e)

[**Aula 3E - Aplicações de Blockchains 5**](#_y3ms8w5i0m7z)

[Blockchain: Quando usar? 5](#_vj1b1muc0e8u)

[Como criar soluções 5](#_5vcuet5oislq)

[Blockchain: Pagamentos 6](#_lxzm41yhtru8)

[Blockchain: outros ativos 6](#_qubyz9fitqtc)

[**Aula 3F - Aplicações Questionáveis com Blockchains 6**](#_ma5yraexhwu0)

[Blockchain: Aplicações Revolucionárias (?) 6](#_mh3sw15fkt8v)

[**Aula 3G - Privacidade em Blockchains 7**](#_7p6d0yirzacp)

[O que esconder? 7](#_tb70d05bjsas)

[Por que esconder? 7](#_xziou7rp35e9)

[Graus de anonimato 7](#_q3azwnptha4a)

[Privacidade em pagamentos 8](#_eqcoonb494lo)

[Privacidade (?) no Bitcoin 8](#_hidllwbvdo2u)

[Técnicas de Privacidade 8](#_ab4i6d9vm99x)

[Criptomoedas com privacidade: origem oculta 8](#_rtnacnuxjquq)

[Criptomoedas com privacidade: destino oculto 8](#_yg4y8hiexqgn)

[Criptomoedas com privacidade: valor oculto 9](#_j1et9vh6sl59)

[**Aula 3H - Forks (Bifurcações) 9**](#_7q3gmp3ligt8)

[Relembrando: Forks 9](#_iztz7fsutxeu)

[Atualizações: Mudando regras 9](#_vviojd76vud9)

[Soft forks e Hard forks 9](#_1tkij6hjv441)

[Soft e hard forks: exemplos 9](#_hc43gfj4fzdi)

##

# Aula 2A - Serviços de Segurança

## Serviços básicos de segurança

- Disponibilidade

Tecnologias descentralizadas ajudam por não terem um ponto central de ataque

- Confidencialidade
- Integridade
- Autenticidade
- Irretratabilidade

## Ataques aos serviços

- Interceptação - confidencialidade

![](RackMultipart20231230-1-folsk5_html_c126fedc4f97b0b8.png)

- Interrupção - disponibilidade

![](RackMultipart20231230-1-folsk5_html_badd03d9d04e4f05.png)

- Modificação - integridade e autenticidade

![](RackMultipart20231230-1-folsk5_html_ede6255ed82fd348.png)

- Fabricação - autenticidade

![](RackMultipart20231230-1-folsk5_html_9eeb0fc1a57aaf52.png)

# Aula 2D - Certificação digital e Certificação de Tempo

## Certificados Digitais

- Garantir autenticidade da chave pública
- Autoridades Certificadoras dizem quais são as chaves públicas

## Modelo PKI

- Private Key Infrastructure (ou ICP)

## Tipos de certificados

- **A:** assinatura digital - assinar documentos
- **S:** sigilo - cifração (ex: HTTPS)
- **T:** carimbo de tempo
- utros

## Processo de certificação

1. Chave gerada
2. Envio da chave pública (Ku) com dados cadastrais
3. Certificate signing request
4. AC emite o certificado assinado pela sua chave privada p/ cliente e diretório

## Processo de carimbo de tempo

1. Usuário cria hash dos dados
2. Envia à ACT
3. ACT emite carimbo de tempo assinado com sua chave privada

Carimbo = Cifra(KR-ACT, Hash(dados), tempo)

1. Envio ao usuário

## Descentralizando autoridades

- AC descentralizada: web of trust
- ACT descentralizada: blockchain

# Aula 2E - Construções Avançadas com hashes

## Relembrando

- **Resistência à 1.a inversão**

Impossibilidade de achar dados tendo-se Hash(dados)

- **Resistência à 2.a inversão**

Impossibilidade de achar novos dados M' que Hash(M') = Hash(M)

- **Resistência à 3.a inversão (colisão)**

Impossibilidade de achar quaisquer dados X e Y tal que Hash(X) = Hash(Y)

## Comprometimento

1. Alice mostra Hash(M) para Bob
2. Alice revela M no futuro
3. Bob pode conferir que M é a mensagem que gerou o Hash(M) que Alice mostrou anteriormente calculando o hash (resistência à colisão)

## Usos

- **Sorteio justo**
- **Hash chains**

hn = Hash(hn-1)

Usado para autenticação de usuários

Servidor guarda

h1000 = Hash(Hash(...(Hash(senha)))

Usuário envia h999

Servidor confere que Hash(h999) = h1000

Servidor guarda h999

- **Hashes encadeados**
  - Hash chain + compromisso + dados
  - Verificar sequência de dados
  - Para provar que M está na cadeia, é necessário revelar todos os Mi na frente de M - O(n)
- **Merkle Tree**
  - Hashes em formato de árvore
  - Para provar que M está na árvore, é necessário revelar nós vizinhos no caminho até a raíz

![](RackMultipart20231230-1-folsk5_html_f51c3b3629034fb4.png)

- **Merkle Tree Esparsa**
  - Mensagem M na folha de posição Hash(M)
  - Permite mostrar que M não está na árvore mostrando que tem vazio na posição Hash(M)

# Aula 3A - Motivação para Blockchains

## Ordenação de Eventos

- Solução 1: relógios sincronizados + carimbos de tempo

Problema: necessário confiar nos carimbos

- Solução 2: Usar ACT para poder confiar nos carimbos
- Solução 3: Blockchain

## Blockchain = ACT distribuído

- ACT pode publicar hashes em cadeia para garantir ordenamento de eventos
- Descentralização: proof of work
  - Achar número que Hash(Bloco + número) comece com n zeros
  - Tencontrar = O(10n)
  - Tverificar = O(1)

# Aula 3B - Blockchain sem o hype - Funcionamento

## Bitcoin

- Ledger digital
- Pseudoanonimato

## Blockchain: Processando Eventos

- Fase 1: propagação
- Fase 2: validação (dos eventos, não da veracidade dos dados) e propagação dos blocos

## Blockchain: Encadeando Eventos

- Blocos: hash do bloco antigo + próprio hash + dados + nonce
- Proof of work: encontrar nonce para que Hash(Dados + nonce) comece com n zeros

## Blockchain: Consenso

- Várias possibilidades (proof of …)
- Bitcoin: Proof of Work
  - Solução custosa computacionalmente
  - Resistente a ataques

## Blockchain: Módulos

1. **Aplicação**

Validação (ex: Bitcoin)

1. **Consenso distribuído**

Visão uniforme da rede

1. **Armazenamento + replicação**

Disponibilidade, resistência à censura

1. **Blocos encadeados**

Ordenação

1. **Criptografia (hash, ass. digital)**

Detecção de alterações (integridade), irretratabilidade

- Blockchain: módulos 2 ao 5

# Aula 3C - Logs Transparentes

## Log Transparente

- Apenas módulos 4 e 5
- Não precisa de replicação e consenso
- Uma única entidade insere blocos e monitores observam alterações
- Verificável

## Transparência de Certificados

- Evitar que sites falsos personifiquem sites verdadeiros no caso do comprometimento de ACs
- Log público (árvore de merkel) que permite apenas adição de dados e a verificação da presença de certificados
- Todos os certificados das ACs são adicionados
- Monitores verificam os nós da árvore e a raíz

**Procedimento:**

1. Dono do domínio pede certificado para AC
2. AC checa a posse do domínio, e cria um **pré-certificado** (assina domínio com sua chave privada, mas inclui uma extensão para avisar usuários que não devem utilizar esse certificado ainda, pois ele não foi incluído em um log transparente de transparência de certificados)
3. AC envia o pré-certificado para um provedor de log (ex: Google 'Argon2023' log)
4. Log responde com um **Signed Certificate Timestamp (SCT),** que é uma promessa de que o certificado será incluído ao log em breve
5. Pré certificado é adicionado ao log, e uma nova raíz da merkle tree é assinada
6. AC recebe SCT e envia SCT + certificado para dono do domínio
7. Ao visitar um site, navegador dos usuários verifica se o certificado possui um ou mais SCTs
8. Monitores observam logs para verificar certificados suspeitos, e também podem cobrar de empresas para monitorar seus domínios e notificá-las ao notar mudanças

![](RackMultipart20231230-1-folsk5_html_35e9500838db7a28.png)

[https://certificate.transparency.dev/howctworks/#](https://certificate.transparency.dev/howctworks/#stepby)[stepby](https://certificate.transparency.dev/howctworks/#stepby)

- Como a Transparência de Certificados permite que todos vejam todos os certificados, os donos dos domínios podem ficar sabendo quando um certificado para seu domínio for criado e adicionado ao log (através dos monitores, por exemplo). Isso impede situações como sites maliciosos obtendo certificados para um domínio e enviando-os a usuários sem o conhecimento do dono real do domínio.
- Ex: hacker compromete AC e emite certificado para si mesmo do domínio banco.com.br. Usuários do banco podem entrar no site do hacker achando que estão no site real. Enquanto isso, o banco não faria ideia de que o hacker possui esse certificado. Transparência de Certificados impede essa situação pois o banco veria no log que foi emitido um novo certificado para o domínio banco.com.br.

## Log Transparente: Registro de ativos

- Ao registrar ativo em sistema, seu ativo pode ser roubado pelo dono do sistema. Em um blockchain, ele ainda pode ser roubado pelo nó minerador do blockchain
- Solução 1:
  - enviar Hash(ativo+random) p/ servidor
  - após confirmação, enviar dados
  - não resolve para solução com servidor, pois ele pode alegar que os dados já estavam no banco de dados
- Solução 2:
  - enviar Hash(d+r) p/ servidor
  - inclusão do hash em log transparente
  - envio de d+r ao servidor
  - servidor não pode roubar d
  - também funciona com blockchain mas é mais custoso desnecessariamente

# Aula 3D - Lendas (?) sobre Blockchains

## "Imutabilidade"

- Blockchain (e hashes) dão integridade mas isso não impede mutações, apenas garante sua detecção

## "Irretratabilidade"

- Assinaturas digitais dão irretratabilidade
- Podem ser inseridas no blockchain

## "Veracidade"

- O consenso é para a ordem dos dados, não para sua validação
- Validação dos dados feita pela camada de aplicação

## "Depósito de dados"

- Para armazenamento é uma opção muito pouco escalável (replicação dos dados em todos os nós)
- Existem outras tecnologias de armazenamento distribuído

## "O" Blockchain

- Cada pessoa pode criar seu blockchain

## "Aberto e anônimo"

- Depende de
  - quem valida os dados e adiciona blocos
  - quem pode enviar dados para a rede
  - quem pode visualizar conteúdo do blockchain

## "Leve e eficiente"

- Parte mais custosa: consenso
- Leveza:
  - comparação com outras tecnologias como cartórios e transferências internacionais
  - em blockchains federados, os mecanismos de consenso podem ser leves

## "Pesado"

- XRP Ledges é muito eficiente
- Simplificações deixam mais eficiente:
  - consenso bizantino (nós se conhecem)
  - sorteio justo (nós se conhecem)
  - revezamento ou votação (nós puníveis na vida real)
- Redes federadas
  - Todos usuários identificados
  - Facilitam consenso leve

## Bitcoin leve?

- Bitcoin não tem as simplificações mencionadas
  - usuários não identificados
  - usuários não confiáveis
  - proof of stake assumiria que usuários não seriam mal intencionados

# Aula 3E - Aplicações de Blockchains

## Blockchain: Quando usar?

- Ordenação de eventos
- Distribuído
- Sem confiança entre membros
- Não é necessário o instante de tempo
- Não é interessante quando ataques envolvem eventos que não precisam ser registrados no blockchain

## Como criar soluções

- Defina o problema
- Modele usando ACT
  - Se resolver, blockchain provavelmente resolve também
  - Pode ser que um log transparente baste

## Blockchain: Pagamentos

- Transferência de ativos (moedas)
- Transferências intranacionais são mais fáceis com PIX
- Transferências entre bancos internacionais são mais fáceis com BTC
- Ripple Net: como BTC mas tem menos demora para pagamentos, menos gasto de energia, menor volatilidade, menor taxa e serve para câmbio entre moedas

## Blockchain: outros ativos

- Contratos diversos
  - Ex: jogador de futebol, imóvel
  - Substitui cartório
- **Contratos inteligentes:** não necessariamente associados a blockchains
  - programas com lógica de contrato
  - blockchain: ordenação no tempo dos contratos
- Locked transactions
- Transferência de ativos reais
  - Necessário "tokenizar" ativos
  - Casos mais fáceis: casa (n.o de matrícula), veículo, pessoas (CPF)
  - Casos mais difíceis: produtos sem identificação única (ex: vacas, trigo, etc)
  - Mesmo após tokenizar: como garantir que ações sobre ativos reais se refletem no blockchain - digital twin
- Normalmente é preciso de auditoria por entidade confiável
- Fungibilidade: capacidade de um ativo de ser substituído por outro de mesma quantidade e qualidade sem problemas (ex: Bitcoins são fungíveis)
- Itens que requerem confirmação da data de criação (ex: arte, patentes) podem ser registradas em cartório, ACT, ou como Tokens Não Fungíveis (NFT) em blockchain

# Aula 3F - Aplicações Questionáveis com Blockchains

## Blockchain: Aplicações Revolucionárias (?)

- **Coleta de assinaturas para projeto de lei de iniciativa popular**

**Problema** : câmara diz não conseguir verificar tantas assinaturas, e projeto acaba sendo adotado por parlamentar

**Solução: Blockchain?**

Para verificar assinaturas, basta utilizar assinaturas digitais verificáveis (certificados digitais, p. ex, com ICP). O Blockchain garantiria a ordem dos votos, o que é desnecessário

- **Provar que tomou vacina**

**Problema** : site do Ministério da Saúde sai do ar

**Solução: Blockchain?**

Não requer ordenação, apenas disponibilidade e assinaturas digitais do ministério nos comprovantes de vacinação.

Log transparente serviria para impedir a entidade de saúde de reescrever o passado, por exemplo dizer que alguém tomou a vacina há 3 anos, ou excluir um comprovante (irretratabilidade), mas não impediria a criação de um comprovante falso no instante. A posse de uma assinatura digital também já bastaria para a irretratabilidade.

- **Votação eletrônica: registro de votos em blockchain**

**Problema** : como saber se o voto foi contabilizado? (saber se a urna registrou o número que apertei e se ao contarem os votos no TSE vão contar corretamente)

**Solução: Blockchain?**

Não requer ordenação, inclusive a ordem poderia comprometer o sigilo do voto.

Solução real, com software honesto: assinaturas digitais e divulgação dos resultados pela urna.

Solução real, sem software honesto: impressão do voto para conferir com os votos digitais. Auditabilidade fim-a-fim: entregar comprovantes aos usuários para conferirem.

Log transparente seria interessante para publicar os dados de forma que nem o TSE possa alterá-los sem detecção.

- **Verificação de dados reais quaisquer**

**Problema** : como saber se o usuário tem a experiência que ele alega em certa atividade?

**Solução: Blockchain?**

Não tem ordem. Blockchain não verifica os dados, apenas entra em consenso a respeito da ordem deles.

Solução real: sistemas de reputação (reclame aqui, assinaturas digitais para votos de bom/ruim)

- **Plataforma padronizada para/ compartilhamento de documentos**

**Problema** : empresas com formatos internos diversos

**Solução: Blockchain?**

Não há necessidade de ordenar eventos. Empresas padronizam documentos para colocar no blockchain - blockchain só serve como desculpa para entrar em um acordo de padronização.

Diversas linguagens de padronização: RDF, JSON, XML, Gellish

- " **Problema de transparência global"**

**Problema** : eliminar informações privilegiadas

**Solução: Blockchain?**

Para resolver o problema, todos teriam que inserir suas informações no blockchain, então elas deixariam de ser privilegiadas. Mas nada impede os usuários de simplesmente não inserir informações no blockchain nesse caso, pois o registro de eventos não é necessário para a operação do sistema, como seria no bitcoin, por exemplo ("obriga" os usuários a incluir transações)

- **Auditoria de Redes Definidas por Software (SDN)**

**Problema** : Log das ações do controlador

**Solução: Blockchain?**

O controlador é uma entidade confiável, então os switches da rede podem armazenar as instruções assinadas do controlador localmente.

- **Validação de componentes fornecendo um serviço**

**Problema** : como garantir que contêiner não está comprometido? (executando algo que não deveria)

**Solução: registrar os processos dos contêineres num Blockchain?**

Blockchain não garante a validade dos dados

Não tem ordenação de eventos

Plataforma SPIFFE faz essas verificações sem blockchain

- **Identidades centradas no usuário**

**Problema** : contas para tudo

**Solução: Blockchain?**

Não tem ordenação de eventos

Soluções reais: OpenID, OAuth, Web Of Trust

# Aula 3G - Privacidade em Blockchains

## O que esconder?

- Identidades
  - Quem é o usuário real
  - Origens e destinos de transações
- Quantias
  - Valor de transações
- Metadados
  - Lógica de contratos inteligentes

## Por que esconder?

- Mesmo princípio do sigilo bancário
- Empresas: informações estratégicas
- Pessoas: segurança
- Criminosos: atividades ilegais

## Graus de anonimato

- **Anonimato fraco (pseudoanonimato)**
  - Um só identificador
  - Pro: permite criar sistema de reputação
  - Contra: perda de anonimato se qualquer evento for relacionado ao usuário (inferências)
- **Anonimato forte**
  - Pro: previne ligações entre diferentes eventos de mesmo usuário
  - Contra: dificulta reputação
- Possível ter ambos
  - Ex: fraco para auditores, forte para outros usuários

## Privacidade em pagamentos

- **BTC/ETH**
  - Pseudoanonimato
  - Transferências e conteúdos públicos (origem, destino, valor)
  - Exchanges: conhecem identidades dos usuários que as usam
- **Operadoras tradicionais (bancos, cartões)**
  - Transferências privadas
  - Identidades conhecidas pelo operador
- **Zcash/Monero**
  - Transferências públicas
  - Conteúdo privado (origem, destino, valores)

## Privacidade (?) no Bitcoin

- ID da conta: hash de chave pública
  - Gerado pelo usuário
  - Pseudoanonimato
- Recomendações em redes abertas
  - Usar identificadores distintos para cada transação (receber moedas e enviar "troco")
  - Ocultar endereço de IP ao fazer transações (ex: TOR)
  - Não usar intermediários com política de Know Your Customer (KYC), como exchanges
  - Mesmo assim tem problemas, por exemplo, se alguém enviar moedas de 2 contas diferentes para outra pessoa que só possui 1 conta, pode-se associar as duas contas do enviador.

## Técnicas de Privacidade

- **Mixing**

![](RackMultipart20231230-1-folsk5_html_9d0c7c9068ea6bab.png)

  - Moedas misturadas entre usuários
  - Ilegal em alguns países
  - Problemas:
    - Mixer pode revelar usuários
    - Mixer pode cobrar taxas
    - Mixer pode roubar fundos
  - **Mixing sem mixer**![](RackMultipart20231230-1-folsk5_html_d4acea43a9aa3584.png)
    - Coin Join, Tornado Cash
    - Assinatura de todos os usuários
    - Saída: mínimo de todas as entradas
    - Problemas:
      - Requer interação entre usuários
      - Se um usuário gastar uma moeda do mixing, anula o processo
      - Quantias transferidas permanecem públicas

## Criptomoedas com privacidade: origem oculta

**Assinatura em anel** (ex: Cripto Note)

- Anel: grupo de usuários com chaves públicas ui e privadas ri.
- Assinatura si calculada usando apenas um ri não pode ser atribuída ao usuário i, mas pode ser verificada com qualquer ui dos membros do anel, ou seja, pode ter sido gerada por qualquer um deles.
- A definição do anel não requer interação entre usuários.
- Duas assinaturas si e si' feitas com a mesma chave podem ser detectadas.
- A moeda Monero usa anéis com a \>= 16

## Criptomoedas com privacidade: destino oculto

**Endereços "furtivos" (stealth)** (ex: Monero)

- Cada usuário tem 2 pares de chaves (privada, pública), um de visualização (a, A=aG) e outro de transação (b, B=bG)
- A posse da chave privada de visualização "a" permite saber se a transação é destinada ao usuário que possui "a"
- A posse das chaves privadas de visualização e transação (a, b) permite gastar valores em transações

![](RackMultipart20231230-1-folsk5_html_1ce7813f8c79fdd3.png)

R: Chave Diffire Hellman efêmera gerada no emissor

Conferir se a transação é para usuário:

D = H(aR) + b

Chave para transacionar:

H(aR) + b

## Criptomoedas com privacidade: valor oculto

- Monero: valores apenas visualizados com chave de visualização
- Pedersen Commitments: esconde cada entrada na transação, mas permite operações aritméticas de soma/ subtração entre esses valores, então é possível verificar que o input da transação é igual ao output (previne "gerar" moedas na transação)
- Ring Confidential Transactions (Ring CT): permite provar que uma entrada foi "consumida" com a chave de transação correspondente, sem revelar qual entrada
- Bulletproofs: permite verificar que cada entrada na transação é um valor positivo dentro de certa faixa (previne que sejam feitas transações que criam dívidas)
- Zcash também oculta origem, destino e valores, mas utiliza apenas um protocolo (zk-SNARKs)

# Aula 3H - Forks (Bifurcações)

## Relembrando: Forks

- Nós não estão em consenso a respeito da ordem dos blocos
- Pode ser um dissenso temporário, resolvido quando a rede naturalmente entra em consenso com novos blocos

## Atualizações: Mudando regras

- Governança
  - **Desempenho** (por exemplo, aumentar tamanho do bloco, mudar mecanismo de consenso)
  - **Segurança** (correção de bugs, atualização de algoritmos criptográficos, atualizar lista de nós na federação)
  - **Funcionalidade** (adicionar suporte a contratos inteligentes)
- A gestão da rede é distribuída, alguns nós podem não atualizar as mudanças

## Soft forks e Hard forks

- Causados por atualizações nas regras do blockchain
- **Retrocompatibilidade:** nós atualizados falam com nós desatualizados?

3 tipos de blocos:

- blocos gerados na v1, compatíveis com v2
- blocos gerados na v1, não compatíveis com a v2
- blocos gerados na v2

É gerada bifurcação, com uma cadeia apenas com nós desatualizados e outra com nós atualizados e desatualizados. Quando a cadeia atualizada fica maior que a desatualizada, ela será abortada.

- **Adoção:** alguns nós não se atualizam e continuam na cadeia desatualizada, e outros geram uma nova cadeia atualizada. Registros pré fork são duplicados
- **Soft fork:** atualização com retrocompatibilidade e todos adotam eventualmente
- **Hard fork:** não há retrocompatibilidade ou usuários não aceitam (se usuários resolverem aceitar no futuro, pode tornar-se um soft fork)

## Soft e hard forks: exemplos

**Bitcoin:** blocos pequenos em 2015. Duas propostas:

- Segregated Witness: tirar as assinaturas do bloco. Aumentaria bloco em 2x e evitaria operações maliciosas sobre o ID das transações
- Aumentar o tamanho do bloco: 8 ou 32x maior. Poderia ser necessário cancelar mais transações quando uma for inválida.
- **Hard fork:** não se chegou ao consenso. Moedas foram duplicadas entre Bitcoin e Bitcoin Cash

**Ethereum:** Incidente DAO

- Crowdfunding com blockchain
- Bug no contrato: 50M roubados
- Propostas:
  - Não aceitar moedas roubadas (não rolou)
  - Não fazer nada
  - Desfazer transações a partir do momento do roubo
- Maioria da rede optou por desfazer, enquanto alguns continuaram considerando o roubo: Ethereum e Ethereum Classic

23
