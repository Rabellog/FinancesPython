import tkinter as tk
from tkinter import messagebox

Gastos = {}

def calcular_gastos():
    return sum(gasto[1] for gasto in Gastos.values())

def adicionar_gasto():
    tipo_de_gasto = combo_tipo.get()
    valor_gasto = float(entry_valor.get())
    descricao = entry_descricao.get()

    Gastos[len(Gastos) + 1] = (tipo_de_gasto, valor_gasto, descricao)
    messagebox.showinfo("Sucesso", "Gasto registrado com sucesso!")
    atualizar_listagem()
    atualizar_saldo()

def atualizar_listagem():
    listbox_gastos.delete(0, tk.END)
    for chave, (tipo, valor, descricao) in Gastos.items():
        listbox_gastos.insert(tk.END, f"{chave}° gasto do mês: {tipo} - R$ {valor:.2f}")
        listbox_gastos.insert(tk.END, f"Descrição: {descricao}")
        listbox_gastos.insert(tk.END, "")

def atualizar_saldo():
    salario = float(entry_salario.get())
    total_gastos = calcular_gastos()
    saldo_restante = salario - total_gastos
    label_gastos_valor.config(text=f"R$ {total_gastos:.2f}")
    label_saldo_valor.config(text=f"R$ {saldo_restante:.2f}")

root = tk.Tk()
root.title("Controle de Gastos")
root.configure(bg='#f2f2f2')

title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

def criar_label(master, text, row, column, sticky='w', padx=10, pady=5):
    label = tk.Label(master, text=text, fg='#333333', bg='#f2f2f2', font=label_font)
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return label

criar_label(root, "Seu Salário: R$", 0, 0)
entry_salario = tk.Entry(root, bg='#ffffff', fg='#333333', bd=0, font=entry_font)
entry_salario.grid(row=0, column=1, padx=10, pady=5, sticky='we')

criar_label(root, "Total gasto no mês: R$", 1, 0)
label_gastos_valor = tk.Label(root, text="", fg='#333333', bg='#f2f2f2', font=label_font)
label_gastos_valor.grid(row=1, column=1, padx=10, pady=5, sticky='w')

criar_label(root, "Saldo restante: R$", 2, 0)
label_saldo_valor = tk.Label(root, text="", fg='#333333', bg='#f2f2f2', font=label_font)
label_saldo_valor.grid(row=2, column=1, padx=10, pady=5, sticky='w')

listbox_gastos = tk.Listbox(root, width=50, height=10, bg='#ffffff', fg='#333333', bd=0, font=entry_font)
listbox_gastos.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='we')

criar_label(root, "Tipo de Gasto:", 4, 0)
combo_tipo = tk.StringVar()
combo_tipo.set("Contas")
combo_tipos = tk.OptionMenu(root, combo_tipo, "Contas", "Alimentação", "Lazer")
combo_tipos.config(bg='#ffffff', fg='#333333', width=15, bd=0, font=entry_font) 
combo_tipos.grid(row=4, column=1, padx=10, pady=5, sticky='we')

criar_label(root, "Valor: R$", 5, 0)
entry_valor = tk.Entry(root, bg='#ffffff', fg='#333333', bd=0, font=entry_font)
entry_valor.grid(row=5, column=1, padx=10, pady=5, sticky='we')

criar_label(root, "Descrição:", 6, 0)
entry_descricao = tk.Entry(root, bg='#ffffff', fg='#333333', bd=0, font=entry_font)
entry_descricao.grid(row=6, column=1, padx=10, pady=5, sticky='we')

def configurar_estilo_botao(widget):
    widget.config(fg='white', bg='#4a90e2', pady=10, bd=0, font=button_font)

button_adicionar = tk.Button(root, text="Adicionar Gasto", command=adicionar_gasto)
configurar_estilo_botao(button_adicionar)
button_adicionar.grid(row=7, column=0, columnspan=2, padx=10, pady=20, sticky='we')

root.mainloop()