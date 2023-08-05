"""Loader that loads Facebook chat json dump."""
import datetime
import json
from pathlib import Path
from typing import List

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


def concatenate_rows(row: dict) -> str:
    """Combine message information in a readable format ready to be used."""
    sender = row["sender_name"]
    text = row["content"]
    date = datetime.datetime.fromtimestamp(row["timestamp_ms"] / 1000).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    return f"{sender} on {date}: {text}\n\n"


class FacebookChatLoader(BaseLoader):
    """Loader that loads Facebook messages json directory dump."""

    def __init__(self, path: str):
        """Initialize with path."""
        self.file_path = path

    def load(self) -> List[Document]:
        """Load documents."""
        try:
            import pandas as pd
        except ImportError:
            raise ValueError(
                "pandas is needed for Facebook chat loader, "
                "please install with `pip install pandas`"
            )
        p = Path(self.file_path)

        with open(p, encoding="utf8") as f:
            d = json.load(f)

        normalized_messages = pd.json_normalize(d["messages"])
        df_normalized_messages = pd.DataFrame(normalized_messages)

        # Only keep plain text messages
        # (no services, nor links, hashtags, code, bold ...)
        df_filtered = df_normalized_messages[
            (df_normalized_messages.content.apply(lambda x: type(x) == str))
        ]

        df_filtered = df_filtered[["timestamp_ms", "content", "sender_name"]]

        text = df_filtered.apply(concatenate_rows, axis=1).str.cat(sep="")

        metadata = {"source": str(p)}

        return [Document(page_content=text, metadata=metadata)]
