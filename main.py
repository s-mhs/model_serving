import requests

def get_response(prompt: str):
    return requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen3-vl:8b",
            "stream": False,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        timeout=30
    )

def main() -> int:
    response = get_response("what's your name?")
    response.raise_for_status()
    
    # debug messages
    print("Status:", response.status_code)
    print("Body:", response.text)
    
    print(response.json()["message"]["content"])
    
    return 0 

if __name__ == "__main__":
    main()