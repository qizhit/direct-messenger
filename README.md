# Direct Messaging Chat App

## Project Overview
This project is a GUI-based direct messaging application built with Python and Tkinter as part of the ICS 32 course at UC Irvine. It allows users to securely send and receive direct messages via the Distributed Social Platform (DSP) server using a defined messaging protocol.

The application consists of three main components:
- **Messaging Protocol** (`ds_protocol.py`): Handles JSON-based communication with the server, including sending and retrieving direct messages.
- **Direct Messaging Backend** (`ds_messenger.py`): Defines classes and methods for message creation, sending, and retrieval, independent of the GUI.
- **Graphical User Interface** (`a5.py`): A Tkinter-based chat interface for selecting contacts, sending messages, and displaying conversations. Previous messages and contacts are cached locally and automatically reloaded when the app starts.

## Features
- Send direct messages to any user on the DSP server.
- Retrieve new and all past messages.
- Store messages and recipient data locally for offline access.
- Automatically refresh messages while the app is running.
- Visually distinguishes between incoming and outgoing messages.
- Responsive GUI with contact list, conversation display, input box, and user management tools.

## Requirements
- Python 3.6+
- Internet connection (to communicate with the DS server)
- `tkinter` (included with Python standard library)

## How to Run
Run the following command in the terminal:
```
python3 a5.py
```
The GUI will launch automatically.

## GUI Interface
![IMG_0479](https://github.com/user-attachments/assets/f73108d7-b408-4271-b670-1f124bd3c10c)
