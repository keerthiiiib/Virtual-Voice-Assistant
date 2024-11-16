from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_response(prompt, max_length=100):
    """
    Generates a response using GPT-2.
    :param prompt: The user input as a string.
    :param max_length: The maximum length of the generated response.
    :return: Generated response as a string.
    """
    try:
        # Encode the input prompt
        inputs = tokenizer.encode(prompt, return_tensors="pt")

        # Generate a response
        outputs = model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )

        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response[len(prompt):].strip()  # Exclude the prompt from the response
    except Exception as e:
        return "Sorry, I couldn't process that right now. Please try again later."
