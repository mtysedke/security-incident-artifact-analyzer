"""
browser_history.py

Module for parsing browser history and download artifacts from Chrome/Edge/Brave.
"""

import sqlite3
from typing import List, Dict, Any
from datetime import datetime, timedelta
from pathlib import Path


class BrowserHistoryParser:
    """
    Parses browser history from Chromium-based browsers (Chrome, Edge, Brave, etc.).
    """

    def __init__(self, source_path: str) -> None:
        """
        :param source_path: Path to the browser history SQLite DB file.
                            Example (Chrome):
                            C:/Users/<USER>/AppData/Local/Google/Chrome/User Data/Default/History
        """
        self.source_path = Path(source_path)

    def _convert_chrome_time(self, chrome_time: int) -> str:
        """
        Convert Chrome/WebKit timestamp (microseconds since 1601-01-01) to ISO datetime string.

        :param chrome_time: Chrome/WebKit timestamp
        :return: ISO formatted datetime string or "N/A"
        """
        if not chrome_time:
            return "N/A"

        epoch_start = datetime(1601, 1, 1)
        delta = timedelta(microseconds=chrome_time)
        dt = epoch_start + delta
        return dt.isoformat(sep=" ")

    def parse_history(self, limit: int = 200) -> List[Dict[str, Any]]:
        """
        Parse visited URLs from Chrome/Edge/Brave history SQLite DB.

        :param limit: Maximum number of entries to return.
        :return: List of dicts with URL, title, timestamps, and visit count.
        """

        results: List[Dict[str, Any]] = []

        if not self.source_path.exists():
            return [{"error": f"History file not found: {self.source_path}"}]

        try:
            # If the Chrome file is locked, the user should provide a copied version.
            conn = sqlite3.connect(str(self.source_path))
            cursor = conn.cursor()

            query = f"""
            SELECT url, title, last_visit_time, visit_count
            FROM urls
            ORDER BY last_visit_time DESC
            LIMIT {limit};
            """

            for url, title, ts, count in cursor.execute(query):
                results.append({
                    "url": url,
                    "title": title,
                    "last_visit": self._convert_chrome_time(ts),
                    "visit_count": count
                })

            conn.close()

        except Exception as e:
            return [{"error": f"Failed to parse browser history: {e}"}]

        return results

    def run(self) -> Dict[str, Any]:
        """
        Run all browser history parsing routines.

        :return: Aggregated results in a structured dict.
        """
        return {
            "history": self.parse_history(),
        }
