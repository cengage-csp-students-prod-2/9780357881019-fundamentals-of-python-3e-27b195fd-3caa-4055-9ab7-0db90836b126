import breezypythongui


class Window(breezypythongui.EasyFrame):
    """The window for the temperature converter."""
    
    @classmethod
    def ctof(cls, celsius:float):
        """Returns the celsius temperature in fahrenheit."""
        
        return celsius * 1.8 + 32
    @classmethod
    def ftoc(self, fahrenheit:float):
        """Returns the fahrenheit temperature in celsius."""
        return (fahrenheit - 32) / 1.8
    def __init__(self):
        """
        Creates the main window and its widgets.
        """
        
        breezypythongui.EasyFrame.__init__(self, "Temperature converter")
        self.addLabel("Celsius", 0, 0)
        self.addLabel("Fahrenheit", 0, 1)
        self.celsiusfield=self.addFloatField(0, 1, 0)
        self.fahrenheitfield=self.addFloatField(32.0, 1, 1)
        self.button1=self.addButton(">>>>>", 2, 0,command= self.celsiustofahrenheit)
        self.button2=self.addButton("<<<<<", 2, 1,command= self.fahrenheittocelsius)


    def celsiustofahrenheit(self):
        """ 
        When the user clicks the '>>>>>' button, the program should read the
        value in the celsius field, convert it to fahrenheit and write the result
        to the fahrenheit field. If the celsius field does not contain a valid
        number, an error message should be displayed.
        """
        try:
            celsius=self.celsiusfield.getNumber()
        except ValueError:
            self.messageBox("Error", "Enter a number for celsius")
            return  
        fahrenheit=self.ctof(celsius)                
        self.fahrenheitfield.setValue(format(fahrenheit, '.2f'))

    def fahrenheittocelsius(self):
        """
        When the user clicks the '<<<<<' button, the program should read the
        value in the fahrenheit field, convert it to celsius and write the result
        to the celsius field. If the fahrenheit field does not contain a valid
        number, an error message should be displayed.
        """
        try:           
            fahrenheit=self.fahrenheitfield.getNumber()
        except ValueError:            
            self.messageBox("Error", "Enter a number for fahrenheit")
            return
        celsius=self.ftoc(fahrenheit)
        self.celsiusfield.setValue(format(celsius, '.2f'))

Window().mainloop()