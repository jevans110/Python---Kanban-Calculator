import tkinter as tk


class BufferCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Kanban Buffer Calculator")

        # Create Labels
        self.label_buff = tk.Label(master, text="Buffer:")
        self.label_buff.grid(row=1, column=0)
        self.label_wip = tk.Label(master, text="Total WIP:")
        self.label_wip.grid(row=2, column=0)
        # self.label_cleaned = tk.Label(master, text="Pieces cleaned in week 1:")
        # self.label_cleaned.grid(row=3, column=0)
        self.label_finished = tk.Label(
            master, text="Pieces finishing this week:")
        self.label_finished.grid(row=3, column=0)
        self.label_38 = tk.Label(master, text="Product 1")
        self.label_38.grid(row=0, column=1)
        self.label_44 = tk.Label(master, text="Product 2")
        self.label_44.grid(row=0, column=2)
        self.label_50 = tk.Label(master, text="Product 3")
        self.label_50.grid(row=0, column=3)
        self.label_60 = tk.Label(master, text="Product 4")
        self.label_60.grid(row=0, column=4)

        # Create Entry fields
        self.buff_wip_38 = tk.Entry(master)
        self.buff_wip_38.insert(0, "12")
        self.buff_wip_44 = tk.Entry(master)
        self.buff_wip_44.insert(0, "5")
        self.buff_wip_50 = tk.Entry(master)
        self.buff_wip_50.insert(0, "30")
        self.buff_wip_60 = tk.Entry(master)
        self.buff_wip_60.insert(0, "31")
        self.buff_wip_38.grid(row=1, column=1)
        self.buff_wip_44.grid(row=1, column=2)
        self.buff_wip_50.grid(row=1, column=3)
        self.buff_wip_60.grid(row=1, column=4)

        self.entry_wip_38 = tk.Entry(master)
        self.entry_wip_38.focus()
        self.entry_wip_44 = tk.Entry(master)
        self.entry_wip_50 = tk.Entry(master)
        self.entry_wip_60 = tk.Entry(master)
        self.entry_wip_38.grid(row=2, column=1)
        self.entry_wip_44.grid(row=2, column=2)
        self.entry_wip_50.grid(row=2, column=3)
        self.entry_wip_60.grid(row=2, column=4)

        # self.entry_cleaned_38 = tk.Entry(master)
        # self.entry_cleaned_44 = tk.Entry(master)
        # self.entry_cleaned_50 = tk.Entry(master)
        # self.entry_cleaned_60 = tk.Entry(master)
        # self.entry_cleaned_38.grid(row=3, column=1)
        # self.entry_cleaned_44.grid(row=3, column=2)
        # self.entry_cleaned_50.grid(row=3, column=3)
        # self.entry_cleaned_60.grid(row=3, column=4)

        self.entry_finished_38 = tk.Entry(master)
        self.entry_finished_44 = tk.Entry(master)
        self.entry_finished_50 = tk.Entry(master)
        self.entry_finished_60 = tk.Entry(master)
        self.entry_finished_38.grid(row=3, column=1)
        self.entry_finished_44.grid(row=3, column=2)
        self.entry_finished_50.grid(row=3, column=3)
        self.entry_finished_60.grid(row=3, column=4)

        # Create Buttons
        self.button_calculate = tk.Button(
            master, text="Calculate", command=self.calculate)
        self.button_calculate.grid(row=6, column=4)

        # Create Output Labels
        self.label_output_38 = tk.Label(
            master, text="Pieces that can be Processed for Product 1:")
        self.label_output_44 = tk.Label(
            master, text="Pieces that can be Processed for Product 2:")
        self.label_output_50 = tk.Label(
            master, text="Pieces that can be Processed for Product 3:")
        self.label_output_60 = tk.Label(
            master, text="Pieces that can be Processed for Product 4:")
        self.label_output_38.grid(row=6, column=0)
        self.label_output_44.grid(row=7, column=0)
        self.label_output_50.grid(row=8, column=0)
        self.label_output_60.grid(row=9, column=0)

        self.label_output_value_38 = tk.Label(master, text="")
        self.label_output_value_44 = tk.Label(master, text="")
        self.label_output_value_50 = tk.Label(master, text="")
        self.label_output_value_60 = tk.Label(master, text="")
        self.label_output_value_38.grid(row=6, column=1)
        self.label_output_value_44.grid(row=7, column=1)
        self.label_output_value_50.grid(row=8, column=1)
        self.label_output_value_60.grid(row=9, column=1)

    def calculate(self):
        # Get input values
        buff_38 = int(self.buff_wip_38.get())
        buff_44 = int(self.buff_wip_44.get())
        buff_50 = int(self.buff_wip_50.get())
        buff_60 = int(self.buff_wip_60.get())

        wip_38 = int(self.entry_wip_38.get())
        wip_44 = int(self.entry_wip_44.get())
        wip_50 = int(self.entry_wip_50.get())
        wip_60 = int(self.entry_wip_60.get())

        finished_38 = int(self.entry_finished_38.get())
        finished_44 = int(self.entry_finished_44.get())
        finished_50 = int(self.entry_finished_50.get())
        finished_60 = int(self.entry_finished_60.get())

        # Calculate output values
        if buff_38 - wip_38 + finished_38 <= buff_38:
            output_38 = buff_38 - wip_38 + finished_38
        elif buff_38 - wip_38 + finished_38 < 0:
            output_38 = 0
        else:
            output_38 = buff_38

        if buff_44 - wip_44 + finished_44 <= buff_44:
            output_44 = buff_44 - wip_44 + finished_44
        elif buff_44 - wip_44 + finished_44 < 0:
            output_44 = 0
        else:
            output_44 = buff_44

        if buff_50 - wip_50 + finished_50 <= buff_50:
            output_50 = buff_50 - wip_50 + finished_50
        elif buff_50 - wip_50 + finished_50 < 0:
            output_50 = 0
        else:
            output_50 = buff_50

        if buff_60 - wip_60 + finished_60 <= buff_60:
            output_60 = buff_60 - wip_60 + finished_60
        elif buff_60 - wip_60 + finished_60 < 0:
            output_60 = 0
        else:
            output_60 = buff_60

        # Update output labels
        self.label_output_value_38.configure(text=output_38)
        self.label_output_value_44.configure(text=output_44)
        self.label_output_value_50.configure(text=output_50)
        self.label_output_value_60.configure(text=output_60)

    # def get_remaining(self, cleaned, finished):
     #   return max(0, cleaned - finished)


root = tk.Tk()
gui = BufferCalculator(root)
root.mainloop()
