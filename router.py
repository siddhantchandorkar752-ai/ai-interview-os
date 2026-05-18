def route_question(user_input):

    user_input = user_input.lower()

    if 'python' in user_input:
        return 'python'
    
    elif 'machine learning' in user_input or 'ml' in user_input:
        return 'machine_learning'
    
    elif 'prompt' in user_input:
        return 'genai'
    
    else:
        return 'general'