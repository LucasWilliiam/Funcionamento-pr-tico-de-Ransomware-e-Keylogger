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

#### Lições de Defesa Aprendidas:

* **Monitoramento de Processos:** Keyloggers (como o script de exfiltração) precisam ser executados continuamente (em *background*). Sistemas EDR (Endpoint Detection and Response) podem identificar processos desconhecidos monitorando eventos de teclado.
* **Análise de Tráfego de Rede:** O envio de e-mails periódicos para um destinatário incomum (ou tentativas de login SMTP) é um indicador forte de exfiltração de dados e deve ser sinalizado pelo firewall ou proxy.
* **Mínimo Privilégio:** Limitar as permissões de execução de programas pode dificultar o salvamento de arquivos de log ou a abertura de conexões de rede de saída (SMTP).
