from requests import Session
import json
import uuid

hf_url = "https://huggingface.co/chat"


class ChatBot:
    def __init__(self) -> None:
        self.session = self.get_hc_session()
        self.conversation_list = []
        self.now_conversation = self.new_conversation()

    def get_hc_session(self) -> Session:
        session = Session()
        session.get(hf_url)
        return session
    
    def change_conversation(self, conversation_id: str) -> bool:
        if conversation_id not in self.conversation_list:
            raise Exception("Invalid conversation id. Please check conversation id list.")
        self.now_conversation = conversation_id
        return True
    
    def get_conversation_list(self) -> list:
        return self.conversation_list
    
    def new_conversation(self) -> str:
        err_count = 0
        resp = ""
        while True:
            try:
                resp = self.session.post(hf_url + "/conversation")
                return json.loads(resp.text)['conversationId']
            except BaseException as e:
                err_count += 1
                print(f"[Error] Failed to create new conversation. Retrying... ({err_count})")
                if err_count > 5:
                    raise e
                continue

    def get_cookies(self) -> dict:
        return self.session.cookies.get_dict()
        

    def chat(self, text: str, temperature=0.9, top_p=0.95, repetition_penalty=1.2, top_k=50, truncate=1024, watermark=False, max_new_tokens=1024, stop=["</s>"], return_full_text=False, stream=True, use_cache=False, is_retry=False) -> str:
        if self.now_conversation == "":
            self.now_conversation = self.new_conversation()
        req_json = {
            "inputs": text,
            "parameters": {
                "temperature": temperature,
                "top_p": top_p,
                "repetition_penalty": repetition_penalty,
                "top_k": top_k,
                "truncate": truncate,
                "watermark": watermark,
                "max_new_tokens": max_new_tokens,
                "stop": stop,
                "return_full_text": return_full_text,
                "stream": stream,
            },
            "options": {
                    "use_cache": use_cache,
                    "is_retry": is_retry,
                    "id": str(uuid.uuid4()),
            },
        }
        # print(req_json)
        # print(self.session.cookies.get_dict())
        # print(f"https://huggingface.co/chat/conversation/{self.now_conversation}")
        headers = {
            "Origin": "https://huggingface.co",
            "Referer": f"https://huggingface.co/chat/conversation/{self.now_conversation}",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64",
            "Content-Type": "application/json",
            "Accept": "*/*",
        }
        resp = self.session.post(hf_url + f"/conversation/{self.now_conversation}", json=req_json, stream=True, headers=headers, cookies=self.session.cookies.get_dict())
        res_text = ""
        if resp.status_code == 200:
            for line in resp.iter_lines():
                if line:
                    res = line.decode("utf-8")
                    obj = json.loads(res[1:-1])
                    if "generated_text" in obj:
                        self.conversation_list.append(obj["generated_text"])
                        res_text += obj["generated_text"]
                    elif "error" in obj:
                        raise Exception(obj["error"])
            return res_text
        else:
            raise Exception(f"Failed to chat. Status code: {resp.status_code}")
    

if __name__ == "__main__":
    chatbot = ChatBot()
    print("-----HuggingChat-----")
    while True:
        question = input("> ")
        res = chatbot.chat(question)
        print("< " + res)
