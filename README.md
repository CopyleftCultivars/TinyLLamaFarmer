# TinyLLamaFarmer

![image](https://github.com/user-attachments/assets/7e82feec-44c5-401d-b1f2-c54fba6c02f9)

// 5/4/24: Currently updated models are in alpha testing as of 5/4/24 //

// 10/29/24: Models have reached beta testing and third party review. Additional models can be seen on your org hugging face hub /copyleftcultivars //

An on-device local, off-the-grid, Natural Farming AI Agriculture Assistant, to democratize access to farming knowledge where it's needed the most.

Created by Caleb DeLeeuw, as a submission to BackDropBuild Hackathon and working for Copyleft Cultivars, a nonprofit.

The .tsx file webapp shows examples of how the user interface in the repo can be configured, which may make it easier to implement, but which is not actually needed to get this working.

On-device as detailed below is currently only available on Samsung Galaxy S23 series, and some other Smartphones with Snapdragon 8 Gen 2 chip, as well as possibly working on any other device on which MLC LLM's MLC Chat Demo APK runs.

We welcome contributions, PRs, and comments. We also encourage you to reach out to copyleftcultivars@gmail.com

Consider supporting Copyleft Cultivars, a nonprofit, through Patreon. [LINK](https://www.patreon.com/c/CopyleftCultivarsNonprofit)

# Setting Up llama.cpp with CopyleftCultivars/llama-3.1-natural-farmer on Android

This guide will walk you through installing llama.cpp and running the new CopyleftCultivars/llama-3.1-natural-farmer model from Hugging Face Hub on your Android device.

## Requirements:

- Android device with at least 8GB RAM (12GB+ recommended)
- At least 8GB free storage space (the Q8_0 quantized model is larger than Q4 models)
- Computer with internet access (optional)

## Software:

- Termux (from F-Droid)
- Hugging Face account (free) - https://huggingface.co/join

## Part 1: Setting Up Termux and llama.cpp

1. Install F-Droid and Termux:
   - Download F-Droid from f-droid.org
   - Open F-Droid and search for "Termux"
   - Install Termux through F-Droid

2. Set up the development environment:
```bash
pkg update
pkg upgrade
pkg install git make clang
```

3. Build llama.cpp:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make LLAMA_NATIVE=1
```

## Part 2: Downloading the llama-3.1-natural-farmer Model

1. Go to Hugging Face Hub (https://huggingface.co/join) and sign in or create a free account
2. Navigate to "CopyleftCultivars/llama-3.1-natural-farmer-Q8_0-GGUF"
3. Download the GGUF model file (must be done with data or internet connection, but will stay downloaded after that until the app is fully shut down.)

If downloading directly through Termux:
```bash
cd ~/llama.cpp/models
wget [GGUF_MODEL_URL]
```

Note: This model is already quantized to Q8_0 format for optimal quality while maintaining reasonable resource usage.

## Part 3: Running the Model

1. Basic setup to run the model:
```bash
cd ~/llama.cpp
./main -m models/llama-3.1-natural-farmer-q8_0.gguf --temp 0.7 --ctx-size 4096 --threads 4
```

2. For interactive chat mode:
```bash
./main -m models/llama-3.1-natural-farmer-q8_0.gguf --temp 0.7 --ctx-size 4096 --threads 4 --interactive
```

Recommended parameters for this model:
- `--ctx-size 4096`: LLaMA 3.1 supports larger context
- `--temp 0.7`: Good balance of creativity and consistency
- `--threads 4`: Adjust based on your device
- `--repeat-penalty 1.1`: Helps prevent repetition

## Verify Model Installation

Launch the interactive mode and test the model by asking about IMO in the context of growing corn. If it answers regarding Indigenous Micro-Organisms, then you have successfully installed the correct Natural Farmer model. Good job! Enjoy!

Example test prompt:
```
What is IMO in the context of growing corn?
```

## Important Notes:

- This model is larger and may use more resources than smaller models
- The Q8_0 quantization provides high quality but requires more RAM
- Monitor your device's temperature during extended use
- Keep your device plugged in when running the model
- First response may take longer due to model size and initialization

## Optimizing Performance

If you experience performance issues:

1. Try adjusting these parameters:
```bash
--threads 2        # Reduce thread count
--ctx-size 2048    # Reduce context size if memory limited
--batch-size 512   # Adjust batch size for throughput
```

2. If still experiencing issues, you might need to try the Q4 version of the model if available

## Optional usage customization: Setting Up a Local Web Interface

1. Build the server:
```bash
make server
```

2. Run the web interface:
```bash
./server -m models/llama-3.1-natural-farmer-q8_0.gguf --host 0.0.0.0 --port 8080
```

3. Access through your browser at `http://localhost:8080`

### Advanced User Interface Options:

### (1) Basic Terminal Interface
The default terminal interface through Termux looks like this:
```
$ ./main -m models/llama-3.1-natural-farmer-q8_0.gguf --interactive
Model loaded. Interactive mode enabled.
> What is IMO in farming?
IMO (Indigenous Microorganisms) refers to beneficial microorganisms...
> _
```

### (2) Setting Up the Web Interface (Optional)

1. Build the web server:
```bash
cd ~/llama.cpp
make server
```

2. Start the server:
```bash
./server -m models/llama-3.1-natural-farmer-q8_0.gguf --host 0.0.0.0 --port 8080
```

3. Access options:
- On your phone: Open browser and go to `http://localhost:8080`
- From other devices on your network: 
  - Find your phone's IP: Run `ip addr show | grep inet` in Termux
  - Access `http://[YOUR_PHONE_IP]:8080` from any device on your network

The web interface provides:
- Chat-style message history
- Text input box with send button
- Mobile-friendly design
- Shareable access across your local network

Note: Keep Termux running and your screen on while using either interface. For extended sessions, keep your device plugged in and in a well-ventilated area.

## Troubleshooting

- If you get "out of memory" errors:
  - Reduce --ctx-size
  - Close other apps
  - Try reducing --threads
- If the model loads but runs slowly:
  - Experiment with different --threads values
  - Ensure device isn't in power saving mode
- For storage issues:
  - Need at least 8GB free space for this model
  - Consider clearing app cache/data

- If you encounter permission errors, run: `chmod +x main`
- For memory errors, try a more aggressive quantization format
- If the model loads but runs slowly, adjust the number of threads
- For storage issues, ensure you have at least 4GB free space

For troubleshooting or further assistance, you can:
1. Check the llama.cpp GitHub repository
2. Join the llama.cpp Discord community
3. Email CopyleftCultivars@gmail.com with questions about the model specifically

Consider supporting Copyleft Cultivars, a nonprofit, through our Patreon if you find this model useful. Our Patreon Supporter make this and many other projects possible! Thanks!
