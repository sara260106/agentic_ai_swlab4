# -------------------------------
# Rule-Based AI Agent
# -------------------------------

from datetime import datetime
import re


# -------------------------------
# INPUT HANDLER
# -------------------------------
def get_user_input():
    user_input = input("Enter your command: ")
    return user_input.lower()


# -------------------------------
# DECISION LOGIC (Intent Detection)
# -------------------------------
def detect_intent(user_input):
    if "hello" in user_input or "hi" in user_input:
        return "greeting"
    
    elif "date" in user_input:
        return "date"
    
    elif "calculate" in user_input:
        return "calculation"
    
    else:
        return "unknown"


# -------------------------------
# ACTION EXECUTION
# -------------------------------
def perform_action(intent, user_input):
    
    if intent == "greeting":
        return "Hello! How can I help you?"
    
    elif intent == "date":
        return f"Today's date is: {datetime.now().date()}"
    
    elif intent == "calculation":
        try:
            # Extract math expression after "calculate"
            expression = user_input.replace("calculate", "").strip()
            
            # Safety: allow only numbers and operators
            if not re.match(r'^[0-9+\-*/(). ]+$', expression):
                return "Invalid calculation format."
            
            result = eval(expression)
            return f"Result: {result}"
        
        except:
            return "Error in calculation."
    
    else:
        return "Sorry, I don't understand that command."


# -------------------------------
# MAIN AGENT LOOP
# -------------------------------
def run_agent():
    print("Rule-Based AI Agent Started (type 'exit' to quit)\n")
    
    while True:
        user_input = get_user_input()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        intent = detect_intent(user_input)
        response = perform_action(intent, user_input)
        
        print("Agent:", response)


# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    run_agent()
