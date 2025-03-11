from .agents_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, name, max_retries=2, verbose=True):
        super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=max_retries)


    def execute(self, text):
        messages = [
            {"role":"system","content":"You are an AI assistant that summarizes medical texts"}
            {"role":"user",
             "content":("Please provide the concise summary of the following medical text:\n\n"
             f"{text}\n\nSummary:")
             }
        ]
        summary = self.call_openai(messages, max_tokens=300)
        return summary
    
    