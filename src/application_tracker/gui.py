"""GUI for the Application Tracker."""

import tkinter as tk

from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date

from .job_application import JobApply
from .application_manager import Application_Manager
from .storage import load_applications_from_file, save_applications_to_file 

class Application_gui:
    def __init__(self):
        """Create the main GUI for the Application Tracker."""
        self.root = tk.Tk()
        self.root.title("Job Application Tracker")
        self.root.geometry("1000x600")
        
        #connect to the application manager
        self.manager = Application_Manager()
        self.manager.applications = load_applications_from_file("test_applications.json")
        self.manager.update_next_id()
        
        #create shared styles for the application
        self.create_styles()
        self.create_title_frame()
        self.create_title()
        self.create_subtitle()
        self.create_main_section()
        self.create_button()
        self.create_dashboard()
        self.create_table()
        
        self.refresh_dashboard()
        self.refresh_table()
        
        #Create shared styles for the application
    def create_styles(self):
        """Create shared styles for the application."""
        self.style = ttk.Style()
        self.style.configure("Header.TFrame", background="#E8F3E8") #pastel green
        self.style.configure("Subheader.TFrame", background="#E8F3E8") #pastel green
        self.style.configure("Section.TFrame",background="#F3F5F4" ) #very light gray
        self.style.configure("widget.TFrame", background="#E8F3E8") #pastel green
        self.style.configure("Title.TLabel", font=("Inter", 16, "bold"), padding=5, foreground="#254D35", background="#E8F3E8") #darkforestgreen, pastel green
        self.style.configure("Subtitle.TLabel", font=("Inter", 10, "bold"), padding=5, foreground="#254D35", background="#E8F3E8") #darkforestgreen, pastel green
        self.style.configure("Section.TLabel", font=("Inter", 10, "bold"),  padding=5, foreground="#254D35", background="#F3F5F4") #darkforestgreen, verylightgray
        self.style.configure("Number.TLabel", font=("Inter", 12, "bold"), padding=5, foreground="#254D35", background="#E8F3E8") #darkforestgreen
        self.style.configure("TButton", font=("Inter", 10), padding=5, foreground="#254D35", background="#E8F3E8") #darkforestgreen
        self.style.configure("Entry.TLabel", font=("Inter", 10))

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
        self.dashboard_frame = ttk.Frame(self.title_frame, style="Section.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.dashboard_frame.pack(fill=tk.X, padx=10, pady=10)

        self.dashboard_title = ttk.Label(self.dashboard_frame, text="Jobs search journey", style="Section.TLabel")
        self.dashboard_title.pack(anchor='w', padx=(0, 10))

        # Create the total frame to display total jobs searched
        self.total_frame = ttk.Frame(self.dashboard_frame, style="widget.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.total_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        self.total_label = ttk.Label(self.total_frame, text="Total Jobs", style="Subtitle.TLabel")
        self.total_label.pack(anchor='w', padx=5, pady=(5, 0))
        self.total_number_label = ttk.Label(self.total_frame, text=str(len(self.manager.list_applications())), style="Number.TLabel")
        self.total_number_label.pack(anchor='w', padx=5, pady=(0, 5))

        # Create the applied frame to display total applications
        self.applied_frame = ttk.Frame(self.dashboard_frame, style="widget.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.applied_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        self.applied_label = ttk.Label(self.applied_frame, text="Active Applications", style="Subtitle.TLabel")
        self.applied_label.pack(anchor='w', padx=5, pady=(5, 0))
        #this part count total number of active applications including those in the interview stage
        self.applied_number_label = ttk.Label(self.applied_frame, text=str(len(self.manager.list_applications_by_status("Applied")) 
                                                + len(self.manager.list_applications_by_status("Interview"))), style="Number.TLabel")
        self.applied_number_label.pack(anchor='w', padx=5, pady=(0, 5))

        #Create the interviewed frame to display total interviews
        self.interviewed_frame = ttk.Frame(self.dashboard_frame, style="widget.TFrame", relief=tk.RIDGE, borderwidth=2)
        self.interviewed_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)
        self.interviewed_label = ttk.Label(self.interviewed_frame, text="Interviews", style="Subtitle.TLabel")
        self.interviewed_label.pack(anchor='w', padx=5, pady=(5, 0))
        self.interviewed_number_label = ttk.Label(self.interviewed_frame,
                                                   text=str(len(self.manager.list_applications_by_status("interview"))), style="Number.TLabel")
        self.interviewed_number_label.pack(anchor='w', padx=5, pady=(0, 5)) 

    def create_main_section(self):
        """Create the main section for Button, Table and later is the chart"""
        self.main_section_frame = ttk.Frame(self.root, style="Section.TFrame")
        self.main_section_frame.pack(fill=tk.BOTH, expand=True)

    #Create buttons
    def create_button(self):
        """create button for add application, update and remove"""
        #Create button frame
        self.button_frame = ttk.Frame(self.main_section_frame, style="Section.TFrame")
        self.button_frame.pack(fill=tk.X, padx=15, pady=10)
        
        #Add Button function
        self.add_button = ttk.Button(self.button_frame, text="Add Application",style="TButton",
                                        command = self.add_app_form)
        self.add_button.pack(side=tk.LEFT, padx=5)

        #Remove button
        self.remove_button = ttk.Button(self.button_frame, text="Remove Application",style="TButton",
                                            command = self.remove_app)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        #Update button
        self.update_button = ttk.Button(self.button_frame, text="Update Application",style="TButton", 
                                        command = self.update_app_form)
        self.update_button.pack(side=tk.LEFT, padx=5)

    def add_app_form(self):
        """open the new window to add application"""
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add New Application")
        self.add_window.geometry("800x500")

        self.add_window_frame = ttk.Frame(self.add_window, style="Section.TFrame")
        self.add_window_frame.pack(fill=tk.BOTH, expand=True) 

        self.form_title = ttk.Label(self.add_window_frame,text="Application Details",style="Title.TLabel",anchor="center")
        self.form_title.pack(fill=tk.BOTH,anchor="w",padx=10,pady=(10, 15)
)
        #add the grid form to make the entry table appear nicer
        self.add_form_frame = ttk.Frame(self.add_window_frame)
        self.add_form_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Allow the input column to expand
        self.add_form_frame.grid_columnconfigure(0, minsize=150)
        self.add_form_frame.grid_columnconfigure(1, weight=1)

        #Collect entry value for application in form of grid, 
        ttk.Label(self.add_form_frame, text="Company", style="Entry.TLabel").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.company_entry = ttk.Entry(self.add_form_frame)
        self.company_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.add_form_frame, text="Jobtype", style="Entry.TLabel").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.job_type_entry = ttk.Combobox(self.add_form_frame,
                            values=["Vollzeit", "Teilzeit", "Minijob", "Werkstudent", "Praktikum"],
                            state="readonly")
        self.job_type_entry.grid(row=2, column=1,sticky="ew", padx=10, pady=6)

        ttk.Label(self.add_form_frame, text="Position", style="Entry.TLabel").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.position_entry = ttk.Entry(self.add_form_frame)
        self.position_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.add_form_frame, text="Location", style="Entry.TLabel").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.location_entry = ttk.Entry(self.add_form_frame)
        self.location_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.add_form_frame, text="Contact", style="Entry.TLabel").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.contact_entry = ttk.Entry(self.add_form_frame)
        self.contact_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.add_form_frame, text="Status", style="Entry.TLabel").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.status_entry = ttk.Combobox(self.add_form_frame,
                            values=["Research","Applied", "Interview","Offer", "Rejected", "Withdrawn"],
                            state="readonly")
        self.status_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=6)
        self.status_entry.set("Applied")  # default status

        ttk.Label(self.add_form_frame, text="Applied Date").grid(row=7, column=0, sticky="w", padx=10, pady=5)
        self.applied_date_entry = DateEntry(  # add calendar
            self.add_form_frame,
            date_pattern="yyyy-mm-dd"
        )
        self.applied_date_entry.grid(row=7, column=1, sticky="ew", padx=10, pady=6)
        #tick the box only if an interview is schedule, otherwise the date is saved as empty
        self.interview_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.add_form_frame, text="Interview Date", variable=self.interview_var).grid(row=8, column=0, sticky="w", padx=10, pady=5)
        self.interview_date_entry = DateEntry(  # add calendar
            self.add_form_frame,
            date_pattern="yyyy-mm-dd"
        )
        self.interview_date_entry.grid(row=8, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.add_form_frame, text="URL", style="Entry.TLabel").grid(row=9, column=0, sticky="w", padx=10, pady=5)
        self.URL_entry = ttk.Entry(self.add_form_frame)
        self.URL_entry.grid(row=9, column=1, sticky="ew", padx=10, pady=5)

        ttk.Label(self.add_form_frame, text="Notes", style="Entry.TLabel").grid(row=10, column=0, sticky="w", padx=10, pady=5)
        self.notes_entry = ttk.Entry(self.add_form_frame)
        self.notes_entry.grid(row=10, column=1, sticky="ew", padx=10, pady=6)

        self.save_button = ttk.Button(self.add_window_frame, text="Save Application", style="TButton", 
                    command=self.save_application)
        self.save_button.pack(pady=20)

    def update_app_form(self):
        """ Open a new window to show and Update application """
    #user choose an application from table below, maybe change later,
    #could move the button below the table
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning( "No Selection",
                                    "Please choose an application to update.")
            return

        item_values = self.tree.item(selected_item[0], "values")
        application_ID = int(item_values[0])
        application = self.manager.get_application(application_ID)
        self.application_to_update = application

        if application is None:
            messagebox.showerror("Error", "Application not found!.")
            return
        #add open new window to show all information
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Update Application")
        self.update_window.geometry("600x600")

        #add window frame, title for a better interface
        self.update_window_frame = ttk.Frame(self.update_window, style="Section.TFrame")
        self.update_window_frame.pack(fill=tk.BOTH, expand=True) 
        self.form_title = ttk.Label(self.update_window_frame,text="Application Details",style="Title.TLabel",anchor="center")
        self.form_title.pack(fill=tk.BOTH,anchor="w",padx=10,pady=(10, 15)
)
        #add the grid form to make the entry table appear nicer
        self.update_form_frame = ttk.Frame(self.update_window_frame)
        self.update_form_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        self.update_form_frame.grid_columnconfigure(0, minsize=150)
        self.update_form_frame.grid_columnconfigure(1, weight=1)


    #add data entry to update information
        ttk.Label(self.update_form_frame, text="Company", style="Entry.TLabel").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.company_entry = ttk.Entry(self.update_form_frame)
        self.company_entry.insert(0, application.company or "")
        self.company_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="Jobtype", style="Entry.TLabel").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.job_type_entry = ttk.Combobox(self.update_form_frame,
                            values=["Vollzeit", "Teilzeit", "Minijob", "Werkstudent", "Praktikum"],
                            state="readonly")
        self.job_type_entry.set(application.job_type)
        self.job_type_entry.grid(row=2, column=1,sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="Position", style="Entry.TLabel").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.position_entry = ttk.Entry(self.update_form_frame)
        self.position_entry.insert(0, application.position or "")
        self.position_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="Location", style="Entry.TLabel").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.location_entry = ttk.Entry(self.update_form_frame)
        self.location_entry.insert(0,application.location or "")
        self.location_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="Contact", style="Entry.TLabel").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.contact_entry = ttk.Entry(self.update_form_frame)
        self.contact_entry.insert(0, application.contact or "")
        self.contact_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="Status", style="Entry.TLabel").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.status_entry = ttk.Combobox(self.update_form_frame,
                            values=["Research","Applied", "Interview","Offer", "Rejected", "Withdrawn"],
                            state="readonly")
        self.status_entry.set(application.status)
        self.status_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="Applied Date").grid(row=7, column=0, sticky="w", padx=10, pady=5)
        self.applied_date_entry = DateEntry(  # add calendar
            self.update_form_frame,
            date_pattern="yyyy-mm-dd"
        )
        self.applied_date_entry.set_date(application.applied_date)
        self.applied_date_entry.grid(row=7, column=1, sticky="ew", padx=10, pady=6)

        self.interview_var = tk.BooleanVar(value=application.interview_date is not None)
        ttk.Checkbutton(self.update_form_frame, text="Interview Date", variable=self.interview_var).grid(row=8, column=0, sticky="w", padx=10, pady=5)
        self.interview_date_entry = DateEntry(  # add calendar
            self.update_form_frame,
            date_pattern="yyyy-mm-dd"
        )
        if application.interview_date:
            self.interview_date_entry.set_date(application.interview_date)
        self.interview_date_entry.grid(row=8, column=1, sticky="ew", padx=10, pady=6)

        ttk.Label(self.update_form_frame, text="URL", style="Entry.TLabel").grid(row=9, column=0, sticky="w", padx=10, pady=5)
        self.URL_entry = ttk.Entry(self.update_form_frame)
        self.URL_entry.insert(0, application.url or "")
        self.URL_entry.grid(row=9, column=1, sticky="ew", padx=10, pady=5)

        ttk.Label(self.update_form_frame, text="Notes", style="Entry.TLabel").grid(row=10, column=0, sticky="w", padx=10, pady=5)
        self.notes_entry = ttk.Entry(self.update_form_frame)
        self.notes_entry.insert(0, application.notes or "")
        self.notes_entry.grid(row=10, column=1, sticky="ew", padx=10, pady=6)
#add save changes button
        self.save_update_button = ttk.Button(self.update_window_frame, text="Save Update", style="TButton", 
                    command=self.save_update)
        self.save_update_button.pack(pady=20)

    def get_interview_date(self):
        """Return the interview date as text, or None if the box is not ticked."""
        if self.interview_var.get():
            return self.interview_date_entry.get()
        return None
    
  #define save update function
    def save_update(self):
        """Read the update form, check the values and save them."""
        try: 
            updates = {
                "company":  self.company_entry.get().strip(),
                "position": self.position_entry.get().strip().title(),
                "job_type": JobApply.valid_job_type(self.job_type_entry.get()),
                "location": self.location_entry.get().strip(),
                "contact":self.contact_entry.get().strip(),
                "status": JobApply.valid_status(self.status_entry.get()),
                "applied_date": JobApply.valid_date(self.applied_date_entry.get(),"applied_date"),
                "interview_date": JobApply.valid_date(self.interview_date_entry.get(),"interview_date"),
                "url": self.URL_entry.get().strip(),
                "notes": self.notes_entry.get().strip(),
            }
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return
        
        self.manager.update_application(self.application_to_update.application_id, updates)
        #Add application to Json
        self.save_data()
        self.refresh_dashboard()
        self.refresh_table()
        self.update_window.destroy()

#check this part
    def save_application(self):
        """Save the new application"""
        if not self.company_entry.get().strip():
            messagebox.showwarning("Missing company", "Please enter a company name.")
            return
        try:
            application = JobApply(
                company  = self.company_entry.get().strip(),
                position = self.position_entry.get().strip(),
                job_type = self.job_type_entry.get().strip(),
                location = self.location_entry.get().strip(),
                contact = self.contact_entry.get().strip(),
                status= self.status_entry.get(),
                applied_date = self.applied_date_entry.get(),
                interview_date = self.interview_date_entry.get(),
                url = self.URL_entry.get().strip(),
                notes= self.notes_entry.get().strip()
            )
        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return
        
        #Add application to manager
        self.manager.add_application(application)
        #Add application to Json
        self.save_data()
        self.refresh_dashboard()
        self.refresh_table()
        self.add_window.destroy()
        
    def remove_app(self):
            """Remove the selected application"""
            selected = self.tree.selection()
            if not selected:
                messagebox.showwarning("No Selection", "Please select an application to remove.")
                return
            application_ID = int(self.tree.item(selected[0], "values")[0])
            application = self.manager.get_application(application_ID)
            confirm = messagebox.askyesno("Remove application",
                                        f"Do you want to delete this application: {application.position} at {application.company}?")
            if not confirm:
                return
                
            self.manager.remove_application(application_ID)
            self.save_data()
            self.refresh_dashboard()
            self.refresh_table()
            messagebox.showinfo("Deleted", "Application deleted successfully.")

    def refresh_dashboard(self):
        """Refresh the dashboard to update the displayed information."""
        self.total_number_label.config(text=str(len(self.manager.list_applications())))
        #show active applications including those in the interview stage
        self.applied_number_label.config(text=str(len(self.manager.list_applications_by_status("Applied")) 
                                                  + len(self.manager.list_applications_by_status("Interview"))))
        self.interviewed_number_label.config(text=str(len(self.manager.list_applications_by_status("Interview"))))

    def create_table(self):
        """Create the table to display applications."""       
        self.tree = ttk.Treeview(self.main_section_frame, 
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


    def refresh_table(self):
        """Display all applications in the table."""
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add applications to the table
        for application in self.manager.applications:
            self.tree.insert("",tk.END,
                values=(
                    application.application_id,
                    application.company,
                    application.position,
                    application.status,
                    application.notes,
                    application.updated_date))

    def save_data(self):
        """Save all applications to the JSON file."""
        save_applications_to_file( self.manager.applications,"test_applications.json")

        
    def run(self):
            """Run the main loop of the GUI."""
            self.root.mainloop()

if __name__ == "__main__":
    app = Application_gui()
    app.run()