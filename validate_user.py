import json
import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
def load_system_prompt():
    """Load system prompt from file"""
    with open('prompts/modified.txt', 'r', encoding='utf-8') as f:
        return f.read()


def validate_user(input_file):
    """Validate user data using LLM"""
    
    # 1. Load the "Law" (System Prompt)
    system_prompt = load_system_prompt()
    
    # 2. Load the "Evidence" (User Data)
    with open(input_file, 'r') as f:
        user_data = json.load(f)
    
    # 3. Call the LLM with separate roles
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            # CHANGE: Move the rules to the 'system' role
            {"role": "system", "content": system_prompt}, 
            
            # CHANGE: Pass ONLY the JSON data to the 'user' role
            {"role": "user", "content": json.dumps(user_data)} 
        ]
    )
    
    # Parse and return
    return json.loads(response.choices[0].message.content)

def main():
    """Entry point"""
    if len(sys.argv) < 2:
        print("Usage: python validate_user.py <input_file.json>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        result = validate_user(input_file)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
