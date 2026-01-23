from app.pkgs.prompt.subtask_interface import SubtaskInterface
from app.pkgs.tools.llm import chatCompletion
from app.pkgs.tools.utils_tool import detect_programming_language, get_code_from_str

class SubtaskPro(SubtaskInterface):
    def splitTask(self, newfeature, serviceName, appBasePrompt, projectInfo, projectLib, serviceStruct, appID):
        # The current version does not support this feature
        return "", False

    def write_code(self, requirement_id, service_name, file_path, development_detail, step_id):
        language = detect_programming_language(file_path)
        prompt = f"""
Role: You are a senior full stack developer.
Task: Write the complete code for the file described below.

File path: {file_path}
Step: {step_id}
Development detail:
```
{development_detail}
```

Return only the full code for the file. Do not include explanations.
Please respond in {language}.
"""
        context = [{"role": "user", "content": prompt}]
        message, total_tokens, success = chatCompletion(context)
        code = get_code_from_str(message).strip()
        if not code:
            code = message
        return [{"content": code}], success