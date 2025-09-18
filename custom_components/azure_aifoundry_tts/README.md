# Azure AI Foundry TTS – Home Assistant Integration

**Enhance Home Assistant's voice assistant with Azure AI Foundry natural-sounding text-to-speech (TTS) models.**  
This integration allows you to use **Azure AI Foundry TTS models**, including GPT-4o Mini TTS, as a speech provider in Home Assistant.

> **🗣️ Built for [Home Assistant Voice Assistants](https://www.home-assistant.io/voice_control/)**  
> This integration enables Azure AI Foundry TTS in **Assist**.

---

## 🎤 About Azure AI Foundry TTS  

This integration connects to **Azure AI Foundry**, Microsoft's AI service platform that offers high-quality text-to-speech capabilities.  
It delivers **high-quality, human-like speech** with **adjustable affect, tone, pronunciation, pauses, and emotion**.

> **Note:**  
> *You need an Azure account with access to AI Foundry and a deployed TTS model to use this integration.*

With **10 built-in voices**, you can customize **how speech is rendered** to match different scenarios.

---

## 🚀 Features  

✅ **Uses Azure AI Foundry TTS models**  
✅ **Fully UI-based setup**—no YAML required  
✅ **10 voices** (`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`)  
✅ **Customizable speech**—affect, tone, pronunciation, pauses, emotion  
✅ **Works with Home Assistant's Assist**  
✅ **Easily installable via HACS**  
✅ **Playback speed control for faster or slower speech**  
✅ **Streaming audio for quicker responses**  
✅ **Changes take effect immediately – no restart required**  
✅ **Improved error handling and logging**  

---

## 🔧 Installation  

### 1️⃣ Install via HACS (Recommended)  

Since this is a **custom repository**, you must add it manually:

1. Open **HACS** in Home Assistant.  
2. Go to **Integrations** → Click the **three-dot menu** → **Custom repositories**.  
3. Add this repository:  
   [https://github.com/versus1985/Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration.git](https://github.com/versus1985/Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration.git)
4. Select **Integration** as the category and click **Add**.  
5. Click **Download** and install **Azure AI Foundry TTS**.  
6. **Restart Home Assistant** after installation.  

---

### 2️⃣ Manual Installation (Alternative)  

1. Download this repository as a **ZIP file** and extract it.  
2. Copy the `azure_aifoundry_tts` folder to:  /config/custom_components/  
3. Restart Home Assistant.  
4. Go to **Settings → Devices & Services → Add Integration**.  
5. Search for **Azure AI Foundry TTS** and follow the setup process.  

---

## 🛠️ Setup & Configuration  

1. **Go to:** Settings → Devices & Services → Integrations.  
2. **Click "+ Add Integration"** → Select **Azure AI Foundry TTS**.  
3. **Enter your Azure AI Foundry API Key, Endpoint URL, and Deployment ID.**  
4. **Choose a Voice** from the dropdown (e.g., `nova`, `onyx`, `sage`).  
5. **Customize the speech settings:**  
- **Affect/Personality** (e.g., "A cheerful guide")  
- **Tone** (e.g., "Friendly, clear, and reassuring")  
- **Pronunciation** (e.g., "Clear, articulate, and steady")  
- **Pauses** (e.g., "Brief, purposeful pauses after key instructions")
- **Emotion** (e.g., "Warm and supportive")
- **Playback Speed** (e.g., `1.2` for 20% faster)
- **Model** (e.g., `gpt-4o-mini-tts`)
- **Audio Format** (e.g., `mp3`, `wav`)
- **Stream Format** – choose `sse` to stream audio while it is generated or `audio` to wait for the full file
6. Click **Submit**. 🎉 Done!  

Now, Home Assistant's voice assistant will use Azure AI Foundry TTS as its **speech provider**.

---

## 🔊 Using Azure AI Foundry TTS in Home Assistant  

### 🔹 **Enable Azure AI Foundry TTS in Home Assistant Voice Assistants**  

Once the repo is installed, follow these steps:  

1. **Go to:** `Settings → Voice Assistants`.  
2. **Choose your assistant** (e.g., Assist).  
3. Scroll down to **Text-to-Speech** settings.  
4. **Select "Azure AI Foundry TTS" from the dropdown**.  
5. **Choose the same voice you set up earlier**    
6. **Save settings** and test voice output.

👉 **See Home Assistant's [Voice Control Guide](https://www.home-assistant.io/voice_control/) for setup.**  

---

## 📝 FAQ  

### **How do I get an Azure AI Foundry API Key?**  
You need an API key from Azure AI Foundry to use this integration:  
👉 Create an Azure AI Foundry resource in the Azure portal.
👉 Deploy a model like `gpt-4o-mini-tts`.
👉 Copy the API key and endpoint from the resource overview.

### **What are the available voices?**
The integration supports the following **10 voices**:  alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer

### **Is this free to use?**  
No, **Azure AI Foundry is a paid service**. You are charged per character generated. Check Azure's pricing page for more details.  

---

## 🔄 Recent Updates  

Migrated from OpenAI to Azure AI Foundry support
---  

## 🤝 Contributing  

Want to help improve this project? Contributions are welcome!  

1. Fork the repo  
2. Submit pull requests for features/fixes  
3. Report issues or suggest improvements  

---

## 📢 Support  

Have questions or need help?  
- **GitHub Issues:** Report problems [here](https://github.com/versus1985/Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration/issues)  
- **Home Assistant Forums:** Share feedback [here](https://community.home-assistant.io)  

Enjoy **human-like, expressive TTS** in Home Assistant! 🎤🔊  