#Budgeting System to keep track of the flow of money
import sqlite3
import sys
from tkinter import*
from tkinter import messagebox
from datetime import datetime

# print program title
programTitle = 'BUDGETING PROGRAM'
print (programTitle.center(80,'*'))

# Connect to Data Base
conn = sqlite3.connect('Budget_DB/budget')
print ('Successfully connect to datablase')

# Main Execution
def main():
    print ('Let the budgeting begin.', '\n')
    createBudgetTable()
    mainMenu = mainMenuWindow('Budgetting Menu')
    sys.exit(0)

            
# Create Budget Table
def createBudgetTable ():
    print ('Creating new table in Budget data base if one not exist,'
           'all parameter are preset. \n')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE budgetDistribution (
            ID INT PRIMARY KEY  NOT NULL,
            TRANSACTION_TYPE    TEXT    NOT NULL,
            DATE                DATE    NOT NULL,
            AMOUNT              REAL    NOT NULL
            )''')
        conn.commit()
        print ('Created table.')
    except Exception as e:
        print ('Table already exist.', '\n')
        conn.rollback()
        return 0

# Window for budgeting screen
class mainMenuWindow(object):

    def __init__(self, window_name):
        # create menu window
        self.window=Tk()
        self.window.title(window_name)
        self.window.minsize(width=500, height=500)
        # title 
        Label(self.window, text="Budgetting Main Menu").grid(row=0,column=1, columnspan=2)

        # transaction type
        Label(self.window, text="Tranaction Type: ").grid(row=1, column=0, sticky=W)
        self.trans_type = Entry(self.window, width=25)
        self.trans_type.grid(row=1, column=1)

        # transaction date
        Label(self.window, text="Transaction Date: ").grid(row=2, column=0, sticky=W)
        self.trans_date = Entry(self.window, width=25)
        self.trans_date.grid(row=2, column=1)

        # transaction amount
        Label(self.window, text="Amount: ").grid(row=3, column=0, sticky=W)
        self.amount = Entry(self.window, width=25)
        self.amount.grid(row=3, column=1)

        # submit button
        Button(self.window, text="Submit", command=self.submit_data).grid(row=4,column=1)

        # Quit Button
        quit_button = Button(self.window, text="Quit", command=self.quit_window)
        quit_button.grid(row=6,column=1, columnspan=2)

        self.window.mainloop()

    def submit_data(self):
        ''' build the query and submit data'''

        # get user inpunt date 
        #str_d = self.trans_date.get()
        month, day, year = map(int, self.trans_date.get().split('/'))
        try:
            transaction_type = self.trans_type.get()
            transaction_amount = ('{:.2f}'.format(float(self.amount.get())))
            transaction_date = datetime(year,month,day)
        except:
            messagebox.showerror("User Input Error", "Invalid field input!")
            return None
            
        if self.validate_entry(transaction_amount,transaction_date):
            print("Transaction Type: {0} \nTransaction Date: {1} \nTransaction Amount: ${2} \n"
                  .format(transaction_type, transaction_date, transaction_amount))

    def validate_entry(self, trx_amount, trx_date):
        ''' validate user input'''
        if not re.match('^\d*\.\d*$', trx_amount):
            messagebox.showerror('Amount Error', 'Cannot be empty and must use number only! \nEX: 45.00')
            return False

        if not re.match('^\d2\/\d2\/\d4$', trx_date):
            messagebox.showerror('Date Error', 'Date must be in this format DD/MM/YYYY')
            return False
        return True
            

    def quit_window(self):
        '''quit the main window'''
        self.window.destroy()
        
          
if __name__ == '__main__':
    main()
    

