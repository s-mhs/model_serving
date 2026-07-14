import requests

def get_response(prompt: str):
    return requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "qwen3-v1:8b",
            "stream": False,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
    )

def main() -> int:
    response = get_response("what's your name?")
    response.raise_for_status()
    
    print(response.json()["messages"]["content"])
    
    return 0 

if __name__ == "__main__":
    main()