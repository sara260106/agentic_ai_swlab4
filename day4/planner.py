# -------------------------------
# PLANNER (Step Generator)
# -------------------------------

def create_plan(user_input):
    
    # Simple planning logic
    if "average" in user_input:
        return [
            "extract_numbers",
            "calculate_average",
            "summarize"
        ]
    
    return ["unknown"]
