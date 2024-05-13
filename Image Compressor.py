import os
from PIL import Image
import tkinter as tk  
from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel, CTkFrame
from tkinter import filedialog

def compress_image(image_path, output_path, quality, max_width=None, max_height=None):
  image = Image.open(image_path)
  if max_width or max_height:
    image.thumbnail((max_width, max_height))

  if image.format.upper() in ("JPEG", "WEBP"):
    image.save(output_path, quality=quality)
  else:
    image.convert('RGB').save(output_path, 'JPEG', quality=quality)

def select_and_compress():
  def browse_image():
    filename = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if filename:
        entry.delete(0, tk.END)  # Use tk.END for standard deletion
        entry.insert(0, filename)


  def compress():
    image_path = entry.get()
    if image_path:
      filename, _ = os.path.splitext(image_path)
      output_path = f"{filename}_compressed.jpg"

      max_width = int(width_entry.get() or 0)
      max_height = int(height_entry.get() or 0)

      compress_image(image_path, output_path, 75, max_width, max_height)
      result_label.configure(text=f"Image compressed and saved as: {output_path}")

  root = CTk()
  root.title("Image Compressor")

  # Create a frame to group interface elements (optional for better organization)
  content_frame = CTkFrame(master=root)
  content_frame.pack(padx=20, pady=20)

  browse_button = CTkButton(master=content_frame, text="Browse", command=browse_image)
  browse_button.pack(pady=10)

  entry = CTkEntry(master=content_frame, width=50)
  entry.pack(pady=10)

  width_label = CTkLabel(master=content_frame, text="Enter desired maximum width (or leave blank):")
  width_label.pack(pady=5)

  width_entry = CTkEntry(master=content_frame)
  width_entry.pack(pady=5)

  height_label = CTkLabel(master=content_frame, text="Enter desired maximum height (or leave blank):")
  height_label.pack(pady=5)

  height_entry = CTkEntry(master=content_frame)
  height_entry.pack(pady=5)

  compress_button = CTkButton(master=content_frame, text="Compress", command=compress)
  compress_button.pack(pady=10)

  result_label = CTkLabel(master=content_frame, text="")
  result_label.pack(pady=10)

  root.mainloop()

if __name__ == "__main__":
  select_and_compress()
