#!/usr/bin/env python3

# Copyright (c) 2021, Jonathan AW

import pymupdf4llm
import pathlib
import argparse
import sys


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Retrieve your document content in Markdown and store as UTF8-encoded file.")
    parser.add_argument('-i', '--inputFile', type=str, help="Input file name")
    parser.add_argument('-o', '--outputFile', type=str, help="Output file name")
    args = parser.parse_args()

    if args.inputFile is None or args.inputFile == "":
        return

    if not pathlib.Path(args.inputFile).is_file():
        print("Error: Input file does not exist.")
        return

    if args.outputFile is None or args.outputFile == "":
        output_file = pathlib.Path(args.inputFile).stem + ".md"
    else:
        output_file = args.outputFile

    # Convert PDF to Markdown
    md_text = pymupdf4llm.to_markdown(args.inputFile)

    # Write Markdown content to output file
    pathlib.Path(output_file).write_bytes(md_text.encode())
    
    print(f"Markdown content saved to {output_file}")

if __name__ == "__main__":
    main()
