def caesar_cipher(text, shift, decrypt=False):
  """
  Encrypts or decrypts text using a Caesar cipher with a shift of 3.

  Args:
    text: The text to encrypt or decrypt.
    shift: The amount to shift the letters by (positive for encryption, negative for decryption).
    decrypt: Whether to decrypt the text (default: False).

  Returns:
    The encrypted or decrypted text.
  """

  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_text = ''
  for char in text:
    if char not in alphabet:
      new_text += char
      continue
    index = alphabet.find(char)
    new_index = (index + shift) % len(alphabet)
    new_char = alphabet[new_index]
    new_text += new_char if not decrypt else alphabet[ (index - shift) % len(alphabet)]
  return new_text

# Get user input for encryption or decryption
while True:
  print("Welcome To Ceaser Cypher")
  choice = input("Do you want to encrypt (E) or decrypt (D) text? ").upper()
  if choice in ('E', 'D'):
    break
  else:
    print("Invalid choice. Please enter 'E' or 'D'.")

# Get user input for the text
text = input("Enter the text: ")

# Encrypt or decrypt the text based on user choice
if choice == 'E':
  encrypted_text = caesar_cipher(text, 3)
  print("Encrypted text:", encrypted_text)
else:
  decrypted_text = caesar_cipher(text, -3)
  print("Decrypted text:", decrypted_text)
