# OIBSIP_Python-Programming_3

📌 Project Objective
  The objective of this project is to develop a simple real-time chat application using Python. The application demonstrates client-server communication using     socket programming and provides a basic graphical user interface (GUI) for user interaction.
The project combines networking fundamentals with GUI development to simulate real-time communication between multiple users.

🛠 Tools and Technologies Used
  Python 3
  Socket Programming (for networking)
  Threading Module (for handling multiple clients)
  Tkinter (for GUI interface)
  ScrolledText Widget (for chat display)

🧱 Project Structure
  server.py → Handles multiple client connections and broadcasts messages.
  client.py → GUI-based chat client for sending and receiving messages.

⚙️ Steps Performed
1️⃣ Server Setup
  Created a TCP socket server.
  Bound the server to localhost and a specific port.
  Enabled listening for multiple client connections.
  Used threading to handle multiple clients simultaneously.
  Implemented message broadcasting to all connected users.

2️⃣ Client Development
  Created a socket client to connect to the server.
  Designed a simple GUI using Tkinter.
  Added username prompt on startup.
  Implemented message sending and receiving.
  Used threading to allow real-time message updates without freezing the interface.

3️⃣ Message Handling
  Messages are encoded and decoded using UTF-8.
  When a user joins or leaves, a notification is broadcast to all clients.
  Chat window automatically scrolls to the latest message.

🔄 How the Application Works
  The server starts and waits for client connections.
  Clients connect and provide a username.
  Messages sent by any client are broadcast to all connected users.
  Multiple users can chat simultaneously in real-time.

✅ Key Features
  Real-time messaging
  Multiple client support
  Username identification
  GUI-based interface
  Join/leave notifications
  Simple and clean design

🚀 Outcome
  The final outcome is a fully functional, real-time chat application where multiple users can connect to a server and exchange messages through a graphical   interface.
  The project successfully demonstrates the integration of networking and user interface development in Python while maintaining simplicity and clarity.
