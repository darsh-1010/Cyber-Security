import random
def encrypt_decrypt(text, key, mode='encrypt'):
  """Encrypts or decrypts text using the provided key.

  Args:
    text: The text to encrypt or decrypt.
    key: The substitution key dictionary.
    mode: 'encrypt' (default) or 'decrypt'.

  Returns:
    The encrypted or decrypted text.
  """
  new_text = ''
  for char in text:
    if char.isalpha():
      new_char = key.get(char.lower()) if mode == 'decrypt' else key[char.lower()]
      new_text += new_char.upper() if char.isupper() else new_char
    else:
      new_text += char
  return new_text

def generate_substitution_key():
  """Generates a random, non-repeating key for the substitution cipher."""
  alphabet = list('abcdefghijklmnopqrstuvwxyz')
  random.shuffle(alphabet)
  return dict(zip(alphabet, alphabet[1:] + alphabet[:1]))

# Choose between a predefined key or generate a new one
choice = input("Use predefined key (P) or generate a new key (G)? ").upper()

if choice == 'P':
  # Define your substitution key dictionary (replace with your desired key)
  key = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 'x', 'e': 'b', 'f': 'w', 'g': 't', 'h': 'f', 'i': 'l', 'j': 'k', 'k': 'j', 'l': 'i', 'm': 'o', 'n': 'p', 'o': 'm', 'p': 'n', 'q': 'r', 'r': 'q', 's': 'u', 't': 'g', 'u': 's', 'v': 'v', 'w': 'f', 'x': 'd', 'y': 'a', 'z': 'z'}
elif choice == 'G':
  # Generate a new key
  key = generate_substitution_key()
  print("Generated key:", key)
else:
  print("Invalid choice. Please enter 'P' or 'G'.")
  exit()

# Get user input for encryption or decryption
while True:
  choice = input("Do you want to encrypt (E) or decrypt (D) text? ").upper()
  if choice in ('E', 'D'):
    break
  else:
    print("Invalid choice. Please enter 'E' or 'D'.")

# Get user input for the text
text = input("Enter the text: ")

# Encrypt or decrypt the text based on user choice
if choice == 'E':
  encrypted_text = encrypt_decrypt(text, key)
  print("Encrypted text:", encrypted_text)
else:
  decrypted_text = encrypt_decrypt(text, key, mode='decrypt')
  print("Decrypted text:", decrypted_text)
