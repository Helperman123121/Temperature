import tkinter


class TemperatureGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame
        self.celsius_label = tkinter.Label(self.top_frame, text="Enter the temperature in Celsius:")
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the widgets for the top frame
        self.celsius_label.pack(side="left")
        self.celsius_entry.pack(side="left")

        # Create the widgets for the middle frame
        self.fahrenheit_label = tkinter.Label(self.mid_frame, text="Temperature in Fahrenheit:")
        self.value = tkinter.StringVar()
        self.fahrenheit_result_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # Pack the widgets for the middle frame
        self.fahrenheit_label.pack(side="left")
        self.fahrenheit_result_label.pack(side="left")

        # Create the widgets for the bottom frame
        self.convert_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the widgets for the bottom frame
        self.convert_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def convert(self):
        # Get the temperature in Celsius
        celsius = float(self.celsius_entry.get())

        # Calculate the temperature in Fahrenheit
        fahrenheit = (9 / 5) * celsius + 32

        # Display the result
        self.value.set(fahrenheit)


# Create an instance of the TemperatureGUI class
temperature_gui = TemperatureGUI()