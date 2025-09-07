from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

translater = Agent(
    name = 'Translater Agent',
    instructions= """You are a translater agent. Tranalate the user input in specific languages what user wants like as Urdu , Sindhi , Spanish etc """
)

response = Runner.run_sync(
    translater,
    input = "How are you. translate this sentence into chines" ,
    run_config = config
    )
print(response.final_output)
