#Console program that takes in an optional model name and use the stdin as the prompt to estimate the token length

import tiktoken
import argparse
import sys

def estimate_token_length(prompt: str, model: str = "gpt-4o-mini") -> int:
    # Initialize the encoder
    # encoding = tiktoken.encoding_for_model(model)
    
    try:
        # Initialize the encoder
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        raise ValueError(f"Model '{model}' is not recognized. Please use a valid model name.")
    
    # Encode the prompt to get the list of tokens
    tokens = encoding.encode(prompt)
    
    # Return the number of tokens
    return len(tokens)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Estimate token length of a prompt.")
    parser.add_argument('-m', '--model', type=str, default="gpt-4o-mini", help="Model name to use for encoding")
    args = parser.parse_args()
    
    # Read prompt from stdin
    prompt = sys.stdin.read().strip()
    
    # print (f"Prompt: {prompt}\n\n")
    
    # Estimate token length
    token_length = estimate_token_length(prompt, args.model)
    
    # Print the result, formatting token_length into a number like 1,234,000
    print(f"Token length: {token_length:,}")

if __name__ == "__main__":
    main()
