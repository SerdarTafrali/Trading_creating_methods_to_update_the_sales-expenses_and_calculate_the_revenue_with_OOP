#Defining the "Trading" class
class Trading:
    #Initializing the object's attributes 
    def __init__(self,company_name, foundation_year,founder_name,company_slogan,sales, expenses, revenue):
      self.company_name = company_name
      self.foundation_year = foundation_year
      self.founder_name = founder_name
      self.company_slogan = company_slogan
      self.sales = sales
      self.expenses = expenses
      self.revenue = revenue      

    #Defining the print_report method
    def print_report(self):
      print(f"""
      The company{self.company_name} was founded in {self.foundation_year}.
      the founder of the company is {self.founder_name}.
      company slogan: {self.company_slogan}
      Total sales: {self.sales}
      Total expenses: {self.expenses}
      Total revenue: {self.revenue}""")      

    #Defining the update_sales_and_expenses method
    def update_sales_and_expenses(self, new_sales, new_expenses):
      self.sales += new_sales
      self.expenses += new_expenses
      print("Sales and expenses are updated!")


    #Defining the calculate_revenue method
    def calculate_revenue(self):
      self.revenue = self.sales = self.expenses
      print(f"The revenue of the company is {self.revenue}")
      
#Creating the object "trading_company1" with it's attributes
trading_company1 = Trading("TraCom", 2005, "Chong Wu", "We revolutionize trading.", 5000, 2000, 3000)

#Updating the sales and expenses
trading_company1.update_sales_and_expenses(100,50)

#Calculating the revenue
trading_company1.calculate_revenue()

#Calling the print_report method for trading_company1
trading_company1.print_report()
