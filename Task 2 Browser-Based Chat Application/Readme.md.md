# Advanced Chat Application using Python

## Project Overview

The Advanced Chat Application is a real-time messaging system developed using Python. The application follows a client-server architecture and provides secure communication between multiple users through a graphical user interface (GUI). It supports authentication, message encryption, chat history, notifications, and multimedia sharing.

---

## Features

### User Authentication

* User Registration
* User Login
* Password Hashing for Security
* SQLite Database Storage

### Real-Time Messaging

* Client-Server Communication
* Multiple Connected Users
* Instant Message Broadcasting

### Graphical User Interface

* Built using Tkinter
* User-Friendly Interface
* Scrollable Chat Window
* Message Input Area

### Message History

* Store Chat Messages in SQLite Database
* Retrieve Previous Conversations

### Multiple Chat Rooms

* General Room
* Study Room
* Gaming Room
* Custom Chat Rooms

### Multimedia Sharing

* Image Sharing
* Video Sharing
* Document Sharing

### Notifications

* Desktop Notifications for New Messages
* Alerts for User Activities

### Emoji Support

* Send and Receive Emojis
* Unicode Emoji Compatibility

### Security

* AES Message Encryption
* Secure Password Storage
* Protected User Authentication

---

## Technologies Used

* Python 3.x
* Socket Programming
* Tkinter
* SQLite
* PyCryptodome
* Plyer
* Pillow
* Multithreading

---

## Project Structure

AdvancedChatApp/

├── server.py

├── client.py

├── database.py

├── auth.py

├── encryption.py

├── requirements.txt

├── README.md

├── uploads/

├── downloads/

└── chat.db

---

## Installation

### Clone or Download Project

Place all project files in a single folder.

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Running the Application

### Step 1: Start Server

```bash
python server.py
```

Expected Output:

```text
Server running...
```

### Step 2: Start Client

Open a new terminal and run:

```bash
python client.py
```

You can open multiple client instances to simulate multiple users.

---

## Database Schema

### Users Table

| Field    | Type |
| -------- | ---- |
| username | TEXT |
| password | TEXT |

### Messages Table

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| message  | TEXT    |

---

## Security Features

* Password Hashing using SHA-256
* AES Encryption for Messages
* Secure Authentication System

---

## Future Enhancements

* Voice Messages
* Video Calling
* Group Chats
* Cloud Database Integration
* Dark Mode Theme
* Mobile Application Version
* End-to-End Encryption
* AI Chatbot Integration

---

## Learning Outcomes

This project demonstrates:

* Socket Programming
* GUI Development
* Database Management
* Cybersecurity Concepts
* Multithreading
* Client-Server Architecture
* Software Engineering Practices

---

## Author

Naveen

---

## License

This project is open-source and intended for educational and learning purposes.
