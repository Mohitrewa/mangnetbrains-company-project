# backend/__init__.py

import logging

# Configure global logging settings for the project
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logging.info("Backend project initialized.")
