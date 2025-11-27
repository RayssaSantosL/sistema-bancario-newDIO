# Modelagem de Sistema Bancário em POO 💵✅

Projeto de Modelagem de Sistema Bancário em POO em Python | DESAFIO DIO 

## ✨ Visão Geral  
Este projeto é um mini sistema bancário desenvolvido em **Python**, utilizando:  
- **PySimpleGUI 5.x** para interface gráfica (tema fofinho Sanrio)  
- **`abc`** para implementação de interface abstrata, conforme solicitado no curso  
- Armazenamento simples em memória (sem banco de dados externo)

O objetivo é simular operações bancárias básicas de forma amigável e visual.

---

## 🧩 Arquitetura do Sistema  

### **ContaBase (ABC)**  
Classe abstrata que define o contrato obrigatório das contas:  
- `depositar(valor)`  
- `sacar(valor)`  

### **Conta**  
Implementa a interface `ContaBase`.  
Propriedades:  
- número  
- cliente  
- saldo  

Métodos principais:  
- `depositar(valor)`  
- `sacar(valor)`  

### **Cliente**  
Representa um usuário do banco.  
Atributos:  
- nome  
- cpf  

### **Banco (estrutura de dados)**  
Armazena tudo em memória usando dicionários:  
- `BD_clientes` → mapa CPF → Cliente  
- `BD_contas` → mapa Número da Conta → Conta  

---

## 🎨 Interface Gráfica (GUI)  

Construída com **PySimpleGUI**, com tema personalizado estilo Sanrio (cores pastel, botões fofos e ícones emoji).  
As telas disponíveis são:

### Tela Inicial  
- Criar Cliente  
- Criar Conta  
- Depositar  
- Sacar  
- Ver Contas  

### Criar Cliente  
Formulário para cadastrar nome + CPF.

### Criar Conta  
Solicita número da conta e CPF de um cliente já cadastrado.

### Depositar  
Recebe número da conta + valor.

### Sacar  
Recebe número da conta + valor.

### Ver Contas  
Lista todas as contas com titular e saldo.

---

## 💖 Fluxo de Uso  

1. Abra o programa  
2. Cadastre um cliente  
3. Crie uma conta vinculando o cliente  
4. Realize depósitos e saques  
5. Visualize as contas criadas  

---

## 📦 Instalação  

Certifique-se de ter Python instalado (3.10+).

Instale a biblioteca necessária:

```bash
pip install PySimpleGUI
```
---

## ❌ Limitações atuais

1. Dados não são salvos em arquivo (memória volátil)
2. Não há extrato completo
3. Validações de CPF e Número de conta são simples

---

## 🚀 Possíveis Extensões Futuras

1. Persistência usando SQLite
2. Extrato detalhado com histórico
3. Limite de saque e taxas por tipo de conta
   
---

## 🎀 Créditos
Projeto desenvolvido para fins de estudo, com foco em POO, classes abstratas, GUI e boas práticas em Python. 
By Rayssa Santos 
