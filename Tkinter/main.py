from tkinter import *
from tkhtmlview import HTMLLabel
root = Tk()
root.title("Argyleram Project")
root.geometry("800x600")
html_content = """
<h1 style="text-align: center;">The Argyleram Project</h1>
<section id="Description">
    <h2 style="text-align: center;">Description</h2>
    <p style="text-align: center; color: grey;">Welcome! The Argyleram Project aims to create the most secure messaging system. Stay tuned for more information!</p>
</section>
<section id="instructions">
    <h2 style="text-align: center;">Instructions</h2>
    <p style="text-align: center; color: grey;">Enter the message you would like to send below:</p>
</section>
"""
the_label = HTMLLabel(root, html=html_content)
the_label.pack(fill=BOTH, expand=True)
msg_window = Text(root, height=10, width=50)
msg_window.pack(pady=10)
def send_message():
    msg = msg_window.get("1.0", "end-1c")
    print(f"Sending message: {msg}")
send_button = Button(root, text="Send Message", command=send_message)
send_button.pack()
root.mainloop()
