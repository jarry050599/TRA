import requests
//ABC-t
def call_gpt_api(prompt):
    headers = {
        "Authorization": f"Bearer {GPT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }
    response = requests.post(GPT_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        if "choices" in response_json:
            return response_json["choices"][0]["message"]["content"]
        else:
            print("Error: 'choices' key not found in GPT API response")
            print("Response:", response_json)
    else:
        print(f"Error: GPT API request failed with status code {response.status_code}")
        print("Response:", response.text)
    return None

def call_cloude_api(code):
    headers = {
        "Authorization": f"Bearer {CLOUDE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "code": code
    }
    response = requests.post(CLOUDE_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        if "bugs" in response_json:
            return response_json["bugs"]
        else:
            print("Error: 'bugs' key not found in Cloude API response")
            print("Response:", response_json)
    else:
        print(f"Error: Cloude API request failed with status code {response.status_code}")
        print("Response:", response.text)
    return None

def main():
    # 步驟1：使用GPT生成程式碼
    prompt = "Write a Python function to calculate the factorial of a number."
    generated_code = call_gpt_api(prompt)
    if generated_code:
        print("Generated Code:", generated_code)

        # 步驟2：使用Cloude檢查生成的程式碼是否有BUG
        bugs = call_cloude_api(generated_code)
        if bugs:
            print("Bugs Found:", bugs)
        else:
            print("No bugs found or error in Cloude API response.")
    else:
        print("Failed to generate code from GPT API.")

if __name__ == "__main__":
    main()
