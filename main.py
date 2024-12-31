import customtkinter
from services.system_services import SystemService
from services.gemini_services import GeminiService
from CTkMessagebox import CTkMessagebox

app = customtkinter.CTk()
app.geometry("500x300")
app.resizable(False, False)
app.title("How To Run It?")

customtkinter.set_appearance_mode("dark")

def send_question(): CTkMessagebox(title="Result", message= "Your Score: " + GeminiService.send_request(app_name.get()))

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1)
app.grid_rowconfigure(6, weight=1)
app.grid_columnconfigure(0, weight=1)

system_info_label = customtkinter.CTkLabel(
    app, 
    text="Your System Information", 
    font=("Arial", 20, "bold"),
)
system_info_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

cpu_label = customtkinter.CTkLabel(
    app, 
    text="CPU: " + SystemService.get_cpu(), 
    font=("Arial", 14),
)
cpu_label.grid(row=1, column=0, pady=(5, 5), sticky="n")

gpu_label = customtkinter.CTkLabel(
    app, 
    text="GPU: " + SystemService.get_gpu(), 
    font=("Arial", 14),
)
gpu_label.grid(row=2, column=0, pady=(5, 5), sticky="n")

ram_label = customtkinter.CTkLabel(
    app, 
    text="RAM: " + str(SystemService.get_ram()) + " GB", 
    font=("Arial", 14),
)
ram_label.grid(row=3, column=0, pady=(5, 10), sticky="n")

os_label = customtkinter.CTkLabel(app, text="OS: " + SystemService.get_os(), font=("Arial", 14))
os_label.grid(row=4, column=0, pady=(5, 10), sticky="n")

app_name = customtkinter.CTkEntry(app , placeholder_text="Enter The App That You Want To Run",height=30,width=275,font=("Helvetica", 14),corner_radius=50,text_color="white",)
app_name.grid(row=5, column=0, pady=(5, 10), sticky="n")

ask_button = customtkinter.CTkButton(app , text="Ask For Performance",height=30,width=200,font=("Helvetica", 13),corner_radius=50,text_color="white",bg_color="black",command=lambda: send_question())
ask_button.grid(row=6, column=0, pady=(5, 10), sticky="n")

app.mainloop()