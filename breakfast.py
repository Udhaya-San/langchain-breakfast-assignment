from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = """
Give exactly 5 healthy breakfast ideas.

Rules:
1. Numbered list
2. One line per item
3. No introduction
4. No conclusion
"""

reply = llm.invoke(prompt)

print(reply.content)