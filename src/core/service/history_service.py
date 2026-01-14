import os
import json
from datetime import datetime
from typing import Any, Dict, List


HISTORY_FILE = "chat_history.json"


class HistoryService:
    def __init__(self) -> None:
        self.history = self._load_history()

    def _load_history(self) -> Any:
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def _save_history(self) -> None:
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.history, f, default=str)

    def add_interaction(self, prompt: str, response: str, response_type: str) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response,
            "response_type": response_type,
        }
        self.history.append(entry)
        self._save_history()

    def get_full_history(self) -> Any:
        return self.history
