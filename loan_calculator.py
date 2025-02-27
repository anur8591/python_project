from tkinter import *

class LoanCalculator:
    def __init__(self):  # Corrected constructor name
        window = Tk()  
        window.title("Loan Calculator")  
        window.geometry("400x350")  # Increased window size for spacing

        # Set background color for the entire window
        window.configure(bg="lightblue")

        # Labels with background color and spacing
        Label(window, text="Annual Interest Rate (%) :", bg="lightblue", pady=5).grid(row=1, column=1, sticky=W)
        Label(window, text="Number of Years :", bg="lightblue", pady=5).grid(row=2, column=1, sticky=W)
        Label(window, text="Loan Amount (₹) :", bg="lightblue", pady=5).grid(row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment :", bg="lightblue", pady=5).grid(row=4, column=1, sticky=W)
        Label(window, text="Total Payment :", bg="lightblue", pady=5).grid(row=5, column=1, sticky=W)
        Label(window, text="Status :", bg="lightblue", pady=10).grid(row=7, column=1, sticky=W)

        # Variables
        self.annualInterestRateVar = StringVar()
        self.numberOfYearsVar = StringVar()
        self.loanAmountVar = StringVar()
        self.monthlyPaymentVar = StringVar()
        self.totalPaymentVar = StringVar()
        self.statusVar = StringVar()

        # Entry Fields with background color and spacing
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT, bg="white").grid(row=1, column=2, pady=5)
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT, bg="white").grid(row=2, column=2, pady=5)
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT, bg="white").grid(row=3, column=2, pady=5)

        # Output Labels with background color and spacing
        Label(window, textvariable=self.monthlyPaymentVar, bg="yellow", pady=5).grid(row=4, column=2, sticky=E)
        Label(window, textvariable=self.totalPaymentVar, bg="yellow", pady=5).grid(row=5, column=2, sticky=E)
        Label(window, textvariable=self.statusVar, bg="lightgray", pady=10).grid(row=7, column=2, sticky=E)

        # Compute Button with green color and spacing
        Button(window, text="Compute Payment", command=self.computePayment, bg="green", fg="white", pady=5).grid(row=6, column=2, columnspan=2, sticky=E, pady=10)

        # Clear Button with red color and spacing
        Button(window, text="Clear", command=self.clearFields, bg="red", fg="white", pady=5).grid(row=8, column=2, columnspan=2, sticky=E, pady=10)
        
        window.mainloop()  

    def clearFields(self):
        self.annualInterestRateVar.set("")
        self.numberOfYearsVar.set("")
        self.loanAmountVar.set("")
        self.monthlyPaymentVar.set("")
        self.totalPaymentVar.set("")
        self.statusVar.set("")

    def computePayment(self):
        # Validate input fields for numbers
        if self.isValidInput(self.loanAmountVar.get()) and self.isValidInput(self.annualInterestRateVar.get()) and self.isValidInput(self.numberOfYearsVar.get()):
            try:
                # Calculate Monthly Payment
                monthlyPayment = self.getMonthlyPayment(
                    float(self.loanAmountVar.get()),
                    float(self.annualInterestRateVar.get()) / 1200,
                    int(self.numberOfYearsVar.get())
                )

                # Set the results
                self.monthlyPaymentVar.set('₹' + format(monthlyPayment, '10.2f'))
                totalPayment = monthlyPayment * 12 * int(self.numberOfYearsVar.get())
                self.totalPaymentVar.set('₹' + format(totalPayment, '10.2f'))

                self.statusVar.set("Calculation Successful !")

            except Exception as e:
                self.statusVar.set(f"Error: {str(e)}")
        else:
            self.statusVar.set("Invalid Input. Please enter numbers only.")

    def isValidInput(self, input_value):
        # Check if the input is a valid number (float or integer)
        try:
            float(input_value)  # Try to convert to a float
            return True
        except ValueError:
            return False

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # Formula to calculate monthly payment
        if monthlyInterestRate == 0:
            return loanAmount / (numberOfYears * 12)
        return loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)))

# Run the application
LoanCalculator()
