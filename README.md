# Azure AI Foundry 🎤 About Azure AI 🚀 Features  

✅ **Uses Azure AI Foundry** for sec## 🛠️ Setup & Configuration  

1. **Go to:** Settings → Devices & Services → Integrations.  
2. **Click "+ Add Integration"** → Select **Azure AI Foundry TTS**.  
3. **Enter your Azure AI Foundry API Key.**  
4. **Enter your Azure AI Foundry Endpoint URL** (e.g., `https://your-resource-name.inference.ai.azure.com`).
5. **Enter your Deployment ID** (the name of your TTS model deployment on Azure AI Foundry).
6. **Choose a Voice** from the dropdown (e.g., `nova`, `onyx`, `sage`).  
7. **Customise the speech settings:**  
- **Affect/Personality** (e.g., "A cheerful guide")  
- **Tone** (e.g., "Friendly, clear, and reassuring")  
- **Pronunciation** (e.g., "Clear, articulate, and steady")  
- **Pauses** (e.g., "Brief, purposeful pauses after key instructions")
- **Emotion** (e.g., "Warm and supportive")
- **Playback Speed** (e.g., `1.2` for 20% faster)
- **Model** (e.g., `gpt-4o-mini-tts` - this is overridden by your deployment)
- **Audio Format** (e.g., `mp3`, `wav`)
- **Stream Format** – choose `sse` to stream audio while it is generated or `audio` to wait for the full file
8. Click **Submit**. 🎉 Done!eady AI models  
✅ **Deploy any TTS model** available on your Azure AI Foundry resource  
✅ **Fully UI-based setup**—no YAML required  
✅ **Support for multiple voices** depending on your deployment  
✅ **Customisable speech**—affect, tone, pronunciation, pauses, emotion  
✅ **Works with Home Assistant's Assist**  
✅ **Easily installable via HACS**  
✅ **Playback speed control for faster or slower speech**  
✅ **Streaming audio for quicker responses**  
✅ **Changes take effect immediately – no restart required**  
✅ **Improved error handling and logging**    

This integration connects to **Azure AI Foundry**, allowing you to use any TTS model you've deployed on your Azure AI Foundry resource.
It offers **high-quality, human-like speech** with **adjustable affect, tone, pronunciation, pauses, and emotion**.

> **Azure AI Foundry**  
> *Azure AI Foundry gives you access to frontier generative AI models in a secure, compliant, and enterprise-ready environment. You can deploy models like GPT-4o, GPT-4o mini, and others for various AI applications including text-to-speech.*

With **flexible deployment options**, you can use any TTS model available in your Azure AI Foundry instance and customize **how speech is rendered** to match different scenarios.Home Assistant Integration

**Enhance Home Assistant's voice assistant with Azure AI Foundry's powerful text-to-speech (TTS) models.**  
This integration allows you to use **any TTS model deployed to your Azure AI Foundry** resource as a speech provider in Home Assistant.

> **🗣️ Built for [Home Assistant Voice Assistants](https://www.home-assistant.io/voice_control/)**  
> This integration enables Azure AI Foundry TTS in **Assist**.I GPT-4o Mini TTS – Home Assistant Integration

**Enhance Home Assistant’s voice assistant with OpenAI’s latest natural-sounding text-to-speech (TTS) model.**  
This integration allows you to use **GPT-4o Mini TTS**, OpenAI’s newest and most expressive TTS model, as a speech provider in Home Assistant.

> **🗣️ Built for [Home Assistant Voice Assistants](https://www.home-assistant.io/voice_control/)**  
> This integration enables GPT-4o Mini TTS in **Assist**.

---

## 🎤 About GPT-4o Mini TTS  

This integration is based on **GPT-4o Mini TTS**, OpenAI’s latest TTS model.  
It offers **high-quality, human-like speech** with **adjustable affect, tone, pronunciation, pauses, and emotion**.

> **OpenAI Quote:**  
> *"Hear and play with these voices in [OpenAI.fm](https://www.OpenAI.fm), our interactive demo for trying the latest text-to-speech model in the OpenAI API. Voices are currently optimized for English."*

With **10 built-in voices**, you can customise **how speech is rendered** to match different scenarios.

---

## 🚀 Features  

✅ **Uses GPT-4o Mini TTS**, OpenAI’s latest speech model  
✅ **Fully UI-based setup**—no YAML required  
✅ **10 voices** (`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`)  
✅ **Customisable speech**—affect, tone, pronunciation, pauses, emotion  
✅ **Works with Home Assistant’s Assist**  
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
2. **Click “+ Add Integration”** → Select **OpenAI GPT-4o Mini TTS**.  
3. **Enter your OpenAI API Key.**  
4. **Choose a Voice** from the dropdown (e.g., `nova`, `onyx`, `sage`).  
5. **Customise the speech settings:**  
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


<img width="334" height="1045" alt="image" src="https://github.com/user-attachments/assets/fb6f147e-b016-4766-bcb9-f1ddeec87ffa" />


Now, Home Assistant's voice assistant will use GPT-4o Mini TTS as its **speech provider**.

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

![image](https://github.com/user-attachments/assets/6f61f299-1c51-4109-ab5b-f7b1a1e6f658)

👉 **See Home Assistant’s [Voice Control Guide](https://www.home-assistant.io/voice_control/) for setup.**  

---

## 📝 FAQ  

### **How do I get an OpenAI API Key?**  
You need an API key from OpenAI to use this integration. Get one from:  
👉 [https://platform.openai.com/signup/](https://platform.openai.com/signup/)  

### **What are the available voices?**
The integration supports the following **10 voices**:  alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer


### **Is this free to use?**  
No, **OpenAI’s API is a paid service**. You are charged per character generated. Check OpenAI’s pricing page for more details.  

---

## 🔄 Recent Updates  

Streaming mode enabled for immediate playback  
---  

## 🤝 Contributing  

Want to help improve this project? Contributions are welcome!  

1. Fork the repo  
2. Submit pull requests for features/fixes  
3. Report issues or suggest improvements  

---

## 📢 Support  

Have questions or need help?  
- **GitHub Issues:** Report problems [here](https://github.com/wifiuk/OpenAI-GPT-4o-Mini-TTS-Home-Assistant-Integration/issues)  
- **Home Assistant Forums:** Share feedback [here](https://community.home-assistant.io)  

Enjoy **human-like, expressive TTS** in Home Assistant! 🎤🔊  



