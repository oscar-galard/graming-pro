from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()

def main():
    target = input("What you want to write?(function, object, request api): ")
    lang_fram = input("What language or framework you want to use?: ")
    
    instructions = """

Create a concise programming exercise to build {target} using {lang_fram}.

**Requirements:**
- Exercise should take 10–40 minutes to implement.
- Provide only:
  1. **Objective**: One clear task.
  2. **Features**: 2–3 specific, practical features to implement.
  3. **Steps**: Brief, numbered steps (3–5) focusing on core logic.
  4. **Example code stub** (if applicable) showing structure.
- Avoid explanations, theory, bonus tasks, testing instructions, or success criteria.

    """
    
    Prompt = PromptTemplate(
        input_variables=["target", "lang_fram"],
        template=instructions
    )
    
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.8
        )
    
    chain = Prompt | llm
    
    result = chain.invoke({
        "target": target,
        "lang_fram": lang_fram
        })
    
    print(result.content)  

if __name__ == "__main__":
    main()
