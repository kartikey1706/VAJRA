import sqlite3
from datetime import datetime
from app.models.verification import VerificationRecord

class ErrorDatabase:
    def __init__(self, db_path: str = "vajra_errors.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS verification_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    forecast_id TEXT,
                    valid_time TEXT,
                    variable TEXT,
                    forecast_value REAL,
                    observed_value REAL,
                    error REAL,
                    is_bust INTEGER,
                    timestamp TEXT
                )
            """)
            conn.commit()

    def save_record(self, record: VerificationRecord):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO verification_logs (forecast_id, valid_time, variable, forecast_value, observed_value, error, is_bust, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    record.forecast_id,
                    record.valid_time.isoformat() if hasattr(record.valid_time, 'isoformat') else str(record.valid_time),
                    record.variable,
                    record.forecast_value,
                    record.observed_value,
                    record.error,
                    1 if record.is_bust else 0,
                    datetime.utcnow().isoformat()
                )
            )
            conn.commit()

    def get_historical_errors(self, variable: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM verification_logs WHERE variable = ?", (variable,))
            return cursor.fetchall()

error_db = ErrorDatabase()
