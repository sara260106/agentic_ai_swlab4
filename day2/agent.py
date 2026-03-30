# -------------------------------
# TOOL-USING AI AGENT
# -------------------------------

from tools import calculator_tool, weather_tool, summarizer_tool


# -------------------------------
# INTENT DETECTION
# -------------------------------
def detect_intent(user_input):
    
    if "calculate" in user_input:
        return "calculator"
    
    elif "weather" in user_input:
        return "weather"
    
    elif "summarize" in user_input:
        return "summarize"
    
    else:
        return "unknown"


# -------------------------------
# AGENT EXECUTION
# -------------------------------
def run_agent():
    
    print("Tool-Using AI Agent Started (type 'exit' to quit)\n")
    
    while True:
        user_input = input("Enter command: ").lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        intent = detect_intent(user_input)
        
        # TOOL CALLING
        if intent == "calculator":
            expression = user_input.replace("calculate", "").strip()
            response = calculator_tool(expression)
        
        elif intent == "weather":
            response = weather_tool("Nashik")
        
        elif intent == "summarize":
            text = user_input.replace("summarize", "").strip()
            response = summarizer_tool(text)
        
        else:
            response = "Sorry, I don't understand."
        
        print("Agent:", response)


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    run_agent()
