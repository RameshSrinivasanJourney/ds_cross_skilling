from langfuse import get_client

from app.config.langfuse_config import (
    load_dotenv,
)

# Load environment variables.
load_dotenv()

langfuse = get_client()