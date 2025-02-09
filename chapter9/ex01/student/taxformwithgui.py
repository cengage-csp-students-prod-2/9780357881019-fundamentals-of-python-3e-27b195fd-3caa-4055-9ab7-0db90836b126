# Write your code here
# Initialize the constants
import breezypythongui

               
import time

# Compute the income tax
class Window(breezypythongui.EasyFrame):
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0
    
    
    def __init__(self):
        breezypythongui.EasyFrame.__init__(self, "Tax Calculator")
        self.addLabel("Gross Income", 0, 0)
        self.addLabel("Dependants", 1, 0)
        self.dependants=self.addIntegerField(0, 1, 1)
        self.gross=self.addFloatField(0, 0, 1)
        self.button=self.addButton("Compute", 2, 0,command= self.gettax)
        self.addLabel("Total tax", 3, 0)
        self.taxfield=self.addTextField(0, 3, 1,state="readonly")

    def gettax(self):
        try:
            gross=self.gross.getNumber()
        except ValueError:
            self.messageBox("Error", "Enter a number for gross income")
            return
        try:
            dependants=self.dependants.getNumber()
        except ValueError:
            self.messageBox("Error", "Enter a number for dependants")
            return 
        tax= (gross - self.STANDARD_DEDUCTION - self.DEPENDENT_DEDUCTION * dependants )*self.TAX_RATE
        self.taxfield.setValue("$"+format(tax, '.2f'))



Window().mainloop()