# you need to run "pip install tkhtmlview" in the shell


# Import das modules
from tkinter import *
from tkhtmlview import HTMLLabel

# Create the looky thingy
root = Tk()
root.title("Argyleram Project")  # Set a title for the window
root.geometry("800x600")  # Set window dimensions (adjust as needed)

# Define the HTML content
html_content = """
<h1>The Argyleram Project</h1>
<section id="Description">
    <h2><center>Description</center></h2>
    <p><center>Welcome! The Argyleram Project aims to create the most secure messaging system. Stay tuned for more information!</center></p>
</section>
"""

# Create an HTML lable
the_label = HTMLLabel(root, html=html_content)
the_label.pack(fill=BOTH, expand=True)  # size

# Start thingy
root.mainloop()
