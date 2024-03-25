# TinyLLamaFarmer
**CURRENTLY IN TESTING AND DOCUMENTATION, SO PLEASE DO NOT USE THIS WALKTHROUGH YET!**

An on-device local, off-the-grid, Natural Farming AI Agriculture Assistant, to democratize access to farming knowledge where it's needed the most.

Created by Caleb DeLeeuw, as a submission to BackDropBuild Hackathon and working for Copyleft Cultivars, a nonprofit.

Currently only available on Samsung Galaxy S23 series, and some other Smartphones with Snapdragon 8 Gen 2 chip, as well as possibly working on any other device on which MLC LLM's MLC Chat Demo APK runs.

We welcome contributions, PRs, and comments. We also encourage you to reach out to copyleftcultivars@gmail.com

Consider supporting Copyleft Cultivars, a nonprofit, through Patreon. [LINK]

## Setting Up MLC Chat with Copyleftcultivars/Gemma2B-NaturalFarmerV3 on Samsung Galaxy S23

This guide will walk you through installing the MLC Chat demo app and replacing the pre-loaded Gemma2B model with the Copyleftcultivars/Gemma2B-NaturalFarmerV3 model from Hugging Face Hub (GGUF format) on your Samsung Galaxy S23.

**Requirements:**

* Samsung Galaxy S23 with Snapdragon 8 Gen 2 chip
* Computer with internet access

**Software:**

* MLC Chat Demo APK (for Samsung S23) - Download link will be on MLC website: llm.mlc.ai
* Hugging Face account (free) - Hugging Face Account: [https://huggingface.co/join](https://huggingface.co/join)

**Part 1: Downloading the MLC Chat Demo APK and Gemma2B-NaturalFarmerV3 Model**

1. **Download MLC Chat Demo APK:** Visit the MLC LLM website ([https://github.com/mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm)) and navigate to the "Demos" section. Download the MLC Chat Demo APK specifically designed for Samsung S23 with Snapdragon 8 Gen 2 chip.

2. **Download Gemma2B-NaturalFarmerV3 Model:**
    * Go to Hugging Face Hub (Hugging Face Account: [https://huggingface.co/join](https://huggingface.co/join)) and sign in or create a free account.
    * Search for the model named "Copyleftcultivars/Gemma2B-NaturalFarmerV3".
    * Click on the model name and navigate to the "Files & Versions" tab.
    * Download the model file in MLC LLM specific format (ensure it's compatible with MLC LLM).

**Part 2: Sideloading the MLC Chat Demo APK (Android requires enabling unknown sources)**

1. **Enable Unknown Sources:** On your Galaxy S23, go to Settings > Security. Locate the option "Unknown Sources" and enable it (**Warning:** Only download APKs from trusted sources like MLC LLM).

2. **Transfer the APK:** Transfer the downloaded MLC Chat Demo APK from your computer to your Galaxy S23. You can use a cable connection or cloud storage services.

3. **Install the APK:** Locate the downloaded APK on your phone's file manager app. Tap on the APK file and follow the on-screen instructions to complete the installation.

**Part 3: Replacing Pre-loaded Gemma2B with Copyleftcultivars/Gemma2B-NaturalFarmerV3**

** (This part requires some technical knowledge)**

1. **Identify Model Storage Location:** 
 Unfortunately, the current MLC Chat demo doesn't have a built-in model management feature yet. You'll need to locate the directory where the pre-loaded Gemma2B model is stored on your phone.

[STEPS TO LOCATE DIRECTORY IN SAMSUNG GALAXY S23 ULTRA]

 Refer to the MLC LLM documentation ([https://llm.mlc.ai/](https://llm.mlc.ai/)) for troubleshooting tips on finding model storage locations. It might involve using file explorer apps that can access system directories.

2. **Backup Existing Model (Optional):** It's recommended to create a backup copy of the existing Gemma2B model files before replacing them. 

3. **Copy Downloaded Model:** Copy the downloaded Copyleftcultivars/Gemma2B-NaturalFarmerV3 model (GGUF format) to the same directory where you found the pre-loaded Gemma2B model files.

4. **Verify Model Replacement:** Launch the MLC Chat app. There currently isn't a visual indicator within the app to confirm the model swap. The Model will show up on the list as the Gemma2B model, or may show the specific "NaturalFarmer" name. However, you can try interacting with the chat and see if the responses differ from the pre-loaded Gemma2B. A good test question is to explain IMO in the context of growing corn. If it answers regarding Indigenous Micro-Organisms, then you are successful and this is the correct Natural Farmer model. Good job! Enjoy!

**Important Notes:**

* This process involves modifying system files and might not be officially supported by MLC LLM. Proceed with caution and at your own risk.
* Ensure the downloaded Copyleftcultivars/Gemma2B-NaturalFarmerV3 model is compatible with MLC LLM's format requirements. Incompatible models might not function correctly.
* The MLC Chat app is still under development, and this method might change in future updates with official model management features.

For troubleshooting or further assistance, refer to the MLC LLM documentation and GitHub repository ([https://github.com/mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm)) for support resources.
