import openai
import gspread
import time

# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key" ### Enter your API key

# Google Drive Folder containing images
GOOGLE_DRIVE_FOLDER_LINK = "your_google_drive_folder_link" ### Get the link using the share button

def generate_response(prompt):
    """
    Generate a response from ChatGPT for a given prompt.
    
    Parameters:
    prompt (str): The text prompt to send to ChatGPT.
    
    Returns:
    str: The generated response from ChatGPT, or an error message if the API call fails.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # ChatGPT model type
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Google Sheets Authentication using OAuth (No Service Account Required)
client = gspread.oauth()

def write_to_sheet(sheet_name, text_prompt, text_response, image_prompt, image_link):
    """
    Write a single row of data to the Google Sheet.
    
    Parameters:
    sheet_name (str): The name of the Google Sheet document.
    text_prompt (str): The text prompt used for generating the ChatGPT response.
    text_response (str): The ChatGPT-generated response.
    image_prompt (str): The description of the image.
    image_link (str): The Google Drive link to the corresponding image.
    
    Returns:
    None
    """
    sheet = client.open(sheet_name).sheet1
    sheet.append_row([text_prompt, text_response, image_prompt, image_link])
    time.sleep(1)  # To avoid hitting API limits

if __name__ == "__main__":
    ### EXAMPLE TEXT AND IMAGE PROMPTS
    text_prompts = [
        "What is the capital of France?",
        "Explain quantum mechanics in simple terms.",
        "Give me a Python script to sort a list.",
    ]

    image_prompts = [
        "A futuristic city at sunset.",
        "A cat wearing a space suit on Mars.",
        "A medieval castle in the mountains."
    ]
    
    for text_prompt in text_prompts:
        for i, image_prompt in enumerate(image_prompts):
            image_link = f"{GOOGLE_DRIVE_FOLDER_LINK}/{i+1}.jpg"  # Images are named 1.jpg, 2.jpg, etc for eas of use.
            text_response = generate_response(text_prompt)
            write_to_sheet("ChatGPT Responses", text_prompt, text_response, image_prompt, image_link)

    # Print when everything is done.
    print("All responses and image links saved to Google Sheet.")
