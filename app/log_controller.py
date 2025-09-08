import logging

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO, 
                    filename='adk-chatbot.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    force=True)
logging.getLogger("httpx").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
logging.getLogger("opentelemetry").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)