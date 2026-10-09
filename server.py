from mcp.server.fastmcp import FastMCP

# Create one MCP server
mcp = FastMCP("Week2-Multiple-Tools")


# Tool 1: Get weather information
@mcp.tool()
def get_weather(city: str) -> str:
    """Get sample weather information for a city."""
    weather_data = {
        "coimbatore": "Cloudy, 28°C",
        "chennai": "Sunny, 32°C",
        "delhi": "Clear, 30°C"
    }
    return weather_data.get(
        city.lower(),
        f"Weather data unavailable for {city}"
    )


# Tool 2: Search employee information
@mcp.tool()
def search_employee(employee_id: int) -> str:
    """Search employee details using an employee ID."""
    employees = {
        101: "Arun - IT Department",
        102: "Priya - HR Department",
        103: "Rahul - Security Department"
    }
    return employees.get(employee_id, "Employee not found")


# Tool 3: Create a support ticket
@mcp.tool()
def create_ticket(title: str, description: str) -> str:
    """Create a sample support ticket."""
    return (
        f"Ticket created successfully!\n"
        f"Title: {title}\n"
        f"Description: {description}\n"
        f"Status: Open"
    )


# Tool 4: Get an inspirational quote
@mcp.tool()
def get_quote() -> str:
    """Return an inspirational quote."""
    return "Success comes from consistent learning and practice."


# Tool 5: Send a simulated notification
@mcp.tool()
def send_notification(message: str) -> str:
    """Simulate sending a notification."""
    return f"Notification simulated successfully: {message}"


# Start the MCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")