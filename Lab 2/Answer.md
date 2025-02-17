# 📡 Relatório do Laboratório: Implementação de Cliente-Servidor com TCP e UDP  

## 🔍 Objetivo  
Este laboratório tem como objetivo praticar a implementação de comunicação entre cliente e servidor utilizando os protocolos **TCP** (Transmission Control Protocol) e **UDP** (User Datagram Protocol). Através da análise dos códigos fornecidos e da execução das aplicações, busca-se:  
1. Compreender as diferenças fundamentais entre **TCP (orientado a conexão)** e **UDP (sem conexão)**.  
2. Visualizar o comportamento dos protocolos em cenários reais, como handshake (TCP), envio/recebimento de dados e tratamento de erros.  
3. Comparar a confiabilidade do TCP com a eficiência do UDP, utilizando as figuras geradas durante a execução.  

---

## 🖼️ Análise das Figuras  

### Figura 1: TCP Client
**tcp_client.py**
- **Funcionamento**: O cliente TCP inicia uma conexão com o servidor (`connect()`), envia uma mensagem (ex: `"hello"`), e aguarda a resposta modificada (ex: `"HELLO"`).  
- **Observação**: A conexão é estabelecida antes do envio de dados (handshake), garantindo entrega confiável.  

### Figura 2: TCP Server
**tcp_server.py**
- **Funcionamento**: O servidor TCP aguarda conexões (`listen()`), aceita uma (`accept()`), processa a mensagem recebida (ex: converte para maiúsculas), e envia a resposta.  
- **Observação**: Após o envio, a conexão é encerrada (`close()`), seguindo o modelo de comunicação **"one-to-one"**.  

### Figura 3: UDP Client
**udp_client.py**
- **Funcionamento**: O cliente UDP envia datagramas diretamente ao servidor (`sendto()`) sem estabelecer conexão. Não há garantia de entrega ou ordem.  
- **Observação**: A mensagem pode ser perdida ou chegar fora de sequência, mas o protocolo é mais rápido devido à ausência de overhead.  

### Figura 4: UDP Server
**udp_server.py**
- **Funcionamento**: O servidor UDP aguarda datagramas (`recvfrom()`), processa a mensagem, e envia a resposta de volta ao endereço do cliente.  
- **Observação**: Não há estado de conexão, permitindo comunicação **"one-to-many"** ou **"many-to-many"**.  

---

## 📊 Comparação TCP vs. UDP  
| **Característica**       | **TCP**                          | **UDP**                          |  
|---------------------------|----------------------------------|----------------------------------|  
| **Conexão**               | Orientado a conexão (handshake) | Sem conexão                      |  
| **Confiabilidade**        | Entrega garantida e ordenada    | Entrega não garantida            |  
| **Overhead**              | Alto (controle de fluxo, ACKs)  | Baixo                            |  
| **Casos de Uso**          | HTTP, SSH, FTP                  | Streaming, VoIP, DNS            |  
| **Resultado nas Figuras** | Conexão estável e previsível    | Menor latência, mas sem garantias|  

---

## 📝 Conclusão  
Este laboratório permitiu explorar na prática as diferenças entre **TCP** e **UDP**, reforçando conceitos teóricos como confiabilidade, overhead e modelos de comunicação. As figuras ilustram claramente como o TCP prioriza a integridade dos dados, enquanto o UDP favorece a velocidade, sendo essencial escolher o protocolo adequado conforme a aplicação.  

---  

# 📡 Lab Report: Client-Server Implementation with TCP and UDP  

## 🔍 Objective  
This lab aims to practice implementing client-server communication using **TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol). By analyzing the provided code and running the applications, the goals are:  
1. Understand the core differences between **TCP (connection-oriented)** and **UDP (connectionless)**.  
2. Observe protocol behavior in real scenarios, such as handshakes (TCP), data transmission, and error handling.  
3. Compare TCP’s reliability with UDP’s efficiency using the generated figures.  

---

## 🖼️ Figure Analysis  

### Figure 1: TCP Client
**tcp_client.py**
- **Functionality**: The TCP client initiates a connection to the server (`connect()`), sends a message (e.g., `"hello"`), and waits for a modified response (e.g., `"HELLO"`).  
- **Observation**: The connection is established before data exchange (handshake), ensuring reliable delivery.  

### Figure 2: TCP Server
**tcp_server.py**
- **Functionality**: The TCP server listens for connections (`listen()`), accepts one (`accept()`), processes the received message (e.g., converts to uppercase), and sends the response.  
- **Observation**: After sending, the connection is closed (`close()`), following a **"one-to-one"** model.  

### Figure 3: UDP Client
**udp_client.py**
- **Functionality**: The UDP client sends datagrams directly to the server (`sendto()`) without establishing a connection. No delivery or order guarantees.  
- **Observation**: Messages may be lost or arrive out of order, but the protocol is faster due to lower overhead.  

### Figure 4: UDP Server
**udp_server.py**
- **Functionality**: The UDP server waits for datagrams (`recvfrom()`), processes the message, and sends the response back to the client’s address.  
- **Observation**: No connection state, enabling **"one-to-many"** or **"many-to-many"** communication.  

---

## 📊 TCP vs. UDP Comparison  
| **Characteristic**       | **TCP**                          | **UDP**                          |  
|---------------------------|----------------------------------|----------------------------------|  
| **Connection**            | Connection-oriented (handshake) | Connectionless                   |  
| **Reliability**           | Guaranteed, ordered delivery    | No delivery guarantees           |  
| **Overhead**              | High (flow control, ACKs)       | Low                              |  
| **Use Cases**             | HTTP, SSH, FTP                  | Streaming, VoIP, DNS            |  
| **Result in Figures**     | Stable and predictable          | Lower latency, no guarantees     |  

---

## 📝 Conclusion  
This lab provided hands-on experience with **TCP** and **UDP**, highlighting key differences in reliability, overhead, and communication models. The figures demonstrate how TCP prioritizes data integrity, while UDP favors speed, emphasizing the importance of choosing the right protocol based on application requirements.