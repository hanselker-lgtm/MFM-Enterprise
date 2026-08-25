import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import date

class MainWindow:
    def __init__(self, context):
        self.ctx = context
        self.root = tk.Tk()
        self.root.title("MFM — MaritimForeningsManager")
        self.root.geometry("1100x700")
        self.current_user = None
        self._login()

    def _login(self):
        win = tk.Toplevel(self.root)
        win.title("MFM Login")
        win.geometry("360x220")
        win.transient(self.root)
        win.grab_set()

        frame = ttk.Frame(win, padding=20)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="MFM Login", font=("Segoe UI", 16, "bold")).pack(pady=(0,12))
        ttk.Label(frame, text="Username").pack(anchor="w")
        username = ttk.Entry(frame)
        username.pack(fill="x", pady=(0,8))
        ttk.Label(frame, text="Password").pack(anchor="w")
        password = ttk.Entry(frame, show="*")
        password.pack(fill="x")

        def do_login():
            user = self.ctx.users.authenticate(username.get(), password.get())
            if not user:
                messagebox.showerror("MFM Login", "Invalid username or password.")
                return
            self.current_user = user
            win.destroy()
            self._build()

        ttk.Button(frame, text="Login", command=do_login).pack(pady=14)
        win.protocol("WM_DELETE_WINDOW", self.root.destroy)
        username.focus_set()
        self.root.withdraw()

        def on_close():
            if win.winfo_exists():
                win.destroy()
            self.root.destroy()
        win.protocol("WM_DELETE_WINDOW", on_close)
        self.root.wait_window(win)
        if self.current_user:
            self.root.deiconify()

    def _build(self):
        top = ttk.Frame(self.root, padding=12)
        top.pack(fill="x")
        ttk.Label(top, text="MFM — Management & Intelligence", font=("Segoe UI", 18, "bold")).pack(side="left")
        ttk.Button(top, text="Refresh", command=self.refresh).pack(side="right")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(top, textvariable=self.search_var, width=35)
        search_entry.pack(side="right", padx=8)
        ttk.Button(top, text="Search", command=self.run_search).pack(side="right")
        search_entry.bind("<Return>", lambda event: self.run_search())

        nav = ttk.Frame(self.root, padding=(12,0))
        nav.pack(fill="x")
        for text, command in [
            ("Dashboard", self.show_dashboard),
            ("Projects", self.show_projects),
            ("Tasks", self.show_tasks),
            ("Risks", self.show_risks),
            ("Decisions", self.show_decisions),
            ("Accounting", self.show_accounting),
            ("Members", self.show_members),
            ("Bank", self.show_bank),
            ("Users", self.show_users),
            ("System", self.show_system),
            ("Export", self.show_export),
        ]:
            ttk.Button(nav, text=text, command=command).pack(side="left", padx=(0,6))

        self.body = ttk.Frame(self.root, padding=12)
        self.body.pack(fill="both", expand=True)
        self.show_dashboard()

def allowed(self, code):
    return self.ctx.permissions.can(self.current_user, code)

def denied(self):
    messagebox.showwarning("MFM Access", "You do not have permission for this function.")

    def clear(self):
        for child in self.body.winfo_children():
            child.destroy()

    def card(self, parent, title, value, row, col):
        f = ttk.LabelFrame(parent, text=title, padding=18)
        f.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
        ttk.Label(f, text=str(value), font=("Segoe UI", 22, "bold")).pack()
        return f

def show_dashboard(self):
    self.clear()
    ttk.Label(self.body, text="Management Dashboard", font=("Segoe UI", 18, "bold")).pack(anchor="w")

    snapshot = self.ctx.management.snapshot()
    grid = ttk.Frame(self.body)
    grid.pack(fill="x", pady=12)
    for c in range(4):
        grid.columnconfigure(c, weight=1)

    cards = [
        ("Projects", snapshot["projects"]),
        ("Open Tasks", snapshot["open_tasks"]),
        ("Open Risks", snapshot["open_risks"]),
        ("Pending Decisions", snapshot["pending_decisions"]),
        ("Members", snapshot["members"]),
        ("Open Invoices", snapshot["open_invoices"]),
        ("Unmatched Bank", snapshot["unmatched_bank"]),
        ("Result", f"{snapshot['result']:,.2f}"),
    ]
    for i, (title, value) in enumerate(cards):
        self.card(grid, title, value, i // 4, i % 4)

    ttk.Label(self.body, text="Attention Required", font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(12, 6))
    attention = self.ctx.management.attention_items()
    tree = ttk.Treeview(self.body, columns=("priority","item"), show="headings", height=6)
    tree.heading("priority", text="Priority")
    tree.heading("item", text="Item")
    tree.column("priority", width=110)
    tree.column("item", width=700)
    for priority, item in attention:
        tree.insert("", "end", values=(priority, item))
    tree.pack(fill="x")

    ttk.Separator(self.body).pack(fill="x", pady=14)
    ttk.Label(
        self.body,
        text=f"Income {snapshot['income']:,.2f}  |  Expenses {snapshot['expenses']:,.2f}  |  Result {snapshot['result']:,.2f}",
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="w")

    def table(self, columns, rows):
        tree = ttk.Treeview(self.body, columns=columns, show="headings")
        for c in columns:
            tree.heading(c, text=c.replace("_"," ").title())
            tree.column(c, width=180)
        for row in rows:
            tree.insert("", "end", values=[row[c] for c in columns])
        tree.pack(fill="both", expand=True, pady=10)
        return tree

    def show_projects(self):
        if not self.allowed("projects.view"):
            self.denied()
            return
        self.clear()
        head = ttk.Frame(self.body); head.pack(fill="x")
        ttk.Label(head, text="Projects", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Button(head, text="Project Finance", command=self.show_project_finance).pack(side="right", padx=(0,6))
        ttk.Button(head, text="New Project", command=self.new_project).pack(side="right")
        self.table(["id","name","status","budget"], self.ctx.projects.list())


def show_project_finance(self):
    self.clear()
    ttk.Label(self.body, text="Project Finance", font=("Segoe UI", 16, "bold")).pack(anchor="w")
    projects = self.ctx.projects.list()
    if not projects:
        ttk.Label(self.body, text="Create a project first.").pack(anchor="w", pady=10)
        return
    project_names = {str(p["id"]): p["name"] for p in projects}
    selected = tk.StringVar(value=str(projects[0]["id"]))
    row = ttk.Frame(self.body); row.pack(fill="x", pady=10)
    ttk.Label(row, text="Project:").pack(side="left")
    combo = ttk.Combobox(row, textvariable=selected, values=list(project_names.keys()), state="readonly", width=10)
    combo.pack(side="left", padx=6)

    output = ttk.LabelFrame(self.body, text="Budget vs Actual", padding=12)
    output.pack(fill="x", pady=10)

    def refresh():
        for w in output.winfo_children(): w.destroy()
        pid = int(selected.get())
        result = self.ctx.accounting.project_budget_vs_actual(pid)
        ttk.Label(output, text=f"Budget: {result['budget']:,.2f}").pack(anchor="w")
        ttk.Label(output, text=f"Actual: {result['actual']:,.2f}").pack(anchor="w")
        ttk.Label(output, text=f"Variance: {result['variance']:,.2f}").pack(anchor="w")
        ttk.Label(output, text=f"Utilization: {result['utilization']:.1f}%").pack(anchor="w")

    ttk.Button(row, text="Refresh", command=refresh).pack(side="left")
    refresh()

    def new_project(self):
        if not self.allowed("projects.edit"):
            self.denied()
            return
        name = simpledialog.askstring("New Project", "Project name:")
        if not name: return
        try:
            self.ctx.projects.create(name)
            self.show_projects()
        except Exception as e:
            messagebox.showerror("MFM", str(e))

    def show_tasks(self):
        self.clear()
        head = ttk.Frame(self.body); head.pack(fill="x")
        ttk.Label(head, text="Tasks", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Button(head, text="New Task", command=self.new_task).pack(side="right")
        self.table(["id","title","status","due_date","owner"], self.ctx.tasks.list())

    def new_task(self):
        title = simpledialog.askstring("New Task", "Task title:")
        if not title: return
        try:
            self.ctx.tasks.create(title)
            self.show_tasks()
        except Exception as e:
            messagebox.showerror("MFM", str(e))

    def show_risks(self):
        self.clear()
        head = ttk.Frame(self.body); head.pack(fill="x")
        ttk.Label(head, text="Risks", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Button(head, text="New Risk", command=self.new_risk).pack(side="right")
        self.table(["id","title","severity","status","owner"], self.ctx.risks.list())

    def new_risk(self):
        title = simpledialog.askstring("New Risk", "Risk title:")
        if not title: return
        try:
            self.ctx.risks.create(title)
            self.show_risks()
        except Exception as e:
            messagebox.showerror("MFM", str(e))

    def show_decisions(self):
        self.clear()
        head = ttk.Frame(self.body); head.pack(fill="x")
        ttk.Label(head, text="Decisions", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Button(head, text="New Decision", command=self.new_decision).pack(side="right")
        self.table(["id","title","status","owner"], self.ctx.decisions.list())

    def new_decision(self):
        title = simpledialog.askstring("New Decision", "Decision title:")
        if not title: return
        try:
            self.ctx.decisions.create(title)
            self.show_decisions()
        except Exception as e:
            messagebox.showerror("MFM", str(e))


def show_accounting(self):
    self.clear()
    ttk.Label(self.body, text="Accounting", font=("Segoe UI", 16, "bold")).pack(anchor="w")
    buttons = ttk.Frame(self.body)
    buttons.pack(fill="x", pady=8)
    ttk.Button(buttons, text="Chart of Accounts", command=self.show_accounts).pack(side="left", padx=(0,6))
    ttk.Button(buttons, text="Journals", command=self.show_journals).pack(side="left", padx=(0,6))
    ttk.Button(buttons, text="Trial Balance", command=self.show_trial_balance).pack(side="left")
    ttk.Label(self.body, text="Accounting Core v0.1: balanced double-entry journals and trial balance.").pack(anchor="w", pady=10)

def show_accounts(self):
    self.clear()
    head = ttk.Frame(self.body); head.pack(fill="x")
    ttk.Label(head, text="Chart of Accounts", font=("Segoe UI", 16, "bold")).pack(side="left")
    ttk.Button(head, text="New Account", command=self.new_account).pack(side="right")
    self.table(["number","name","account_type"], self.ctx.accounting.accounts())

def new_account(self):
    number = simpledialog.askstring("New Account", "Account number:")
    if not number: return
    name = simpledialog.askstring("New Account", "Account name:")
    if not name: return
    account_type = simpledialog.askstring(
        "New Account", "Type (Asset, Liability, Income, Expense):",
        initialvalue="Expense")
    try:
        self.ctx.accounting.create_account(number, name, account_type)
        self.show_accounts()
    except Exception as e:
        messagebox.showerror("MFM Accounting", str(e))

def show_journals(self):
    self.clear()
    head = ttk.Frame(self.body); head.pack(fill="x")
    ttk.Label(head, text="Posted Journals", font=("Segoe UI", 16, "bold")).pack(side="left")
    ttk.Label(self.body, text="Journal entry creation UI is the next accounting increment.").pack(anchor="w", pady=8)
    self.table(["journal_no","journal_date","description","status"], self.ctx.accounting.journals())

def show_trial_balance(self):
    self.clear()
    ttk.Label(self.body, text="Trial Balance", font=("Segoe UI", 16, "bold")).pack(anchor="w")
    self.table(["number","name","debit","credit"], self.ctx.accounting.trial_balance())

    def refresh(self):
        self.show_dashboard()

    def run(self):
        self.root.mainloop()
