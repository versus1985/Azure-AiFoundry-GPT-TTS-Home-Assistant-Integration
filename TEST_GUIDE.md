# Guida ai test - Azure AI Foundry TTS Integration

## Test Unitari

### Ambiente di test
- Windows 10/11
- Python 3.8+ in ambiente virtuale
- pytest, pytest-asyncio

### Procedura per test unitari

1. Clona il repository:
   ```
   git clone https://github.com/versus1985/Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration.git
   ```

2. Crea e attiva un ambiente virtuale:
   ```
   cd Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration
   python -m venv test_venv
   .\test_venv\Scripts\Activate
   ```

3. Installa le dipendenze:
   ```
   pip install pytest pytest-asyncio aiohttp
   ```

4. Esegui i test:
   ```
   pytest -xvs tests/
   ```
   
   Oppure esegui test specifici:
   ```
   pytest -xvs tests/test_gpt4o_client.py
   pytest -xvs tests/test_config_flow.py
   pytest -xvs tests/test_tts_provider.py
   pytest -xvs tests/test_update_listener.py
   ```

### Risultati dei test unitari

- test_gpt4o_client.py: ✓ Tutti i test passati
- test_config_flow.py: ✓ Tutti i test passati
- test_tts_provider.py: ✓ Tutti i test passati
- test_update_listener.py: ✓ Tutti i test passati

## Test di Integrazione con Home Assistant

### Prerequisiti
- Windows 10/11
- Docker Desktop installato e funzionante

### Procedura per test di integrazione con Docker Compose (raccomandato)

1. Crea una directory per il test e accedi a essa:
   ```
   mkdir -p C:\test-homeassistant
   cd C:\test-homeassistant
   ```

2. Crea un file docker-compose.yml:
   ```yaml
   version: '3'
   
   services:
     homeassistant:
       container_name: homeassistant
       image: ghcr.io/home-assistant/home-assistant:stable
       volumes:
         - ./config:/config
       ports:
         - 8123:8123
       restart: unless-stopped
       environment:
         - TZ=Europe/Rome
   ```

3. Avvia Home Assistant:
   ```
   docker-compose up -d
   ```

4. Crea la struttura per i componenti personalizzati:
   ```
   mkdir -p config\custom_components
   ```

5. Installa il componente Azure AI Foundry TTS:
   ```powershell
   $SourcePath = "C:\SW\github\Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration\custom_components\azure_aifoundry_tts"
   $DestPath = "C:\test-homeassistant\config\custom_components\azure_aifoundry_tts"
   
   # Crea la directory di destinazione se non esiste
   if (-not (Test-Path -Path $DestPath)) {
       New-Item -Path $DestPath -ItemType Directory
   }
   
   # Copia tutti i file del componente
   Copy-Item -Path "$SourcePath\*" -Destination $DestPath -Recurse -Force
   
   # Riavvia Home Assistant
   docker-compose restart
   ```

### Procedura alternativa con Docker singolo

1. Crea una directory per i dati di Home Assistant:
   ```
   mkdir -p C:\test-homeassistant\config
   ```

2. Avvia Home Assistant in Docker:
   ```
   docker run -d --name=homeassistant `
     --restart=unless-stopped `
     -v C:\test-homeassistant\config:/config `
     -p 8123:8123 `
     ghcr.io/home-assistant/home-assistant:stable
   ```

3. Installa il componente Azure AI Foundry TTS:
   ```
   $SourcePath = "C:\SW\github\Azure-AiFoundry-GPT-TTS-Home-Assistant-Integration\custom_components\azure_aifoundry_tts"
   $DestPath = "C:\test-homeassistant\config\custom_components\azure_aifoundry_tts"
   
   # Copia tutti i file del componente
   Copy-Item -Path "$SourcePath\*" -Destination $DestPath -Recurse -Force
   
   # Riavvia Home Assistant
   docker restart homeassistant
   ```

### Configurazione e test dell'integrazione

1. Configura l'integrazione:
   - Accedi all'interfaccia web di Home Assistant all'indirizzo http://localhost:8123
   - Vai a Impostazioni → Dispositivi e servizi → Aggiungi integrazione
   - Cerca "Azure AI Foundry TTS" e segui la procedura guidata di configurazione
   - Inserisci la tua chiave API di Azure AI Foundry, l'endpoint e il deployment ID

2. Testa il servizio TTS:
   - Vai a Strumenti di sviluppo → Servizi
   - Trova il servizio `tts.azure_aifoundry_tts_say`
   - Inserisci un messaggio di test e chiama il servizio
   - Verifica che l'audio venga generato e riprodotto correttamente

3. Configura l'integrazione con Home Assistant Assist:
   - Vai a Impostazioni → Voice Assistants → Assist
   - Sotto "Text-to-Speech", seleziona "Azure AI Foundry TTS"
   - Scegli la voce desiderata e salva

### Configurazioni testate

- **Voce**: sage, nova, onyx
- **Velocità di riproduzione**: 0.8, 1.0, 1.2
- **Formato audio**: mp3, wav
- **Formato stream**: audio, sse

### Problemi noti e soluzioni

1. **Problema**: Errore "401 Unauthorized" durante la connessione all'API.
   **Soluzione**: Verifica che la chiave API sia corretta e che il formato dell'header di autenticazione sia `api-key: {key}`.

2. **Problema**: Errore "404 Not Found" quando si tenta di accedere all'endpoint.
   **Soluzione**: Assicurati che il formato dell'endpoint sia corretto (https://your-resource-name.inference.ai.azure.com) e che il deployment ID esista.

3. **Problema**: Home Assistant non riconosce il componente.
   **Soluzione**: Verifica che i file siano stati copiati nella directory corretta e che Home Assistant sia stato riavviato dopo l'installazione del componente.

4. **Problema**: Home Assistant Core non funziona direttamente su Windows.
   **Soluzione**: Usa Docker o Docker Compose come descritto in questa guida.

## Note aggiuntive per l'ambiente Windows

Home Assistant Core (`hass`) non supporta direttamente Windows (supporta solo Linux, macOS e Windows tramite WSL). Per testare l'integrazione su Windows, è consigliabile utilizzare Docker Desktop come descritto in questa guida.

Se preferisci utilizzare WSL, puoi seguire la [documentazione ufficiale](https://www.home-assistant.io/installation/windows) per l'installazione di Home Assistant su Windows tramite WSL.

## Conclusione

L'integrazione Azure AI Foundry TTS è stata testata con successo sia attraverso test unitari che attraverso test di integrazione con Home Assistant in Docker. Tutti i test sono stati superati, dimostrando che l'integrazione funziona correttamente e può essere utilizzata in ambienti di produzione.

## Prossimi Passi

- Creare una release ufficiale del componente
- Aggiungere il componente al repository HACS
- Aggiornare il README principale del progetto con informazioni sulla migrazione da OpenAI ad Azure AI Foundry