"""Constants for Azure AI Foundry TTS integration."""

DOMAIN = "azure_aifoundry_tts"
PLATFORMS = ["tts"]

# Configuration keys
CONF_API_KEY = "api_key"
CONF_ENDPOINT = "endpoint"
CONF_DEPLOYMENT_ID = "deployment_id"
CONF_VOICE = "voice"
CONF_INSTRUCTIONS = "instructions"
CONF_LANGUAGE = "language"
CONF_PLAYBACK_SPEED = "playback_speed"
CONF_MODEL = "model"
CONF_AUDIO_OUTPUT = "audio_output"
CONF_STREAM_FORMAT = "stream_format"

# Default settings
DEFAULT_VOICE = "sage"
DEFAULT_LANGUAGE = "en"
DEFAULT_PLAYBACK_SPEED = 1.0
DEFAULT_MODEL = "gpt-4o-mini-tts"
DEFAULT_AUDIO_OUTPUT = "mp3"
DEFAULT_STREAM_FORMAT = "audio"
DEFAULT_ENDPOINT = "https://your-resource-name.inference.ai.azure.com"

# Default multi-field instruction settings
DEFAULT_AFFECT = (
    "A cheerful guide who delivers speech in a lively and engaging manner, "
    "tailoring pronunciation clearly for the listener."
)
DEFAULT_TONE = "A conversational, friendly tone suitable for general-purpose speech."
DEFAULT_PRONUNCIATION = "Use standard pronunciation for the language of the message."
DEFAULT_PAUSE = "Insert brief, natural pauses between sentences."
DEFAULT_EMOTION = (
    "Subtly expressive; match the content’s sentiment without over‑acting."
)

# Available voices for Azure AI Foundry
AZURE_TTS_VOICES = [
    "alloy",
    "ash",
    "ballad",
    "coral",
    "echo",
    "fable",
    "onyx",
    "nova",
    "sage",
    "shimmer",
]

# Supported models and formats - can be expanded with any model available on Azure AI Foundry
AZURE_TTS_MODELS = ["tts-1", "tts-1-hd", "gpt-4o-mini-tts"]
AZURE_AUDIO_FORMATS = ["mp3", "opus", "aac", "flac", "wav", "pcm"]
AZURE_STREAM_FORMATS = ["audio", "sse"]

# Full Whisper‑level language support (ISO‑639‑1 codes)
SUPPORTED_LANGUAGES = [
    "af",
    "ar",
    "hy",
    "az",
    "be",
    "bs",
    "bg",
    "ca",
    "zh",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "et",
    "fi",
    "fr",
    "gl",
    "de",
    "el",
    "he",
    "hi",
    "hu",
    "is",
    "id",
    "it",
    "ja",
    "kn",
    "kk",
    "ko",
    "lv",
    "lt",
    "mk",
    "ms",
    "mr",
    "mi",
    "ne",
    "no",
    "fa",
    "pl",
    "pt",
    "ro",
    "ru",
    "sr",
    "sk",
    "sl",
    "es",
    "sw",
    "sv",
    "tl",
    "ta",
    "th",
    "tr",
    "uk",
    "ur",
    "vi",
    "cy",
]
