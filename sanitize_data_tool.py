from .agents_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self, name, max_retries=2, verbose=True):
        super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=max_retries)


    def execute(self, medical_data):
        messages = [
            {"role":"system","content":"You are an AI assistant that sanitizes medical data by removing Protected Health Information (PHI)"}
            {"role":"user",
             "content":("Remove all PHI data from the following data:\n\n"
             f"{medical_data}\n\Sanitized Data:")
             }
        ]
        sanitized_data = self.call_openai(messages, max_tokens=300)
        return sanitized_data
    
    