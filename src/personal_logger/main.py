import customtkinter
import logging
import form_elements


DEFAULT_MESSAGE="Enter your log and click Save."
years=form_elements.get_years()
months=form_elements.get_months()
days=form_elements.get_days()
combobox_year_val=""
combobox_month_val=""
combobox_day_val=""
year_selected=False
month_selected=False
day_selected=False

def readable_date():
    return combobox_year_val+" "+combobox_month_val+" "+combobox_day_val

# view button is only active if year, month and day are selected
def show_view_button():
    global year_selected, month_selected, day_selected
    if year_selected and month_selected and day_selected:
        button_view.configure(state="normal")
    else:
        button_view.configure(state="disabled")

# clears the text area
def clear_note():
    text_entry.delete("1.0", "end")
    button_save.configure(state="normal")
    status_label.configure(text=DEFAULT_MESSAGE)

# checks to see if not blank then saves entry
def save_note():

    text=text_entry.get("1.0","end-1c")

    # check if there is any content
    if len(text)>0:
        save_success=logging.write_log(text)
        if save_success:
            text_entry.delete("1.0", "end")
            status_label.configure(text="Entry saved.")
        else:
            status_label.configure(text="Error saving entry.")

def show_log():
    available,contents=logging.read_log(
        combobox_year_val,
        form_elements.get_numeric_month(combobox_month_val),
        combobox_day_val
    )
    text_entry.delete("1.0", "end")
    button_save.configure(state="disabled")

    if available:
        status_label.configure(text=readable_date())
        text_entry.insert("1.0", contents)
    else:
        status_label.configure(text=f"No log found for {readable_date()}.")
        button_save.configure(state="normal")

def select_year(choice):
    global combobox_year_val, year_selected
    if choice!='Year':
        combobox_year_val=choice
        year_selected=True
    else:
        year_selected=False
    show_view_button()

def select_month(choice):
    global combobox_month_val, month_selected
    if choice!='Month':
        combobox_month_val=choice
        month_selected=True
    else:
        month_selected=False
    show_view_button()

def select_day(choice):
    global combobox_day_val, day_selected
    if choice!='Day':
        combobox_day_val=choice
        day_selected=True
    else:
        day_selected=False
    show_view_button()

app = customtkinter.CTk()
app.title("Personal Log")
app.geometry("500x300")
#set appearance Dark, Light, System
customtkinter.set_appearance_mode("System")

# clear and save buttons
button_clear=customtkinter.CTkButton(app,text="Clear",command=clear_note)
button_clear.grid(row=0,column=0,padx=10,pady=10,sticky="ew",columnspan=2)
button_save=customtkinter.CTkButton(app,text="Save",command=save_note)
button_save.grid(row=0,column=2,padx=10,pady=10,sticky="ew",columnspan=2)

# status label
status_label=customtkinter.CTkLabel(app,text=DEFAULT_MESSAGE)
status_label.grid(row=1,column=0,columnspan=4,padx=10,pady=5,sticky="ew")

# text area
text_entry=customtkinter.CTkTextbox(app)
text_entry.grid(row=2,column=0,columnspan=4,padx=10,pady=5,sticky="nesw")

# calendar to view previous log entries
combobox_year=customtkinter.CTkComboBox(app,values=years,command=select_year)
combobox_year.grid(row=3,column=0,padx=10,pady=5,sticky="ew")
combobox_month=customtkinter.CTkComboBox(app,values=months,command=select_month)
combobox_month.grid(row=3,column=1,padx=10,pady=5,sticky="ew")
combobox_day=customtkinter.CTkComboBox(app,values=days,command=select_day)
combobox_day.grid(row=3,column=2,padx=10,pady=10,sticky="ew")
button_view=customtkinter.CTkButton(app,text="View",command=show_log,state="disabled")
button_view.grid(row=3,column=3,padx=10,pady=10,sticky="ew")

app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
app.grid_columnconfigure(2,weight=1)
app.grid_columnconfigure(3,weight=1)
app.grid_rowconfigure(0,weight=0, minsize=25)
app.grid_rowconfigure(1,weight=0, minsize=25)
app.grid_rowconfigure(2,weight=1)

app.mainloop()




