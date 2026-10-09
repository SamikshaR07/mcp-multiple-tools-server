\# Week 2: Creating Multiple Tools Using MCP



\## 1. Project Overview



This project demonstrates how to create a single MCP (Model Context Protocol) server that provides multiple tools. Each tool performs a different task.



\## 2. Objective



\* Understand the basics of MCP.

\* Create an MCP server using Python.

\* Implement multiple tools in one server.

\* Test the tools using MCP Inspector.



\## 3. Tools Implemented



1\. \*\*get\_weather()\*\* – Returns sample weather information for a city.

2\. \*\*search\_employee()\*\* – Searches employee details using an employee ID.

3\. \*\*create\_ticket()\*\* – Creates a simulated support ticket.

4\. \*\*get\_quote()\*\* – Returns an inspirational quote.

5\. \*\*send\_notification()\*\* – Simulates sending a notification.



\## 4. Technologies Used



\* Python

\* Model Context Protocol (MCP)

\* FastMCP

\* MCP Inspector

\* GitHub



\## 5. System Architecture



```text

&#x20;      MCP Client / Inspector

&#x20;               |

&#x20;               v

&#x20;           MCP Server

&#x20;               |

&#x20;      +--------+--------+

&#x20;      |        |        |

&#x20;   Weather  Employee  Ticket

&#x20;      |        |        |

&#x20;      +--------+--------+

&#x20;               |

&#x20;      +--------+--------+

&#x20;      |                 |

&#x20;    Quote          Notification

&#x20;      |                 |

&#x20;      +--------+--------+

&#x20;               |

&#x20;               v

&#x20;          Tool Results

```



\## 6. Implementation



The server is implemented in `server.py`. Each Python function is registered as an MCP tool using the `@mcp.tool()` decorator.



All five tools are available through the same MCP server. The server uses standard input/output (stdio) transport to communicate with an MCP client.



\## 7. Testing



MCP Inspector can be used to discover the tools and test their inputs and outputs.



The weather and employee tools use sample data. Ticket creation and notification sending are simulated and do not connect to external services.



\## 8. Result



A single MCP server was created with five different tools. Each tool demonstrates a separate capability.



\## 9. Conclusion



This project demonstrates how to create a multi-tool MCP server using Python and FastMCP. The project can be extended to use real APIs, databases, and external services.



