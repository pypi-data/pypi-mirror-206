import langchain as lc
from ..modelhandler.modelhandler import _ModelHandler

DEFAULT_LLM_HUB = {hub.lower(): hub for hub in lc.llms.__all__}

class PretrainedModelForQA(_ModelHandler):

    def __init__(self,  hub: str, model: str, *args, **kwargs):
        self.model = model
        self.hub = DEFAULT_LLM_HUB[hub]
        self.kwargs = kwargs

    @classmethod
    def load_model(cls, hub: str, path: str, *args, **kwargs):
        """"""

        try:
            cls.model = getattr(lc, DEFAULT_LLM_HUB[hub])(model_name=path, *args, **kwargs)
            return cls.model
        except:
            raise ValueError(
                f'''Model "{path}" is not found online or local.
                Please install langchain by pip install langchain''')

    def predict(self, text: str, *args, **kwargs):
        return self.model(text, *args, **kwargs)

    def __call__(self, text: str, *args, **kwargs):
        """Alias of the 'predict' method"""
        return self.predict(text=text, *args, **kwargs)
