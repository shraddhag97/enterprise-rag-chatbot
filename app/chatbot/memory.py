from typing import Dict, List

chat_memory: Dict[str, List[str]] = {}

def add_user_message(session_id: str, message: str):
    if session_id not in chat_memory:
        chat_memory[session_id] = []
    chat_memory[session_id].append(message)

def get_history(session_id: str) -> List[str]:
    return chat_memory.get(session_id, [])
