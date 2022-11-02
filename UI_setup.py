import datetime
import json
import tkinter
from finances_importer import stock_price_downloading
from project import prices

with open('nifty100.json', 'r') as stocks:
    stocks = json.load(stocks)

x = None


def execute():
    prices()
    window.destroy()
    execute_further()


def execute_further():
    x = 0
    pict_list = ["All_plot.png", "heatmap.png", "highest_STD.png", "stock_1.png", "stock_2.png", "stock_3.png",
                 "stock_4.png", "stock_5.png", "All_stock_hist.png", "rsi_1.png", "rsi_2.png", "rsi_3.png", "rsi_4.png"
                 , "rsi_5.png"]

    def next_img():
        nonlocal x, pict_list, chart_img, chart_sec
        x += 1
        if x > 13:
            x = 0
        chart_img = tkinter.PhotoImage(file=f"pict\{pict_list[x]}")
        chart_sec = canvas.create_image(500, 350, image=chart_img)

    window = tkinter.Tk()
    window.title("Chart Analysis")
    window.geometry("1000x1000")
    window.config(bg="#272c3c")

    title_label = tkinter.Label(window, text="Chart Analysis", fg="yellow", bg="#272c3c", font=("ariel", 25))
    title_label.grid(row=0, column=1)
    next_button = tkinter.Button(window, text="Next", highlightthickness=0, command=next_img,padx=25, pady=10)
    next_button.grid(row=0, column=2)
    canvas = tkinter.Canvas(height=900, width=1000, highlightthickness=0, bg="#272c3c")
    chart_img = tkinter.PhotoImage(file=f'pict/{pict_list[0]}')
    chart_sec = canvas.create_image(500, 350, image=chart_img)
    canvas.grid(row=1, column=1, columnspan=3)

    window.mainloop()


window = tkinter.Tk()
window.title("Stock choices")
window.geometry('700x500')
window.config(padx=150, pady=70, bg='#272c3c')


# Create an empty list that I will fill with my inputs
stock_choices = [None] * 5

# list of all StringVars for each OptionMenu
values = []
label = tkinter.Label(text="Pick your stock", fg='Orange', font=('Ariel', 25, 'bold'), pady=25, bg='#272c3c')
label.grid(row=0, column=1)

# Create the option menu widget and passing
# the options_list and value_inside to it.

for i in range(0, 5, 1):
    # Variable to keep track of the option selected in OptionMenu
    value_inside = tkinter.StringVar(window)
    # Set the default value of the variable
    value_inside.set("stock_choices" + str(i + 1))
    stock_menu = tkinter.OptionMenu(window, value_inside, *list(stocks))
    stock_menu.config(pady=10, width=50, bg='#acbca4', highlightthickness=0)
    stock_menu.grid(column=1, row=i+1)
    values.append(value_inside)


def time():
    START_TIME = datetime.datetime(2010, 1, 1)
    END_TIME = datetime.datetime(2021, 12, 31)
    stock_price_downloading(START_TIME, END_TIME)


def stock_picker():
    risk_stock = {}
    for val in values:
        risk_stock[val.get()] = stocks[val.get()]
# making list of selected list
    with open('risk_stock.json', 'w') as rs:
        json.dump(risk_stock, rs, indent=4)
    time()


# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(window, text='Submit', command=stock_picker)
submit_button.grid(row=7, column=1, pady=20)
final_button = tkinter.Button(window, text='final', command=execute)
final_button.grid(row=8, column=1)

window.mainloop()

