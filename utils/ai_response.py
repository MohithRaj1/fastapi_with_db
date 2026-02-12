import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
from dotenv import load_dotenv
load_dotenv()
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def get_completion(user_message, system_message="You are a helpful assistant."):
    """
    Get a completion from the AI model.
    
    Args:
        user_message: The user's message/question
        system_message: The system prompt (default: "You are a helpful assistant.")
    
    Returns:
        The model's response
    """
    try:
        response = client.complete(
            messages=[
                SystemMessage(content=system_message),
                UserMessage(content=user_message),
            ],
            model=model
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in get_completion: {e}")
        raise