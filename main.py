import tkinter

window = tkinter.Tk()
window.title("BMI calculator")
window.config(padx=50, pady=50)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height !")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")





weight_input_label = tkinter.Label(text="Enter your weight (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate")
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI: {round(bmi,2)}. You are"
    if bmi <= 16:
        result_string += "several thin!"
    elif bmi> 16 and bmi <= 17:
        result_string += "moderatery thin"
    elif bmi > 17 and bmi <=18.5:
        result_string += "obese!"

window.mainloop()