# 🌐 Repositório de Aprendizagem em Redes de Computadores  
**Versão em Inglês abaixo**  

## 📚 Sobre Este Repositório  
Este repositório documenta minha jornada de aprendizagem na disciplina de Redes de Computadores da Universidade do Algarve. Aqui, compartilho implementações práticas, exercícios e conceitos teóricos abordados durante as aulas, com base nos conteúdos dos Capítulos 1 e 2 dos materiais fornecidos.  

---

## 🎯 Objetivos  
- 📖 Integrar teoria (modelos OSI/TCP-IP, HTTP, SMTP, DNS) com prática.  
- 💡 Implementar protocolos de rede (TCP/UDP) e arquiteturas (cliente-servidor, P2P).  
- 🔄 Analisar desempenho de redes (atraso, perda, vazão).  
- 📝 Documentar comparações entre comutação de pacotes e circuitos.  

---

## 🗂️ Estrutura do Repositório  
```
Redes-Computadores/  
├── Teoria/                  # Resumos teóricos dos Capítulos 1 e 2  
│   ├── Camada_de_Aplicacao.md  # HTTP, SMTP, DNS, modelos cliente-servidor/P2P  
│   └── Introducao_Redes.md     # Internet, núcleo da rede, atrasos, pilha de protocolos  
├── Lab 1/                  # Introdução à Programação de Redes  
├── Lab 2/                  # Implementações TCP/UDP  
│   ├── tcp_client.py       # Cliente TCP com análise de congestionamento  
│   ├── udp_server.py       # Servidor UDP com estudo de perdas  
│   └── Relatorio_Lab2.md   # Comparação com dados do Capítulo 2 (HTTP vs SMTP)  
└── ...  
```  

---

## 🛠️ Tecnologias & Conceitos Teóricos  
### Capítulo 1: Introdução às Redes  
- Arquitetura de rede (núcleo, borda, provedores).  
- Comutação de pacotes vs. circuitos.  
- Atrasos (transmissão, propagação, fila), perda e vazão.  
- Pilha de protocolos (TCP/IP, encapsulamento).  

### Capítulo 2: Camada de Aplicação  
- Modelos cliente-servidor e P2P.  
- Protocolos: HTTP (persistente/não persistente), SMTP, POP3, IMAP.  
- DNS (resolução hierárquica, registros RR).  
- Caching Web e GET condicional.  

---

## 💻 Exemplos de Implementação  
- **Cliente-Servidor TCP**: Simulação de conexões HTTP persistentes.  
- **Análise de Atraso**: Scripts para calcular *RTT* com base em dados do Capítulo 1.  
- **Cache Local**: Implementação simplificada de proxy web (Capítulo 2).  

---

## 🎓 Informações do Curso  
- **Instituição**: Universidade do Algarve  
- **Disciplina**: Redes de Computadores  
- **Período**: 2023/2024  
- **Referências**: *Kurose & Ross, Computer Networking: A Top-Down Approach*  

---

## 📈 Progresso do Aprendizado  
- [x] Fundamentos de redes (Capítulo 1)  
- [x] Implementação de sockets TCP/UDP  
- [x] Análise de HTTP e SMTP (Capítulo 2)  
- [ ] Implementação de resolvedor DNS  

---

## 🤝 Contribuições  
Contribuições são bem-vindas! Seja para corrigir detalhes teóricos (*ex.: modelos de camadas*) ou adicionar implementações práticas (*ex.: simulação de cache*).  

---

## 📫 Contato  
Para dúvidas ou sugestões, abra uma *issue* ou envie um e-mail.  

---

## 📄 Licença  
Este projeto está sob licença MIT.  

---  

# 🌐 Computer Networks Learning Repository  
**English Version**  

## 📚 About This Repository  
This repository documents my learning journey in the Computer Networks course at the University of Algarve. Here, I share practical implementations, exercises, and theoretical concepts covered in classes, based on Chapters 1 and 2 of the provided materials.  

---

## 🎯 Objectives  
- 📖 Integrate theory (OSI/TCP-IP models, HTTP, SMTP, DNS) with practice.  
- 💡 Implement network protocols (TCP/UDP) and architectures (client-server, P2P).  
- 🔄 Analyze network performance (delay, loss, throughput).  
- 📝 Document comparisons between packet and circuit switching.  

---

## 🗂️ Repository Structure  
```
Computer-Networks/  
├── Theory/                  # Summaries of Chapters 1 and 2  
│   ├── Application_Layer.md  # HTTP, SMTP, DNS, client-server/P2P models  
│   └── Introduction.md       # Internet basics, network core, delays, protocol stack  
├── Lab 1/                  # Introduction to Network Programming  
├── Lab 2/                  # TCP/UDP Implementations  
│   ├── tcp_client.py       # TCP client with congestion control analysis  
│   ├── udp_server.py       # UDP server with loss study  
│   └── Lab2_Report.md      # Comparison with Chapter 2 data (HTTP vs SMTP)  
└── ...  
```  

---

## 🛠️ Technologies & Theoretical Concepts  
### Chapter 1: Introduction  
- Network architecture (core, edge, ISPs).  
- Packet vs. circuit switching.  
- Delays (transmission, propagation, queueing), loss, throughput.  
- Protocol stack (TCP/IP, encapsulation).  

### Chapter 2: Application Layer  
- Client-server and P2P models.  
- Protocols: HTTP (persistent/non-persistent), SMTP, POP3, IMAP.  
- DNS (hierarchical resolution, RR records).  
- Web caching and conditional GET.  

---

## 💻 Implementation Examples  
- **TCP Client-Server**: Simulation of persistent HTTP connections.  
- **Delay Analysis**: Scripts to calculate RTT based on Chapter 1 data.  
- **Local Cache**: Simplified web proxy implementation (Chapter 2).  

---

## 🎓 Course Information  
- **Institution**: University of Algarve  
- **Course**: Computer Networks  
- **Period**: 2023/2024  
- **References**: *Kurose & Ross, Computer Networking: A Top-Down Approach*  

---

## 📈 Learning Progress  
- [x] Network fundamentals (Chapter 1)  
- [x] TCP/UDP socket implementations  
- [x] HTTP and SMTP analysis (Chapter 2)  
- [ ] DNS resolver implementation  

---

## 🤝 Contributing  
Contributions are welcome! Whether to fix theoretical details (*e.g., layer models*) or add practical implementations (*e.g., cache simulation*).  

---

## 📫 Contact  
For questions or suggestions, open an issue or send an email.  

---

## 📄 License  
This project is licensed under the MIT License.
