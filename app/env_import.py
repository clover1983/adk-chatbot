import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

# PROXY = os.environ.get("PROXY")
# NO_PROXY =os.environ.get("NO_PROXY")

os.environ["DISABLE_AIOHTTP_TRANSPORT"] = "True"
# os.environ["OTEL_SDK_DISABLED"] = "True"
# os.environ["AIOHTTP_TRUST_ENV"] = "True"
# os.environ["http_proxy"] = PROXY
# os.environ["https_proxy"] = PROXY
# os.environ["no_proxy"] = NO_PROXY 
# os.environ["HTTP_PROXY"] = PROXY
# os.environ["HTTPS_PROXY"] = PROXY
# os.environ["NO_PROXY"] = NO_PROXY


API_KEY = os.environ.get("API_KEY")

