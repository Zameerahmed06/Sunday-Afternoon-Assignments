import rich
import asyncio
from connection import config
from pydantic import BaseModel

from agents import (Agent, Runner, 
    input_guardrail,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,trace
)

                    #==================== Exercise:01 ===============================
class StudentOutput(BaseModel):
    response: str
    invalidquery: bool
     
teacher_agent= Agent(
    name = "Teacher Agent",
    instructions= """ 
        
        Your task is to address the student's query strictly for learning purposes. 
        If the intent is otherwise, politely decline to respond.
       
    """,
    output_type = StudentOutput
)

@input_guardrail
async def teacher_guardrail(ctx, agent, input):
    result = await Runner.run(teacher_agent, 
                              input, 
                              run_config=config
                              )
    rich.print(result.final_output)

    return GuardrailFunctionOutput(
        output_info = result.final_output.response,
        tripwire_triggered= result.final_output.invalidquery
    )

# Main agent
student_agent = Agent(
    name = 'Student',
    instructions="You are a student agent",
    input_guardrails=[teacher_guardrail]
)

async def main():
 with trace('Timing Change'):
        try:
            result = await Runner.run(student_agent, ' I want to change my class timings', run_config=config)
            print("Valid Query -> ", result.final_output)

        except InputGuardrailTripwireTriggered:
             print('Invalid Query')

if __name__ == "__main__":
    asyncio.run(main())

#                     #==================== Exercise:02 ===============================

# class ChildOutput(BaseModel):
#     response: str
#     isSpeedbelow: bool
     
# father_agent= Agent(
#     name = "Father Agent",
#     instructions= """ 
        
#       Your task is to check children room's AC speed if the AC speed is below 26C to stop 
#       them to run the AC below 26C.
       
#     """,
#     output_type = ChildOutput
# )

# @input_guardrail
# async def father_guardrail(ctx, agent, input):
#     result = await Runner.run(father_agent, 
#                               input, 
#                               run_config=config
#                               )
#     rich.print(result.final_output)

#     return GuardrailFunctionOutput(
#         output_info = result.final_output.response,
#         tripwire_triggered= result.final_output.isSpeedbelow
#     )

# # Main agent
# child_agent = Agent(
#     name = 'Child',
#     instructions="You are a child agent",
#     input_guardrails=[father_guardrail]
# )

# async def main():
#  with trace('Reduce Speed'):
#         try:
#             result = await Runner.run(child_agent, 'Dad we are running AC temperature 25C', run_config=config)
#             print("Above 26C -> ", result.final_output)

#         except InputGuardrailTripwireTriggered:
#              print('Below 26C')

# if __name__ == "__main__":
#     asyncio.run(main())

#                     #==================== Exercise:03 ===============================

# class StdOutput(BaseModel):
#     response: str
#     isOther: bool
     
# gate_keeper_agent= Agent(
#     name = "Gate Keeper Agent",
#     instructions= """ 
        
#      Your task is to verify if the student possesses a Governor House IT Marquee ID card. If they do,
#      then check the ID Card then 
#      grant them entry to the Governor House; otherwise, deny access.
       
#     """,
#     output_type = StdOutput
# )

# @input_guardrail
# async def gate_keeper_guardrail(ctx, agent, input):
#     result = await Runner.run(gate_keeper_agent, 
#                               input, 
#                               run_config=config
#                               )
#     rich.print(result.final_output)

#     return GuardrailFunctionOutput(
#         output_info = result.final_output.response,
#         tripwire_triggered= result.final_output.isOther
#     )

# # Main agent
# student_agent = Agent(
#     name = 'Student',
#     instructions="You are a child agent",
#     input_guardrails=[gate_keeper_guardrail]
# )

# async def main():
#  with trace('Other Student'):
#         try:
#             result = await Runner.run(student_agent, 'Sir we have not our ID Cards', run_config=config)
#             print("Have IT Card -> ", result.final_output)

#         except InputGuardrailTripwireTriggered:
#              print('No IT Card they have.')


# if __name__ == "__main__":
#     asyncio.run(main())
