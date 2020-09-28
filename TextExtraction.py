import os
import sys

# Add your Computer Vision subscription key to your environment variables.
if 'b1ea6500dff642c38ca3b84a7a0fc5fd' in os.environ:
    subscription_key = os.environ['b1ea6500dff642c38ca3b84a7a0fc5fd']
else:
    print("\nSet the b1ea6500dff642c38ca3b84a7a0fc5fd environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# Add your Computer Vision endpoint to your environment variables.
if 'https://cvisionpython.cognitiveservices.azure.com/' in os.environ:
    endpoint = os.environ['https://cvisionpython.cognitiveservices.azure.com/']
else:
    print("\nSet the https://cvisionpython.cognitiveservices.azure.com/ environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

