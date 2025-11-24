# Funcionamento-prático-de-Ransomware-e-Keylogger
Este repositório é o resultado de um desafio prático de cibersegurança focado em análise e prevenção de forma educacional. O objetivo principal é compreender, em um ambiente 100% controlado, o funcionamento interno de dois tipos de malware comuns: Ransomware e Keylogger.

#### O que foi feito no keylogger:

1.  **Captura de Teclas Local (Arquivo `keylogger_local.py`):**
    * Implementação usando a biblioteca `pynput` para escutar e registrar eventos de teclado.
    * As teclas alfanuméricas e símbolos são escritas diretamente, enquanto teclas especiais (como `Enter`, `Space`, `Tab`) são convertidas ou registradas de forma legível.
    * Teclas de modificação (Ctrl, Shift, Alt, etc.) são ativamente **ignoradas** para manter o log limpo e focado no conteúdo digitado.
    * O log é persistentemente salvo no arquivo `log.txt`.

2.  **Exfiltração Automática por E-mail (Arquivo `keylogger_exfiltracao.py`):**
    * **Mecanismo de Furtividade:** Em vez de salvar em arquivo, o código armazena as teclas capturadas em uma variável global (`log`).
    * **Exfiltração:** Utiliza os módulos `smtplib` e `email.mime.text` para empacotar o log e enviá-lo periodicamente (a cada 60 segundos, usando `threading.Timer`) para um e-mail de destino configurado (em um servidor de e-mail de teste).
    * **Estudo Defensivo:** Esta técnica revela como malwares criam padrões de comunicação (ex: conexões SMTP periódicas) que podem ser identificados por firewalls, sistemas de prevenção de intrusão (IPS) ou sistemas de monitoramento de tráfego de rede.

#### Tecnologias Utilizadas:

* **Python 3:** Linguagem principal.
* **`pynput`:** Biblioteca essencial para monitorar e controlar dispositivos de entrada (teclado).
* **`smtplib` e `email.mime.text`:** Utilizados para simular o processo de exfiltração de dados via e-mail.
* **`threading.Timer`:** Usado para agendar o envio periódico do log, simulando a rotina de um malware.
* 
#### Lições de Defesa Aprendidas:

* **Monitoramento de Processos:** Keyloggers (como o script de exfiltração) precisam ser executados continuamente (em *background*). Sistemas EDR (Endpoint Detection and Response) podem identificar processos desconhecidos monitorando eventos de teclado.
* **Análise de Tráfego de Rede:** O envio de e-mails periódicos para um destinatário incomum (ou tentativas de login SMTP) é um indicador forte de exfiltração de dados e deve ser sinalizado pelo firewall ou proxy.
* **Mínimo Privilégio:** Limitar as permissões de execução de programas pode dificultar o salvamento de arquivos de log ou a abertura de conexões de rede de saída (SMTP).


### Ransomware Simulado: Estudo de Criptografia e Cadeia de Ataque

Este script (`ransomware.py`) simula a fase de execução de um ataque de Ransomware, focado em entender como a **criptografia** é usada para negar o acesso aos dados da vítima e como a chave de descriptografia é crucial para a recuperação.

#### O que foi feito no Ransoware:

1.  **Geração e Gerenciamento de Chave:**
    * A função `gerar_chave()` cria uma chave criptográfica simétrica única usando a biblioteca `cryptography.fernet`.
    * A chave é salva em um arquivo (`chave.key`), simulando o que um atacante faria (guardar a chave antes de iniciar a criptografia). Esta chave é essencial para a descriptografia e é o **"segredo"** do resgate.

2.  **Busca e Criptografia de Arquivos:**
    * A função `encontrar_arquivos()` simula a varredura do sistema, excluindo o próprio script do Ransomware e o arquivo da chave (`.key`). **Atenção:** A simulação foi limitada ao diretório `test_files` para garantir um ambiente 100% seguro.
    * `criptografar_arquivo()` utiliza a chave gerada e o algoritmo **Fernet** (que implementa AES 128-bit no modo CBC com HMAC) para criptografar o conteúdo dos arquivos.

3.  **Geração da Mensagem de Resgate:**
    * A função `criar_mensagem_resgate()` gera o arquivo `LEIA ISSO.txt`, comunicando o sequestro dos dados e as "instruções" de pagamento em Bitcoin. Este é o ponto de contato do atacante com a vítima.

#### Tecnologias Utilizadas:

* **Python 3:** Linguagem principal.
* **`cryptography.fernet`:** Biblioteca robusta utilizada para implementar a criptografia simétrica (padrão **AES 128-bit** com Fernet), que é o cerne do sequestro de dados.
* **`os`:** Módulo usado para navegar pelo sistema de arquivos (`os.walk`) e localizar os alvos para criptografia.

#### Lições de Defesa Aprendidas:

* **Importância do Backup Offline:** A única defesa garantida contra um Ransomware que utiliza criptografia forte (como AES) é ter **backups externos e desconectados** da rede. Se o atacante não tem como acessar os dados originais, o ataque é neutralizado.
* **Monitoramento Comportamental:** A criptografia em massa de arquivos gera um padrão de I/O (Input/Output) anômalo no disco rígido. Soluções EDR (Endpoint Detection and Response) são capazes de detectar e **interromper** esse comportamento antes que todos os arquivos sejam comprometidos.
* **Segmentação de Rede e Princípio do Mínimo Privilégio:** Redes segmentadas limitam o alcance de um Ransomware, impedindo que ele se espalhe para servidores críticos. Além disso, a execução de softwares com privilégios limitados restringe o volume de arquivos que podem ser acessados e criptografados.
