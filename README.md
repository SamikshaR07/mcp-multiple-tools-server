# Week 2: MCP Multiple Tools Server

## Project Overview

This project demonstrates how to build a single Model Context Protocol (MCP) server that provides multiple tools using Python and FastMCP.

The server exposes five tools through one interface, demonstrating how an MCP server can organize different functions within a single application.

## Objectives

* Understand the basics of the Model Context Protocol (MCP).
* Create an MCP server using Python and FastMCP.
* Implement multiple tools in one server.
* Define tool names, descriptions, inputs, and functionality.
* Test the tools using Python.

## Features

### 1. Get Weather

**Tool:** `get_weather(city)`

Returns sample weather information for supported cities.

### 2. Search Employee

**Tool:** `search_employee(employee_id)`

Returns sample employee information based on an employee ID.

### 3. Create Support Ticket

**Tool:** `create_ticket(title, description)`

Generates a sample support ticket response with its title, description, and status.

### 4. Get Inspirational Quote

**Tool:** `get_quote()`

Returns an inspirational quote.

### 5. Send Notification

**Tool:** `send_notification(message)`

Simulates sending a notification and returns a confirmation message.

## System Architecture

```text
             User / MCP Client
                    |
                    v
             MCP Server
          (Python + FastMCP)
                    |
       +------------+------------+
       |            |            |
       v            v            v
   Weather       Employee      Support
     Tool        Search         Ticket
                   Tool          Tool
       |                           |
       +-------------+-------------+
                     |
          +----------+----------+
          |                     |
          v                     v
       Quote Tool         Notification Tool
```

All five tools are registered with a single MCP server.

## Technologies Used

* Python
* Model Context Protocol (MCP)
* FastMCP
* Python virtual environment
* GitHub

## Project Structure

```text
mcp-multiple-tools-server/
├── server.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

Replace `YOUR-USERNAME` with your actual GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/mcp-multiple-tools-server.git
cd mcp-multiple-tools-server
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Check Python Syntax

```bash
python -m py_compile server.py
```

### 6. Verify Tool Registration

```bash
python -c "import server; print([t.name for t in server.mcp._tool_manager.list_tools()])"
```

The expected tool names are:

* `get_weather`
* `search_employee`
* `create_ticket`
* `get_quote`
* `send_notification`

## Testing

The five Python functions were tested directly to check their basic functionality.

This confirms that the functions return the expected sample responses. Direct function testing does not, by itself, verify communication through the MCP protocol.

## Important Notes

* Weather information is sample data, not a live weather service.
* Employee records are fictional examples.
* Support tickets are generated as sample responses and are not stored in a database.
* Notifications are simulated; no real notifications are sent.
* MCP Inspector testing has not been completed.

## Result

A Python-based MCP server was created with five registered tools in one server. The project files were uploaded to GitHub.

## Conclusion

This project provides a beginner-friendly introduction to building an MCP server with multiple tools. It demonstrates tool registration, function implementation, dependency management, basic testing, and project documentation.
