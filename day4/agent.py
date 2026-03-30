from tools import extract_numbers, calculate_average, summarize_result
from planner import create_plan


# -------------------------------
# LOGGING
# -------------------------------
def log_step(step, output):
    with open("logs.txt", "a") as f:
        f.write(f"{step}: {output}\n")


# -------------------------------
# AGENT
# -------------------------------
def run_agent():
    
    print("Multi-Step Planning Agent Started (type 'exit' to quit)\n")
    
    while True:
        user_input = input("Enter command: ").lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        plan = create_plan(user_input)
        print("Plan:", plan)
        
        data = None
        
        for step in plan:
            
            if step == "extract_numbers":
                data = extract_numbers(user_input)
                print("Step 1 Output:", data)
                log_step(step, data)
            
            elif step == "calculate_average":
                data = calculate_average(data)
                print("Step 2 Output:", data)
                log_step(step, data)
            
            elif step == "summarize":
                data = summarize_result(data)
                print("Final Output:", data)
                log_step(step, data)
            
            else:
                print("Unknown task")
                break


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    run_agent()
