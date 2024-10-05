import re

class Lexer:
    def __init__(self, code):
        self.code = code  # The input source code
        self.tokens = []  # List to hold the generated tokens

    def tokenize(self):
        # Token specifications for FSMs and other token types
        token_specification = [
            ("KEYWORD", r'\b(if|else|fi|while|return|get|put|integer|boolean|real|function)\b'),
            ("IDENTIFIER", r'[a-zA-Z][a-zA-Z0-9]*'),  # FSM for Identifiers
            ("INTEGER", r'\b\d+\b'),  # FSM for Integers
            ("REAL", r'\b\d+\.\d+\b'),  # FSM for Real numbers
            ("ASSIGN", r'='),
            ("OPERATOR", r'[+\-*/<>!]=?'),
            ("DELIMITER", r'[;{},()]'),
            ("COMMENT", r'\[\*.*?\*\]'),  # Ignore comments enclosed in [* *]
            ("WHITESPACE", r'[ \t\n]+'),  # Ignore whitespace
        ]

        # Combine token specifications into one regex pattern
        token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

        # Match each token using re.finditer
        for mo in re.finditer(token_regex, self.code):
            kind = mo.lastgroup  # Get the name of the token type
            value = mo.group()  # Get the actual lexeme
            if kind == "WHITESPACE" or kind == "COMMENT":
                continue  # Skip over whitespace and comments
            self.tokens.append((kind, value))  # Add token and lexeme to the list

        return self.tokens

# Main lexer function to read multiple files and output the tokens
def process_files(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            code = file.read()  # Read the source code
            lexer = Lexer(code)
            tokens = lexer.tokenize()  # Generate the tokens

            # Write the tokens and lexemes to an output file
            output_file_path = f"output_{file_path}"
            with open(output_file_path, 'w') as output_file:
                output_file.write(f"{'Token':<15} {'Lexeme'}\n")
                output_file.write(f"{'-'*30}\n")
                for token in tokens:
                    output_file.write(f"{token[0]:<15} {token[1]}\n")

            # Print tokens to the console
            print(f"Tokens from {file_path}:")
            for token in tokens:
                print(f"{token[0]:<15} {token[1]}")
            print("\n")  # Add a newline between outputs

# Example usage: Process multiple test case files
if __name__ == "__main__":
    test_files = ["test_case_1.txt", "test_case_2.txt", "test_case_3.txt"]  # List of test files
    process_files(test_files)
