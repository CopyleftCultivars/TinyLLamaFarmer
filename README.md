# TinyLLamaFarmer

![image](https://github.com/user-attachments/assets/7e82feec-44c5-401d-b1f2-c54fba6c02f9)

// 5/4/24: Currently updated models are in alpha testing as of 5/4/24 //

// 10/29/24: Models have reached beta testing and third party review. Additional models can be seen on your org hugging face hub /copyleftcultivars //

An on-device local, off-the-grid, Natural Farming AI Agriculture Assistant, to democratize access to farming knowledge where it's needed the most.

Created by Caleb DeLeeuw, as a submission to BackDropBuild Hackathon and working for Copyleft Cultivars, a nonprofit.

Webapp in the repo is a related Natural Farming Chat webapp, designed to run on hugging face spaces or similar docker based webapp platform, which has great UI for mobile use and may be more easily deployable for some contexts.

On-device as detailed below is currently only available on Samsung Galaxy S23 series, and some other Smartphones with Snapdragon 8 Gen 2 chip, as well as possibly working on any other device on which MLC LLM's MLC Chat Demo APK runs.

We welcome contributions, PRs, and comments. We also encourage you to reach out to copyleftcultivars@gmail.com

Consider supporting Copyleft Cultivars, a nonprofit, through Patreon. [LINK]

# Setting Up llama.cpp with Copyleftcultivars/Gemma2B-NaturalFarmerV3 on Android

=This guide will walk you through installing llama.cpp and running the Copyleftcultivars/Gemma2B-NaturalFarmerV3 model from Hugging Face Hub on your Android device.

## Requirements:

- Android device with at least 6GB RAM (8GB+ recommended)
- At least 4GB free storage space
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

## Part 2: Downloading the Gemma2B-NaturalFarmerV3 Model

1. Go to Hugging Face Hub (https://huggingface.co/join) and sign in or create a free account.
2. Search for the model named "Copyleftcultivars/Gemma2B-NaturalFarmerV3"
3. Click on the model name and navigate to the "Files & Versions" tab
4. Download the GGUF version of the model

If downloading directly through Termux:
```bash
cd ~/llama.cpp/models
wget [GGUF_MODEL_URL]
```

## Part 3: Running the Model

1. Basic setup to run the model:
```bash
cd ~/llama.cpp
./main -m models/gemma2b-naturalfarmer.gguf --temp 0.7 --ctx-size 2048 --threads 4
```

2. For interactive chat mode:
```bash
./main -m models/gemma2b-naturalfarmer.gguf --temp 0.7 --ctx-size 2048 --threads 4 --interactive
```

## Verify Model Installation

Launch the interactive mode and test the model by asking about IMO in the context of growing corn. If it answers regarding Indigenous Micro-Organisms, then you have successfully installed the correct Natural Farmer model. Good job! Enjoy!

Example test prompt:
```
What is IMO in the context of growing corn?
```

## Important Notes:

- This process is officially supported by llama.cpp and is regularly tested on Android devices
- Monitor your device's temperature during extended use
- Consider using a cooling solution for longer sessions
- Keep your device plugged in when running the model
- The model may take a few seconds to load and respond, depending on your device's capabilities

## Optimizing Performance

If you experience slow performance or memory issues:

1. Try adjusting these parameters:
```bash
--threads 2        # Reduce thread count
--ctx-size 1024    # Reduce context size
--batch-size 512   # Adjust batch size
```

2. Quantize the model for better performance:
```bash
./quantize models/original-model.gguf models/quantized-model.gguf q4_k_m
```

## Advanced Usage: Setting Up a Local Web Interface

1. Build the server:
```bash
make server
```

2. Run the web interface:
```bash
./server -m models/gemma2b-naturalfarmer.gguf --host 0.0.0.0 --port 8080
```

3. Access through your browser at `http://localhost:8080`

## Troubleshooting

- If you encounter permission errors, run: `chmod +x main`
- For memory errors, try a more aggressive quantization format
- If the model loads but runs slowly, adjust the number of threads
- For storage issues, ensure you have at least 4GB free space

For troubleshooting or further assistance, you can:
1. Check the llama.cpp GitHub repository
2. Join the llama.cpp Discord community
3. Email CopyleftCultivars@gmail.com with questions about the model specifically

Consider supporting Copyleft Cultivars, a nonprofit, through our Patreon if you find this model useful. Our Patreon Supporter make this and many other projects possible! Thanks!
