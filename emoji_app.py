import emoji

# Example text with emojis
text_with_emojis = "Hello 😊! I love 🍕 and 🐍."

# Convert emojis to text descriptions
text_converted = emoji.demojize(text_with_emojis)

print(text_converted)
