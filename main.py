import PySimpleGUI as sg
from abc import ABC, abstractmethod

# =============== TEMA SANRIO COMPATÍVEL COM PySimpleGUI 5.x ===============

def sanrio_theme():
    sg.theme("DefaultNoMoreNagging")

    sg.theme_background_color("#FFE6F2")
    sg.theme_text_color("#4A4A4A")
    sg.theme_input_background_color("#FFF7FC")
    sg.theme_button_color(("white", "#FF8AC9"))

sanrio_theme()

# ▸ Helper para botão Sanrio
def B(text):
    return sg.Button(text, size=(20, 1), border_width=0, font=("Helvetica", 12, "bold"))

# ▸ Helper para criar janelas fofas
def Win(title, layout):
    return sg.Window(
        f"🌸 {title} 🌸",
        layout,
        finalize=True,
        modal=True,
        element_padding=(10, 10),
    )

# =======================   SISTEMA BANCÁRIO COM ABC   =======================

# Classe abstrata
class ContaBase(ABC):
    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


class Conta(ContaBase):
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        return False


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


# "Banco" bem simples só pra armazenar tudo na memória mesmo
BD_clientes = {}
BD_contas = {}

# ============================   JANELAS   ============================

def janela_menu():
    layout = [
        [sg.Text(" Banco da Ray", font=("Helvetica", 18, "bold"), text_color="#FF4DA6")],
        [B("Criar Cliente 🩷")],
        [B("Criar Conta 💜")],
        [B("Depositar 💛")],
        [B("Sacar 💙")],
        [B("Ver Contas ✨")],
        [B("Sair ❌")],
    ]
    return Win("Menu", layout)


def janela_criar_cliente():
    layout = [
        [sg.Text("🎀 Criar Cliente")],
        [sg.Text("Nome:"), sg.Input(key="nome")],
        [sg.Text("CPF:"), sg.Input(key="cpf")],
        [B("Salvar 🐱"), B("Voltar 🔙")],
    ]
    return Win("Criar Cliente", layout)


def janela_criar_conta():
    layout = [
        [sg.Text("🎀 Criar Conta")],
        [sg.Text("Número da Conta:"), sg.Input(key="numero")],
        [sg.Text("CPF do Cliente:"), sg.Input(key="cpf")],
        [B("Salvar 🎀"), B("Voltar 🔙")],
    ]
    return Win("Criar Conta", layout)


def janela_depositar():
    layout = [
        [sg.Text("💛 Depósito")],
        [sg.Text("Conta:"), sg.Input(key="conta")],
        [sg.Text("Valor:"), sg.Input(key="valor")],
        [B("Depositar ✨"), B("Voltar 🔙")],
    ]
    return Win("Depositar", layout)


def janela_sacar():
    layout = [
        [sg.Text("💙 Saque")],
        [sg.Text("Conta:"), sg.Input(key="conta")],
        [sg.Text("Valor:"), sg.Input(key="valor")],
        [B("Sacar 💸"), B("Voltar 🔙")],
    ]
    return Win("Sacar", layout)


def janela_ver_contas():
    linhas = []
    for numero, conta in BD_contas.items():
        linhas.append(
            [sg.Text(f"Conta {numero} — {conta.cliente.nome} — Saldo: R$ {conta.saldo:.2f}")]
        )
    if not linhas:
        linhas = [[sg.Text("Nenhuma conta criada ainda 🥺")]]

    layout = [
        [sg.Text("✨ Contas Registradas")],
        *linhas,
        [B("Voltar 🔙")],
    ]

    return Win("Contas", layout)

# ============================   LOOP PRINCIPAL   ============================

win = janela_menu()

while True:
    event, values = win.read()

    if event in (sg.WIN_CLOSED, "Sair ❌"):
        break

    # Criar cliente
    if event == "Criar Cliente 🩷":
        win.hide()
        w2 = janela_criar_cliente()
        e, v = w2.read()

        if e == "Salvar 🐱":
            nome = v["nome"]
            cpf = v["cpf"]
            if cpf not in BD_clientes:
                BD_clientes[cpf] = Cliente(nome, cpf)
                sg.popup("Cliente criado com sucesso! ✨")
            else:
                sg.popup("CPF já cadastrado! 😿")

        w2.close()
        win.un_hide()

    # Criar conta
    if event == "Criar Conta 💜":
        win.hide()
        w2 = janela_criar_conta()
        e, v = w2.read()

        if e == "Salvar 🎀":
            numero = v["numero"]
            cpf = v["cpf"]

            if cpf in BD_clientes:
                BD_contas[numero] = Conta(numero, BD_clientes[cpf])
                sg.popup("Conta criada com sucesso! 🎉")
            else:
                sg.popup("Cliente não encontrado! 😿")

        w2.close()
        win.un_hide()

    # Depositar
    if event == "Depositar 💛":
        win.hide()
        w2 = janela_depositar()
        e, v = w2.read()

        if e == "Depositar ✨":
            num = v["conta"]
            val = float(v["valor"])
            if num in BD_contas and BD_contas[num].depositar(val):
                sg.popup("Depósito realizado com sucesso! 💰✨")
            else:
                sg.popup("Erro ao depositar 😿")

        w2.close()
        win.un_hide()

    # Sacar
    if event == "Sacar 💙":
        win.hide()
        w2 = janela_sacar()
        e, v = w2.read()

        if e == "Sacar 💸":
            num = v["conta"]
            val = float(v["valor"])
            if num in BD_contas and BD_contas[num].sacar(val):
                sg.popup("Saque realizado! 💸✨")
            else:
                sg.popup("Erro ao sacar 😿")

        w2.close()
        win.un_hide()

    # Ver contas
    if event == "Ver Contas ✨":
        win.hide()
        w2 = janela_ver_contas()
        w2.read()
        w2.close()
        win.un_hide()

win.close()
