from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()

def main():
    target = input("What you want to write?(function, object, request api): ")
    lang_fram = input("What language or framework you want to use?: ")
    
    instructions = """
    Provide a programing learning excersice, that must follow the next order:

    challenge: create {target} in {lang_fram} 

    Give the user instructions on how to build this.
    1. 3-5 concrete features to implement                 
    2. step-by-step thinking process
    3. the exersice must be a common task related with the information from {target}
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
