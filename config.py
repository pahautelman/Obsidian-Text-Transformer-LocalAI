# Model and Temperature Configuration
MODEL = 'mistral-small:24b' # The name of the language model to use 
TEMPERATURE = 0.05 # The temperature value for controlling randomness in the model's output

# API URL
MODEL_API_URL = 'http://localhost:11434/api/chat' # The URL of the API endpoint for Ollama

# Configuration
MAX_FILE_SIZE = 999 * 1000 # The maximum file size (in bytes) for processing
MIN_FILE_SIZE = 300 # The minimum file size (in bytes) for processing

# File and Directory Paths
DIRECTORY_PATH = r'/Users/phautelman/Projects/open-webui-rag/open webui obsidian reformat/input' # The directory containing the input files

OUTPUT_FOLDER = r'/Users/phautelman/Projects/open-webui-rag/open webui obsidian reformat/output' # The directory where the processed output files will be saved
#  **********************************************************
#  WARNING:  RUNNING THIS SCRIPT WILL DELETE THE OUTPUT FOLDER!
#  ********************************************************** 


# Log File Configuration
LOG_DIRECTORY = 'logs' # The directory where log files will be stored
PROCESS_LOG_FILE = 'process_log.txt' # The name of the file for logging processing details
ERROR_LOG_FILE = 'process_errors_log.txt' # The name of the file for logging errors

# Prompt Configuration
PROMPTS_CONFIG_FILE = 'prompts_config.json' # The name of the JSON file containing the prompts configuration