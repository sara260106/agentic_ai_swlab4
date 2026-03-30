from tools import calculator_tool, weather_tool, summarizer_tool


# -------------------------------
# SIMULATED LLM DECISION
# -------------------------------
def llm_decide_tool(user_input):
    
    prompt = f"User input: {user_input}\nDecide tool: calculator, weather, summarizer"
    
    # Simulated LLM (since API optional)
    if "calculate" in user_input:
        return "calculator"
    elif "weather" in user_input:
        return "weather"
    elif "summarize" in user_input:
        return "summarizer"
    else:
        return "unknown"


# -------------------------------
# LOGGING FUNCTION
# -------------------------------
def log_data(user_input, tool, output):
    with open("logs.txt", "a") as f:
        f.write(f"Input: {user_input}\n")
        f.write(f"Tool: {tool}\n")
        f.write(f"Output: {output}\n")
        f.write("-" * 30 + "\n")


# -------------------------------
# MAIN AGENT
# -------------------------------
def run_agent():
    
    print("LLM-Based Agent Started (type 'exit' to quit)\n")
    
    while True:
        user_input = input("Enter command: ").lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        # LLM decision
        tool = llm_decide_tool(user_input)
        
        # Tool execution
        if tool == "calculator":
            expression = user_input.replace("calculate", "").strip()
            output = calculator_tool(expression)
        
        elif tool == "weather":
            output = weather_tool()
        
        elif tool == "summarizer":
            text = user_input.replace("summarize", "").strip()
            output = summarizer_tool(text)
        
        else:
            output = "I don't understand"
        
        print("Agent:", output)
        
        # Logging
        log_data(user_input, tool, output)


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    run_agent()
