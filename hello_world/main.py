import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    AzureTextCompletion,
    OpenAITextCompletion,
)
from semantic_kernel.orchestration.context_variables import ContextVariables
from semantic_kernel.connectors.ai.ollama.services.ollama_chat_completion import OllamaChatCompletion

def main():
    kernel = sk.Kernel()

    kernel.add_chat_service(
    "llama2",
    OllamaChatCompletion(ai_model_id="llama2", url='http://192.168.11.2:11434/api/chat'),
)

    skills_directory = "skills"

    fun_skill = kernel.import_semantic_skill_from_directory(
        skills_directory, "FunSkill"
    )

    joke_function = fun_skill["Joke"]

    # The "input" variable in the prompt is set by "content" in the ContextVariables object.
    context_variables = ContextVariables(
        content="time travel to dinosaur age", variables={"style": "standup comedy"}
    )
    result = joke_function(variables=context_variables)

    print(result)

    # You can also invoke functions like this
    # result = await jokeFunction.invoke_async("time travel to dinosaur age")
    # print(result)


if __name__ == "__main__":
    main()
