from app.pkgs.tools.llm_interface import LLMInterface

class LLMPro(LLMInterface):
    def chatCompletion(self, context, fackData="", bill=True):
        # The current version does not support this feature
        return "", 0, False