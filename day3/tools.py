from datetime import datetime

def calculator_tool(expression):
    try:
        return f"Result: {eval(expression)}"
    except:
        return "Invalid calculation"

def weather_tool(city="Nashik"):
    return f"Weather in {city}: Sunny, 30°C"

def summarizer_tool(text):
    words = text.split()
    return "Summary: " + " ".join(words[:5]) + "..."
