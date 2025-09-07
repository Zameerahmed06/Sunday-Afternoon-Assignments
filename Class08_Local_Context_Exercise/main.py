import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool, trace
from pydantic import BaseModel
import rich


#            ============================Exercise:01======================
class BankAccount(BaseModel):
     account_number: int | str
     customer_name:str
     account_balance:float
     account_type:str


bank_account = BankAccount(
    account_number="ACC-784456",
    customer_name="Zameer",
    account_balance=10500.50,
    account_type="savings"
)

@function_tool
def get_bank_info(wrapper: RunContextWrapper[BankAccount]):
    return f'The bank info is {wrapper.context}'

personal_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant, always call the tool to get user's bank account information",
    tools=[get_bank_info]
)

async def main():
  with trace('Bank Account Info'):
    result = await Runner.run(
        personal_agent, 
        'What is my name, bank account number , account balance and account type', 
        run_config=config,
        context = bank_account 
        )
    rich.print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())


#            ============================Exercise:02======================
# class StudentProfile(BaseModel):
#      student_id:str|int
#      student_name:str
#      current_semester:int
#      total_courses:int


# student = StudentProfile(
#     student_id="ZMA-456",
#     student_name="Zameer Ahmed",
#     current_semester=3,
#     total_courses=2
# )


# @function_tool
# def get_user_info(wrapper: RunContextWrapper[StudentProfile]):
#     return f'The user info is {wrapper.context}'

# personal_agent = Agent(
#     name = "Agent",
#     instructions="You are a helpful assistant, always call the tool to get user's profile information",
#     tools=[get_user_info]
# )

# async def main():
#   with trace('Profile Info'):
#     result = await Runner.run(
#         personal_agent, 
#         'What is my name, id , semester and courses', 
#         run_config=config,
#         context = student 
#         )
#     rich.print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())



#            ============================Exercise:03======================

# class BookInfo(BaseModel):
#     book_id:str|int
#     book_title:str
#     author_name:str
#     is_available:bool

# library_book = BookInfo(
#     book_id="Agents-066",
#     book_title="OpenAI SDK(Agents)",
#     author_name="Sir Zia Khan",
#     is_available=True
# )


# @function_tool
# def get_book_info(wrapper: RunContextWrapper[BookInfo]):
#     return f'The book info is {wrapper.context}'

# personal_agent = Agent(
#     name = "Agent",
#     instructions="You are a helpful assistant, always call the tool to get book information",
#     tools=[get_book_info]
# )

# async def main():
#   with trace('Library Info'):
#     result = await Runner.run(
#         personal_agent, 
#         'tell me book info what you have ?', 
#         run_config=config,
#         context = library_book 
#         )
#     rich.print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())