# -------------------------------
# TOOLS MODULE
# -------------------------------

from datetime import datetime


# -------------------------------
# CALCULATOR TOOL
# -------------------------------
def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid calculation."


# -------------------------------
# WEATHER TOOL (MOCK)
# -------------------------------
def weather_tool(city="your city"):
    # Mock data (no API needed)
    return f"Weather in {city}: Sunny, 30°C"


# -------------------------------
# TEXT SUMMARIZER TOOL
# -------------------------------
def summarizer_tool(text):
    words = text.split()
    
    if len(words) <= 5:
        return text
    
    summary = " ".join(words[:5])
    return f"Summary: {summary}..."
