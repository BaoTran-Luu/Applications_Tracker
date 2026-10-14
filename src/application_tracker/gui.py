"""GUI for the Application Tracker."""

import tkinter as tk

from tkinter import ttk, messagebox 


from .job_application import JobApply
from .application_manager import Application_Manager
 
class Application_gui:
    def __init__(self):
        """Create the main GUI for the Application Tracker."""
        self.root = tk.Tk()
        self.root.title("Job Application Tracker")
        self.root.geometry("1000x600")

        self.create_styles()

        self.create_title_frame()
        self.create_title()
        self.create_subtitle()
        self.create_dashboard()
        self.create_table()
        

        #Create shared styles for the application
    def create_styles(self):
        """Create shared styles for the application."""
        self.style = ttk.Style()
        self.style.configure("Header.TFrame", background="#E8F3E8") #pastel green
        self.style.configure("Subheader.TFrame", background="#DAF3E0")
        self.style.configure("widget.TFrame", background="#E8F3E8") #pastel green
        self.style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), padding=5, foreground="#254D35") #darkforestgreen
        self.style.configure("Subtitle.TLabel", font=("Helvetica", 10), padding=5, foreground="#254D35") #darkforestgreen
        self.style.configure("Number.TLabel", font=("Helvetica", 12, "bold"), padding=5, foreground="#254D35") #darkforestgreen
        self.style.configure("TButton", font=("Helvetica", 10), padding=5, foreground="#254D35", background="#DAF3E0") #darkforestgreen

    def create_title_frame(self):
        """Create the title frame for the application."""
        self.title_frame = ttk.Frame(self.root, style="Header.TFrame")
        self.title_frame.pack(fill=tk.X, padx=10, pady=10)

    def create_title(self):
        """Create the title label for the application."""
        self.title_label = ttk.Label(self.title_frame, text="Job Application Tracker", style="Title.TLabel")
        self.title_label.pack(pady=(10, 5))

    def create_subtitle(self):
        """Create the subtitle label for the application."""
        self.subtitle_label = ttk.Label(self.title_frame, text= "Rejection is just a redirection", style="Subtitle.TLabel")
        self.subtitle_label.pack(pady=(0, 5))

    def create_dashboard(self):
        """ Create the dashboard frame."""
        self.dashboard_frame = ttk.Frame(self.root, style="Subheader.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.dashboard_frame.pack(fill=tk.X, padx=10, pady=10)

        self.dashboard_title = ttk.Label(self.dashboard_frame, text="Jobs search journey", style="Title.TLabel")
        self.dashboard_title.pack(anchor='w', padx=(0, 10))

        # Create the total frame to display total jobs searched
        self.total_frame = ttk.Frame(self.dashboard_frame, style="widget.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.total_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        self.total_label = ttk.Label(self.total_frame, text="Total Jobs", style="Subtitle.TLabel")
        self.total_label.pack(anchor='w', padx=5, pady=(5, 0))
        self.total_number_label = ttk.Label(self.total_frame, text="0", style="Number.TLabel")
        self.total_number_label.pack(anchor='w', padx=5, pady=(0, 5))

        # Create the applied frame to display total applications
        self.applied_frame = ttk.Frame(self.dashboard_frame, style="widget.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.applied_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        self.applied_label = ttk.Label(self.applied_frame, text="Total Applications", style="Subtitle.TLabel")
        self.applied_label.pack(anchor='w', padx=5, pady=(5, 0))
        self.applied_number_label = ttk.Label(self.applied_frame, text="0", style="Number.TLabel")
        self.applied_number_label.pack(anchor='w', padx=5, pady=(0, 5)) 

        #Create the interviewed frame to display total interviews
        self.interviewed_frame = ttk.Frame(self.dashboard_frame, style="widget.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.interviewed_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        self.interviewed_label = ttk.Label(self.interviewed_frame, text="Total Interviews", style="Subtitle.TLabel")
        self.interviewed_label.pack(anchor='w', padx=5, pady=(5, 0))
        self.interviewed_number_label = ttk.Label(self.interviewed_frame, text="0", style="Number.TLabel")
        self.interviewed_number_label.pack(anchor='w', padx=5, pady=(0, 5)) 


    def create_table(self):
        """Create the table to display applications."""
        self.tree = ttk.Treeview(self.root, 
            columns=("ID", "Company", "Position", "Status","Notes", "Updated Date"),
            show="headings")
        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
        self.tree.column("ID", width=50, stretch=False)
        self.tree.column("Company", width=100, stretch=True)
        self.tree.column("Position", width=150, stretch=True)
        self.tree.column("Status", width=150, stretch=False)
        self.tree.column("Notes", width=200, stretch=True)
        self.tree.column("Updated Date", width=100, stretch=False)
        self.tree.pack(fill=tk.BOTH, expand=True)

    
    
    def run(self):
            """Run the main loop of the GUI."""
            self.root.mainloop()

if __name__ == "__main__":
    app = Application_gui()
    app.run()