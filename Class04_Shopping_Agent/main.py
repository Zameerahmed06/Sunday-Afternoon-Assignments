import requests
from agents import Agent, Runner, function_tool 
from connection import config


@function_tool
def shopping_tool(query: str):
    """
    Search for products from an external shopping API
    based on a user-provided search query (e.g., "headphones", "mug").
    """
    url = "https://dummyjson.com/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        products = data.get("products", [])
        filtered = [p for p in products if query.lower() in p.get("title", "").lower()]
        return {"results": filtered[:5]}
    except Exception as e:
        return {"error": str(e)}

agent = Agent(
    name="Shopping Agent",
    instructions="You are a helpful shopping assistant. Use the tool to search for products.",
    tools=[shopping_tool]
)

result = Runner.run_sync(
    agent, 
    'Search for Eyeshadow Palette with Mirror',
    run_config=config
)

print(result.final_output)

