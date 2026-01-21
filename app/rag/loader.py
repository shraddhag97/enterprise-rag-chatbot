from pathlib import Path

def load_documents(folder_path: str) -> list[str]:
    documents = []
    for file in Path(folder_path).glob("*.txt"):
        documents.append(file.read_text())
    return documents
