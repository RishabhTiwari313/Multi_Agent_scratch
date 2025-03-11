from .agents_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, name, max_retries=2, verbose=True):
        super().__init__(name="WriteArticleTool", max_retries=max_retries, verbose=max_retries)


    def execute(self, topic, outline = None):
        system_message = "You are an experienced academic writer"
        user_content = f"write a research article on following topic:\nTopic:{topic}\n\n"

        if outline:
            user_content += f"Outline:\n{outline}\n\n"
        user_content += f"Article:\n"

        messages = [
            {"role":"system","content":system_message}
            {"role":"user","content":user_content}
        ]
        
        article = self.call_openai(messages, max_tokens=1000)
        return article
    
    