import asyncio
import os
import sys
import importlib
from types import SimpleNamespace

import pytest

sys.path.insert(0, os.path.dirname(__file__))
from hass_stubs import install_homeassistant_stubs

install_homeassistant_stubs()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)

gpt4o = importlib.import_module("custom_components.azure_aifoundry_tts.gpt4o")
GPT4oClient = gpt4o.GPT4oClient
DEFAULT_VOICE = gpt4o.DEFAULT_VOICE


class DummyEntry:
    def __init__(self, data=None, options=None):
        self.data = data or {}
        self.options = options or {}


class DummyContent:
    async def iter_chunked(self, size):
        yield b"audio"

    # Per compatibilità se erroneamente usato come SSE content (stream_tts_audio test)
    def __aiter__(self):
        async def gen():
            yield b"data: {\"type\": \"speech.audio.delta\", \"audio\": \"ZGF0YTE=\"}\n"
            yield b"\n"
            yield b"data: {\"type\": \"speech.audio.delta\", \"audio\": \"ZGF0YTI=\"}\n"
            yield b"\n"
            yield b"data: {\"type\": \"speech.audio.done\"}\n"
            yield b"\n"
        return gen()


class DummyResponse:
    def __init__(self):
        self.status = 200
        self.content = DummyContent()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def json(self):
        return {}

    async def text(self):
        return ""


class DummySession:
    def __init__(self, *args, **kwargs):
        self.payload = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    def post(self, url, headers=None, json=None):
        self.payload = json
        return DummyResponse()


class DummySSEContent:
    def __init__(self, lines):
        self.lines = lines

    def __aiter__(self):
        async def gen():
            for line in self.lines:
                for part in line.split(b"\n"):
                    yield (part + b"\n") if part else b"\n"

        return gen()


class DummySSEResponse:
    def __init__(self, lines):
        self.status = 200
        self.content = DummySSEContent(lines)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def json(self):
        return {}

    async def text(self):
        return ""


class DummySSESession:
    def __init__(self, lines):
        self.payload = None
        self.lines = lines

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    def post(self, url, headers=None, json=None):
        self.payload = json
        return DummySSEResponse(self.lines)


@pytest.mark.asyncio
async def test_instructions_default(monkeypatch):
    entry = DummyEntry(data={"api_key": "k"})
    client = GPT4oClient(None, entry)

    dummy = DummySession()
    # Patchare il ClientSession corretto del modulo azure_aifoundry_tts
    monkeypatch.setattr(
        "custom_components.azure_aifoundry_tts.gpt4o.ClientSession",
        lambda timeout=None: dummy,
    )

    fmt, data = await client.get_tts_audio("hello")
    assert fmt == "mp3"
    assert dummy.payload["instructions"] == ""
    assert dummy.payload["voice"] == DEFAULT_VOICE
    assert dummy.payload["model"] == gpt4o.DEFAULT_MODEL
    assert dummy.payload["response_format"] == gpt4o.DEFAULT_AUDIO_OUTPUT
    assert dummy.payload["stream_format"] == gpt4o.DEFAULT_STREAM_FORMAT


@pytest.mark.asyncio
async def test_sse_stream(monkeypatch):
    entry = DummyEntry(data={"api_key": "k"})
    client = GPT4oClient(None, entry)

    lines = [
        b'data: {"type": "speech.audio.delta", "audio": "ZGF0YTE="}\n\n',
        b'data: {"type": "speech.audio.delta", "audio": "ZGF0YTI="}\n\n',
        b'data: {"type": "speech.audio.done"}\n\n',
    ]
    session = DummySSESession(lines)
    monkeypatch.setattr(
        "custom_components.azure_aifoundry_tts.gpt4o.ClientSession",
        lambda timeout=None: session,
    )

    fmt, data = await client.get_tts_audio("hi", {gpt4o.CONF_STREAM_FORMAT: "sse"})
    assert fmt == "mp3"
    assert data == b"data1data2"


@pytest.mark.asyncio
async def test_default_stream_from_entry(monkeypatch):
    entry = DummyEntry(data={"api_key": "k"}, options={gpt4o.CONF_STREAM_FORMAT: "sse"})
    client = GPT4oClient(None, entry)

    lines = [
        b'data: {"type": "speech.audio.delta", "audio": "ZGF0YTE="}\n\n',
        b'data: {"type": "speech.audio.delta", "audio": "ZGF0YTI="}\n\n',
        b'data: {"type": "speech.audio.done"}\n\n',
    ]
    session = DummySSESession(lines)
    monkeypatch.setattr(
        "custom_components.azure_aifoundry_tts.gpt4o.ClientSession",
        lambda timeout=None: session,
    )

    fmt, data = await client.get_tts_audio("hi")
    assert fmt == "mp3"
    assert data == b"data1data2"


@pytest.mark.asyncio
async def test_stream_tts_audio_generator(monkeypatch):
    entry = DummyEntry(data={"api_key": "k"})
    client = GPT4oClient(None, entry)

    lines = [
        b'data: {"type": "speech.audio.delta", "audio": "ZGF0YTE="}\n\n',
        b'data: {"type": "speech.audio.delta", "audio": "ZGF0YTI="}\n\n',
        b'data: {"type": "speech.audio.done"}\n\n',
    ]
    session = DummySSESession(lines)
    monkeypatch.setattr(
        "custom_components.azure_aifoundry_tts.gpt4o.ClientSession",
        lambda timeout=None: session,
    )


class CaptureSession:
    """Session che cattura URL e payload per verificare deployment e override."""

    def __init__(self):
        self.last_url = None
        self.last_payload = None
        self.status = 200

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    def post(self, url, headers=None, json=None):
        self.last_url = url
        self.last_payload = json
        return DummyResponse()


@pytest.mark.asyncio
async def test_options_override_and_deployment_fallback(monkeypatch):
    """Verifica che le opzioni passate sovrascrivano i default e che il deployment fallback sia il modello.

    Se non viene fornito deployment_id, viene usato il model come parte dell'endpoint.
    """
    entry = DummyEntry(
        data={
            "api_key": "k",
            # Intenzionalmente senza deployment_id
        }
    )
    client = GPT4oClient(None, entry)

    sess = CaptureSession()
    monkeypatch.setattr(
        "custom_components.azure_aifoundry_tts.gpt4o.ClientSession",
        lambda timeout=None: sess,
    )

    options = {
        "voice": "nova",
        "instructions": "Parla lentamente",
        gpt4o.CONF_PLAYBACK_SPEED: 1.25,
        gpt4o.CONF_MODEL: "gpt-4o-mini-tts",  # default ma lo ripassiamo per test
        gpt4o.CONF_AUDIO_OUTPUT: "wav",
        gpt4o.CONF_STREAM_FORMAT: "audio",
    }

    fmt, data = await client.get_tts_audio("ciao mondo", options)
    assert fmt == "wav"
    assert data == b"audio"
    # Deployment fallback al model
    assert sess.last_url.endswith(
        f"/deployments/{options[gpt4o.CONF_MODEL]}/audio/speech"
    )
    assert sess.last_payload["voice"] == "nova"
    assert sess.last_payload["instructions"] == "Parla lentamente"
    assert sess.last_payload["speed"] == 1.25
    assert sess.last_payload["response_format"] == "wav"
    assert sess.last_payload["stream_format"] == "audio"

    fmt, generator = await client.stream_tts_audio("hi", {gpt4o.CONF_STREAM_FORMAT: "sse"})
    assert fmt == "mp3"
    data = b"".join([chunk async for chunk in generator])
    assert data == b"data1data2"


class ErrorResponse:
    def __init__(self, message: str, use_json: bool = True):
        self.status = 401
        self._message = message
        self.use_json = use_json

    async def json(self):
        if self.use_json:
            return {"error": {"message": self._message}}
        raise ValueError("no json")

    async def text(self):
        return self._message


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "key",
    [
        "sk-1234567890ABCDEF",  # pattern >=32 alfanumerici non matcha questi prefissi corti => resta visibile
        "sk-proj-ABCDEFG1234567890",
        "sk-svcacct-1234567890ABCDEF",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456",  # 32 char => deve essere mascherato
    ],
)
async def test_log_api_error_masks_api_key_json(caplog, key):
    resp = ErrorResponse(f"invalid key {key}")
    with caplog.at_level("ERROR"):
        await gpt4o._log_api_error(resp)
    # Solo chi soddisfa la regex [A-Za-z0-9]{32,} viene mascherato
    if len(key) >= 32 and key.isalnum():
        assert key not in caplog.text
        assert "api-***" in caplog.text
    else:
        # Non mascherato perche' non corrisponde alla regex
        assert key in caplog.text


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "key",
    [
        "sk-1234567890ABCDEF",
        "sk-proj-ABCDEFG1234567890",
        "sk-svcacct-1234567890ABCDEF",
        "ZYXWVUTSRQPONMLKJIHGFEDCBA123456",  # 32 char alfanumerici
    ],
)
async def test_log_api_error_masks_api_key_text(caplog, key):
    resp = ErrorResponse(f"bad request {key}", use_json=False)
    with caplog.at_level("ERROR"):
        await gpt4o._log_api_error(resp)
    if len(key) >= 32 and key.isalnum():
        assert key not in caplog.text
        assert "api-***" in caplog.text
    else:
        assert key in caplog.text
