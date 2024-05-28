# you need to run "pip install tkhtmlview" in the shell


# Import necessary modules
from tkinter import *
from tkhtmlview import HTMLLabel

# Create the main window
root = Tk()
root.title("Argyleram Project")  # Set a title for the window
root.geometry("800x600")  # Set window dimensions (adjust as needed)

# Define the HTML content
html_content = """
<h1>The Argyleram Project</h1>
<section id="Description">
    <h2>Description</h2>
    <p>Welcome! The Argyleram Project aims to create the most secure messaging system. Stay tuned for more information!</p>
</section>
"""

# Create an HTMLLabel widget
the_label = HTMLLabel(root, html=html_content)
the_label.pack(fill=BOTH, expand=True)  # Adjust label size

# Start the main event loop
root.mainloop()
