import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# ================= GUI =================
root = tk.Tk()
root.withdraw()

username = simpledialog.askstring("Username", "Enter your username:", parent=root)

root.deiconify()
root.title(f"Chat App - {username}")
root.geometry("500x500")

chat_area = scrolledtext.ScrolledText(root)
chat_area.pack(padx=10, pady=10, fill="both", expand=True)
chat_area.config(state='disabled')

message_entry = tk.Entry(root)
message_entry.pack(padx=10, pady=5, fill="x")

def write():
    message = f"{username}: {message_entry.get()}"
    client.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=write)
send_button.pack(pady=5)

# ================= RECEIVE =================
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client.send(username.encode('utf-8'))
            else:
                chat_area.config(state='normal')
                chat_area.insert(tk.END, message + "\n")
                chat_area.yview(tk.END)
                chat_area.config(state='disabled')
        except:
            print("Error receiving message")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

root.mainloop()
