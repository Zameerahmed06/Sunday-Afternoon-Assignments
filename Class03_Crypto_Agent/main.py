from agents import Agent, Runner, function_tool
from connection import config


@function_tool
def crypto_agent():
    return " if usd dollor price is less than 200pkr then quickly buy dollers. If usd dollor price increases in pkr then sell your dollers "


agent = Agent(
    name = 'crypto agent',
    instructions = 
    """
        You are crypto agent. Your task is to
        help user with crypto currencies buy or sell.
    """,
    tools = [crypto_agent]
)



result = Runner.run_sync(agent, 
                         'Hello crypto agent today doller price is 250pkr can what should I do sell or buy doller?',
                         run_config=config
)
print(result.final_output)




