import tkinter as tk
import winsound
import time

# Morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ' ': ' '}


class MorseCodeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")

        self.root.configure(bg='light grey')

        # Create labels and entry widgets
        self.input_label = tk.Label(root, text="Enter Text:", font=('Arial', 16))
        self.input_entry = tk.Entry(root, width=50, font=('Arial', 20))
        self.root.after(0, self.input_entry.focus)
        self.input_label.configure(bg='light grey')
        self.output_label = tk.Label(root, text="Morse Code:", font=('Arial', 16))
        self.output_entry = tk.Entry(root, width=50, state='readonly', font=('Arial', 20))
        self.output_label.configure(bg='light grey')

        # Create buttons
        self.to_morse_button = tk.Button(root, text="Convert to Morse", command=self.convert_to_morse, font=('Arial', 16,))
        self.sound_button = tk.Button(root, text="Play Sound", command=self.play_morse_sound, font=('Arial', 16,))
        self.to_morse_button.configure(bg='light grey')
        self.sound_button.configure(bg='light grey')
        self.to_morse_button.grid(row=1, column=0, columnspan=2, pady=5)
        self.sound_button.grid(row=1, column=2, pady=5)


        # Place widgets on the grid
        self.input_label.grid(row=0, column=0, padx=10, pady=5)
        self.input_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)
        self.to_morse_button.grid(row=1, column=0, columnspan=2, pady=5)
        self.sound_button.grid(row=1, column=2, pady=5)
        self.output_label.grid(row=2, column=0, padx=10, pady=5)
        self.output_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

    def convert_to_morse(self):
        text = self.input_entry.get().upper()
        morse_code = ' '.join([MORSE_CODE_DICT.get(char, char) for char in text])
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, morse_code)
        self.output_entry.config(state='readonly')

    def play_morse_sound(self):
        text = self.input_entry.get().upper()
        morse_code = ' '.join([MORSE_CODE_DICT.get(char, char) for char in text])
        self.play_sound(morse_code)

    def play_sound(self, morse_code):
        for symbol in morse_code:
            if symbol == '.':
                # Play a short beep for dot
                winsound.Beep(1000, 100)
            elif symbol == '-':
                # Play a longer beep for dash
                winsound.Beep(1000, 300)
            elif symbol == ' ':
                # Pause for space between words
                time.sleep(0.3)


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeConverter(root)
    root.mainloop()
