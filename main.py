from pydantic import BaseModel

from langchain.chat_models import ChatOpenAI
from llm_miner.agent import LLMMiner
from llm_miner.reader import JournalReader
from llm_miner.config import config
import openai


openai.base_url="https://api.hunyuan.cloud.tencent.com/v1"
file_path=r'C:\Users\pupu\Desktop\test\4.xml'
publisher='elsevier'
openai.api_key= 'sk-0LMeiAGG8RnrHZ1yilWtRKB1QRWFOEejKAKgRXwokDbXVdGN'



def set_agent(config):
    model_name = config["model_name"]
    simple_model_name = config["simple_model_name"]
    temp = config['temperature']
    llm = ChatOpenAI(model_name=model_name, temperature=temp,openai_api_key=openai.api_key)
    simple_llm = ChatOpenAI(model_name=simple_model_name, temperature=temp,openai_api_key=openai.api_key)
    return llm, simple_llm


llm, simple_llm = set_agent(config)


def main(file_path: str, journal=None):
    global llm, simple_llm

    jr = JournalReader.from_file(file_path, journal)
    if not jr.elements:
        return False

    agent = LLMMiner.from_llm(llm, simple_llm, verbose=config['verbose'])

    for element in jr.elements:
        data = agent.run(element)
        element.set_data(data)

    return jr

