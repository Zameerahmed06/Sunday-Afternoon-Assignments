from agents import Agent, Runner, trace
from connection import config
import asyncio
from dotenv import load_dotenv

load_dotenv()

lyric_poetry_agent = Agent(
    name ='Lyric Poetry Agent',
    instructions = 
    """
    You are a Lyric Poetry Agent.
    Your task is to analyze and interpret lyric poetry provided by the user.
    Give a thoughtful explanation (tashreeh) of the given stanzas or poems.

    """
)

narrative_poetry_agent = Agent(
    name ='Narrative Poetry Agent',
    instructions = 
    """
    You are a Narrative Poetry Agent.
    Your task is to analyze and interpret narrative poetry provided by the user.
    Give a thoughtful explanation (tashreeh) of the given stanzas or poems.

    """
)

dramatic_poetry_agent = Agent(
    name ='Dramatic Poetry Agent',
    instructions = 
    """
    You are a Dramatic Poetry Agent.
    Your task is to analyze and interpret dramatic poetry provided by the user.
    Give a thoughtful explanation (tashreeh) of the given stanzas or poems.

    """
)

poetry_agent = Agent(
    name = 'Poetry Agent',
    instructions=
    """
        You are a poetry agent with the ability to delegate poetry to the appropriate specialized agents. 
        There are three types of poetry you handle: Lyric poetry, Narrative poetry, and Dramatic poetry.
        Your task is to analyze the user's input and handover the poem to the correct agent based on its category:

        1. If the poem is Lyric poetry, hand it off to the Lyric Poetry Agent.
        2. If the poem is Narrative poetry, hand it off to the Narrative Poetry Agent.
        3. If the poem is Dramatic poetry, hand it off to the Dramatic Poetry Agent.

    """,
    handoffs=[lyric_poetry_agent,narrative_poetry_agent,dramatic_poetry_agent]
)


async def main():

    with trace("Poetry Agent"):

      result = await Runner.run(poetry_agent,
                              """
                               Stanza 1: 
                               In whispered winds, my heart takes flight,
                               A song of stars in silent night.
                               Each word a tear, each line a flame,
                               A soul unmasked, with none to blame.
                               
                               Stanza 2:
                               I do not tell of battles bold,
                               But of the warmth when hands you hold.
                               Lyric flows from joy or ache—
                               The kind of truth no sword can break.

                              please give me explanation of these two stanzas

                              """,
                              run_config=config)
    
    print(result.final_output)
    print('Last Agent => ',result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())


#(Lyric poetry)
# Stanza 1: 
# In whispered winds, my heart takes flight,
# A song of stars in silent night.
# Each word a tear, each line a flame,
# A soul unmasked, with none to blame.
# Stanza 2:
# I do not tell of battles bold,
# But of the warmth when hands you hold.
# Lyric flows from joy or ache—
# The kind of truth no sword can break.


#(Narrative poetry)
# Stanza 1:
# Beneath the moon, a rider came,
# His eyes like fire, his voice like flame.
# He spoke of lands beyond the sea,
# Of kings and wars, and destiny.
# Stanza 2:
# A maiden wept by candlelight,
# Her love had vanished in the night.
# The tale unfolds in every line,
# A thread of fate by grand design.


#(Dramatic poetry)
# Stanza 1:
# (Pacing the stage, voice trembling)
# You think me cold? Then strike me dead!
# But know this truth before it's said:
# I wore this mask to guard my pain—
# A crown of thorns, not golden chain!
# Stanza 2:
# (Turning to the audience, voice rising)
# I begged the stars for just one sign,
# That love was yours, and fate was mine.
# But silence answered every plea—
# And now, you stand, accusing me?