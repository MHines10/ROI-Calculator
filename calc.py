# "Bigger Pockets" ROI Calculator Project

#Create a class for the ROI Calculator
class ROIcalc:
    def __init__(self, monthly_income, added_monthly_expenses, total_investment):
        self.monthly_income = monthly_income
        self.added_monthly_expenses = added_monthly_expenses
        self.total_investment = total_investment
    # Create a method to calculate the monthly cash flow from rental property
    def monthly_cash_flow(self):
        #Subtract the total expenses from the total monthly income
        return self.monthly_income - self.added_monthly_expenses
    # Create a method to calculate the Cash on Cash ROI
    def cash_on_cash_roi(self):
        # Multiply monthly cash flow by 12 to get the annual cash flow total
        annual_cash_flow = self.monthly_cash_flow() * 12
        # Divide the annual cash flow by the total invested amount for property
        # to receive the CoCROI percentage.
        return annual_cash_flow / self.total_investment
        
# A function to calculate users inputs for ROI    
def roi_run():
    # Create user inputs and convert to "int"
    # Take input for total invested amount for property from user
    total_investment = int(input("What is your total invesment for this property? $"))
    # Input for total monthly income from user
    monthly_income = int(input("What is the total monthly income? $"))
    # Input for total monthly expenses from user
    added_monthly_expenses = int(input("Add your total monthly expenses for this property: $"))
    
    # Create an instance to of ROIcalc to pull from class
    prop = ROIcalc(monthly_income, added_monthly_expenses, total_investment)
    # Assign cash flow and cocROI method to instance to return the total
    cash_flow = prop.monthly_cash_flow()
    cash_on_cash_roi = prop.cash_on_cash_roi()
    # Prints out the calculated ROI, Gives monthly and Annual cash flow
    # and CoCROI percentage
    print(f"Your monthly Cash flow: ${cash_flow}. Your Annual Cash Flow: ${cash_flow * 12:,.2f}\nYour Cash on Cash ROI is {cash_on_cash_roi * 100}%")
    
roi_run()