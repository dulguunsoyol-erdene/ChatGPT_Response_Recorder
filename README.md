# ChatGPT_Response_Recorder

## Description
This Python script automates the process of generating text responses using OpenAI's ChatGPT for a list of text prompts, pairing each response with an image from a Google Drive folder, and saving the results in a Google Sheet. The code was created for analysing the accuracy of ChatGPT's responses given different types of prompts.

## Features
- Iterates through a list of text prompts.
- Matches each text prompt with multiple images from a Google Drive folder.
- Uses OpenAI's ChatGPT to generate responses.
- Stores the text prompt, AI-generated response, image description, and image link in a Google Sheet.
- Uses Google Sheets OAuth authentication for easy access without a service account.

## Prerequisites
### 1. Install Required Python Libraries
Ensure you have the following Python packages installed:
```sh
pip install openai gspread oauth2client
```

### 2. Set Up OpenAI API Key
Replace the placeholder in the script:
```python
OPENAI_API_KEY = "your_openai_api_key"
```

### 3. Authenticate Google Sheets
- Ensure your Google Sheet is set to **"Anyone with the link can edit"**.
- Run the script once to trigger OAuth authentication in the browser.

## Input
- **Text Prompts**: A list of text-based questions or requests for ChatGPT.
- **Image Prompts**: A list of image descriptions paired with Google Drive image links.
- **Google Drive Folder**: A folder containing images accessible via public links.
- **Google Sheet**: A spreadsheet where results will be stored.

## Output
The script writes the following data to the Google Sheet:
| Text Prompt | AI Response | Image Description | Image Link |
|-------------|------------|-------------------|------------|
| Prompt 1    | Response 1 | Image 1 Desc      | Image 1 URL|
| Prompt 1    | Response 1 | Image 2 Desc      | Image 2 URL|
| Prompt 2    | Response 2 | Image 1 Desc      | Image 1 URL|

## Execution
Run the script using:
```sh
python script.py
```
The script will iterate through all text prompts and match each with all images before moving to the next prompt. Results will be appended to the Google Sheet.

## Notes
- Ensure the Google Sheet exists before running the script.
- The script assumes images are named numerically (e.g., 1.jpg, 2.jpg).
- To avoid API rate limits, a delay is added when writing to Google Sheets.
