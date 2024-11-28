import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from datetime import datetime

class GyurisOpApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("op.gyuris.hu")
        self.geometry("1000x600")
        self.configure(bg='#f0f0f0')
        
        # Main container
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.create_header()
        self.create_content()
        self.create_footer()
        
    def create_header(self):
        header = ttk.Frame(self.main_frame)
        header.pack(fill=tk.X, pady=(0, 20))
        
        title = ttk.Label(
            header, 
            text="Gyuris Operations Interface", 
            font=('Helvetica', 24, 'bold')
        )
        title.pack()
        
        subtitle = ttk.Label(
            header,
            text="System Management and Monitoring",
            font=('Helvetica', 12)
        )
        subtitle.pack()
        
    def create_content(self):
        content = ttk.Frame(self.main_frame)
        content.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - System Status
        status_frame = ttk.LabelFrame(content, text="System Status")
        status_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        self.create_status_indicators(status_frame)
        
        # Right panel - Operations
        operations_frame = ttk.LabelFrame(content, text="Operations")
        operations_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        self.create_operation_buttons(operations_frame)
        
    def create_status_indicators(self, parent):
        # System status indicators
        statuses = [
            ("Server Status", "Running", "green"),
            ("Database", "Connected", "green"),
            ("Last Backup", "2 hours ago", "orange"),
            ("System Load", "Normal", "green"),
        ]
        
        for label, status, color in statuses:
            frame = ttk.Frame(parent)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            ttk.Label(frame, text=label).pack(side=tk.LEFT)
            status_label = ttk.Label(
                frame, 
                text=status,
                foreground=color
            )
            status_label.pack(side=tk.RIGHT)
            
        # Current time
        self.time_label = ttk.Label(parent, text="")
        self.time_label.pack(pady=10)
        self.update_time()
        
    def create_operation_buttons(self, parent):
        operations = [
            "Start Server",
            "Stop Server",
            "Restart Services",
            "Backup Database",
            "Clear Cache",
            "View Logs"
        ]
        
        for operation in operations:
            btn = ttk.Button(
                parent,
                text=operation,
                command=lambda op=operation: self.handle_operation(op)
            )
            btn.pack(fill=tk.X, padx=10, pady=5)
            
    def create_footer(self):
        footer = ttk.Frame(self.main_frame)
        footer.pack(fill=tk.X, pady=(20, 0))
        
        ttk.Label(
            footer,
            text="© 2024 Gyuris Operations. All rights reserved.",
            font=('Helvetica', 8)
        ).pack(side=tk.LEFT)
        
        link = ttk.Label(
            footer,
            text="Visit Website",
            foreground="blue",
            cursor="hand2",
            font=('Helvetica', 8, 'underline')
        )
        link.pack(side=tk.RIGHT)
        link.bind("<Button-1>", lambda e: webbrowser.open("http://op.gyuris.hu"))
        
    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.configure(text=f"Current Time: {current_time}")
        self.after(1000, self.update_time)
        
    def handle_operation(self, operation):
        messagebox.showinfo(
            "Operation",
            f"{operation} operation initiated.\nThis is a simulation."
        )

if __name__ == "__main__":
    app = GyurisOpApp()
    app.mainloop()
