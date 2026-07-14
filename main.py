import requests

def get_response(prompt: str, endpoint: str, model: str, timeout: int=30):
    return requests.post(
        endpoint,
        json={
            "model": model,
            "stream": False,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        timeout=timeout
    )

def main() -> int:
    response = get_response("what's your name?", "http://localhost:11434/api/chat", "qwen3-vl:8b")
    response.raise_for_status()
    
    # debug messages
    print("Status:", response.status_code)
    print("Body:", response.text)
    
    print(response.json()["message"]["content"])
    
    return 0 

if __name__ == "__main__":
    main()