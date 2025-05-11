    
    

class LLM():
    def __init__(self):
        pass
    def completions_create(self,client, messages: list, model: str) -> str:
        response = client.chat.completions.create(messages=messages, model=model)
        return str(response.choices[0].message.content)

    def build_prompt_structure(self,prompt: str, role: str) -> dict:
        return {"role": role, "content": prompt}


    def update_chat_history(self,history: list, msg: str, role: str):
        history.append(self.build_prompt_structure(prompt=msg, role=role))


class ChatHistory(list):
    def __init__(self, messages: list | None = None, total_length: int = -1):
        if messages is None:
            messages = []

        super().__init__(messages)
        self.total_length = total_length

    def append(self, msg: str):
        if len(self) == self.total_length:
            self.pop(0)
        super().append(msg)


class FixedFirstChatHistory(ChatHistory):
    def __init__(self, messages: list | None = None, total_length: int = -1):
        super().__init__(messages, total_length)

    def append(self, msg: str):
        if len(self) == self.total_length:
            self.pop(1)
        super().append(msg)
