import os
import time
import fontstyle
from datetime import datetime
from prettytable import PrettyTable
from abc import ABC, abstractmethod
from dateutil.relativedelta import relativedelta
# __________________________________________________________ ADMIN CLASS BEGINS _________________________________________________________ #

class Admin:
    def __init__(self):
        with open('ADMIN//Admin.txt', 'r') as f:
            self.content = f.read()

    def Signin(self):
        '''Sign in interface of Admin'''
        while True:
            password = input('''
    Enter Password: ''')
            if password == self.content:
                self.admin_Activity()
                os.system('cls')
                return
            else:
                print('''
    Incorrect Password
    PLease try again!!''')
                time.sleep(0.9)
                os.system('cls')
                continue

    def admin_Activity(self):
        '''Activities/Actions that admin can perform'''
        text = fontstyle.apply('``` MAIN MENU ```', 'bold/white/black')
        while True:
            os.system('cls')
            print(f'''
                        {text}

                    1. View No of Customers
                    2. View Customers Activity
                    3. View Number Of Individual Accounts
                    4. Go Back To Main Interface
                    5. Exit''')
            try:
                choice = input('''
                    Enter your choice: ''')
                if choice == '1':
                    # All the subfolders in the 'ADMIN' directory are customer accounts
                    self.No_of_customers = os.listdir('ADMIN')
                    print(f'''
                    TOTAL NO OF CUSTOMERS IN AMN ONLINE BANKING SYSTEM : {len(self.No_of_customers)-1} customer(s)''')
                    input('\nPress Enter to  continue....')
                    os.system('cls')
                    continue
                elif choice == '2':
                    '''Prints names of all Customer files and their accounts '''
                    
                    self.No_of_customers = os.listdir('ADMIN')
                    if len(self.No_of_customers)==1:
                        print('''
                    There are no customers in the bank. ''')
                        input('''
                    Press any key to go to the main menu''')
                        continue
                    text = fontstyle.apply('CUSTOMERS LIST:', 'bold/black')
                    print(f'''
                    {text}''')
                    self.No_of_customers.remove('Admin.txt')
                    for ind, customer in enumerate(self.No_of_customers):
                        print(f'''  {ind+1}. {customer} ''')
                    '''If the admin want to open the file of a specific customer '''
                    self.customer_file = int(
                        input('''  Enter serial no before th customer to open its file:'''))
                    os.system('cls')
                    self.Customer_details()
                elif choice == '3':

                    '''It will give total no of saving,checking and loan account formed in the bank'''
                    self.Total_accounts = os.listdir('ADMIN')
                    if len(self.Total_accounts)==1:
                        print('''
                    There are no accounts in the bank. ''')
                        input('''
                    Press any key to go to the main menu''')
                        continue
                    self.Total_accounts.remove('Admin.txt')

                    saving__accounts = 0
                    checking__accounts = 0
                    loan__accounts = 0
                    for i in self.Total_accounts:
                        print('in for')
                        accounts = os.listdir(f'ADMIN//{i}')
                        

                        accounts.remove('Basic_Info.txt')

                        for j in accounts:
                            print('j')
                            if j == 'Saving_Account.txt':
                                print('s')
                                saving__accounts += 1
                            elif j == 'Checking_Account':
                                checking__accounts += 1
                            else:
                                loan__accounts += 1
                    os.system('cls')

                    print(f'''
    Total Checking Accounts are: {checking__accounts} account(s)
    Total Saving Accounts are: {saving__accounts} account(s)
    Total Loan Accounts are: {loan__accounts} accounts''')
                    input('''
                        Press Enter to continue....''')

                elif choice == '4':
                    return
                elif choice == '5':
                    choose = input(
                        'Are you sure you want to exit? [Press Enter if "Yes" or any other key if "NO"]:   ')
                    if choose == '':
                        exit()
                else:
                    print('Enter valid choice')
                    os.system('cls')

            except:
                print('Please Enter Valid Choice')
                # os.system('cls')

    def Customer_details(self):
        '''It gives admin the access of all the accounts and basic information of the user'''
        os.system('cls')
        text = fontstyle.apply('```Customer Information```', 'bold//black')
        while True:
            print(f'''
                    {text}
              
                1.View Basic Information
                2.View Accounts
                3.Go back''')

            choice = int(input('''
                Enter your choice: '''))
            if choice == 1:
                '''It will print the Basic_Info.txt file of the user'''
                print('''
                BASIC INFORMATION: ''')
                with open(f'ADMIN\\{self.No_of_customers[self.customer_file-1]}\\Basic_info.txt') as f:
                    print(f'''{f.read()}''')
                    time.sleep(0.8)
                choice = input(
                    '\nPress any key to go back to Customer Information: ')
                os.system('cls')
            if choice == 2:
                '''IT will print all the accounts formed by the user'''
                accounts = os.listdir(f'ADMIN\\{self.No_of_customers[self.customer_file-1]}')
                accounts.remove('Basic_Info.txt')
                if len(accounts)==0:
                    print(f'''
                {self.No_of_customers[self.customer_file-1]} has no accounts''')
                    input('''
                Press Enter to go to Customer Information ''')
                    os.system('cls')
                    continue
                for ind, acc in enumerate(accounts):
                    print(f'{ind+1}. {acc}')
                time.sleep(0.9)
                '''The admin can view the balance enquiry report of any specific account of the user by entering the S.NO written before the accounts'''
                print('''
                        Press the number before the account to view its Balance Enquiry Report
                                                    OR
                                Press Enter to go back to customer information ''')
                choice = int(input('''
                        Enter your choice: '''))
                os.system('cls')
                if choice != '':
                    username = self.No_of_customers[self.customer_file-1]
                    if accounts[choice-1] == 'Saving_Account.txt':
                        obj = Saving_Account(username)
                        obj.Balance_Enquiry(self.Customer_details)

                    elif accounts[choice-1] == "Loan_Account":
                        obj = Loan_Account(username)
                        obj.Balance_Enquiry(username, 'Loan Account')
                    elif accounts[choice-1] == "Checking_Account":
                        obj = Checking_Account(username)
                        obj.Balance_Enquiry(username, 'Checking Account')

            if choice == 3:
                self.admin_Activity()

# ___________________________________________________________ ADMIN CLASS ENDS __________________________________________________________ #

# _______________________________________________________________________ ACCOUNT CLASS BEGINS _____________________________________________________________________ #


class Account(ABC):

    # --------------------------------------------------------------------------------------------------------------------------------#
    def __init__(self, data):
        self.customer_data = data
        self.balance = 0
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Deposit(self):
        deposit = int(input('Enter amount to be deposited: '))
        self.balance += deposit
        print('Amount deposited successfully!!')
        transaction = [datetime.now(), 'Deposit', deposit, self.balance]
        return transaction
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Withdraw(self):
        self.withdraw = int(input('Enter amount to be withdrawn: '))
        self.balance -= self.withdraw

        if self.balance < 0:
            self.balance += self.withdraw
            print(
                f'You have run out of balance. You have Rs.{self.balance}/= only...')
            self.overdraft = self.withdraw - self.balance

        else:
            print('Amount withdrawn successfully!!')
        transaction = [datetime.now(), 'Withdraw', self.balance]
        return transaction
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    @abstractmethod
    def Balance_Enquiry(self, username, report):
        back_to_main_menu = 1
        while back_to_main_menu:
            if report == 'Checking Account':
                with open(f'ADMIN//{username}//Loan_Account', 'r+') as f:
                    print(f.read())
                back_to_main_menu = input('''
        Press any key to go back to Main Menu...''')
                break

            if report == 'Saving Account':
                with open(f'ADMIN//{username}//Loan_Account', 'r+') as f:
                    print(f.read())
                back_to_main_menu = input('''
        Press any key to go back to Main Menu...''')
                break

            if report == 'Loan Account':
                with open(f'ADMIN//{username}//Loan_Account', 'r+') as f:
                    print(f.read())
                back_to_main_menu = input('''
        Press any key to go back to Main Menu...''')
                break
    # --------------------------------------------------------------------------------------------------------------------------------#

# _______________________________________________________________________ ACCOUNT CLASS BEGINS _____________________________________________________________________ #

# ________________________________________________________________ CHECKING ACCOUNT CLASS BEGINS ___________________________________________________________________ #


class Checking_Account(Account):
    # --------------------------------------------------------------------------------------------------------------------------------#
    def Info(self):

        while True:
            try:
                print('''
        Initializing Checking Account
        Please fill the following input fields.
        [NOTE]
        Your business earning must be greater than the Credit Limit and Overdraft Limit
        Credit limit must not be greater than 200000
        Overdraft Limit must not be greater than 100000 and must be less than Credit Limit''')
                self.business_earning = float(
                    input('Enter you Monthly Earning :'))
                while True:
                    self.credit_limit = float(input('Set your credit limit: '))
                    if self.credit_limit > 200000:
                        print(
                            '''Credit limit cannot be greater than 200000. Please follow the instructions😑''')
                        continue

                    else:
                        while True:
                            self.overdraft_limit = float(
                                input('Set overdraft limit enter amount: '))
                            if self.credit_limit < self.overdraft_limit:
                                print(
                                    'The overdraft limit cannot be greater than credit limit. Please follow the instructions😑')
                                continue
                            else:
                                self.Create_file()
                                break
                        break
                input('''
                      Checking Account is created successfully!
                      Press any key to continue...''')
                break

            except ValueError:
                print('Input digits')
    # --------------------------------------------------------------------------------------------------------------------------------#

    def Create_file(self):
        with open(f'ADMIN\\{self.customer_data[0]}\\Checking_Account', '+a') as f:
            f.write(f'''
                                            AMN ONLINE BANKING SYSTEM
_______________________________________________________________________________________________________________________

                                         ``` CUSTOMER AND ACCOUNT DETAILS ```
ACCOUNT NAME: CHECKING ACCOUNT                              
USERNAME: {self.customer_data[0]}           
CUSTOMER NAME: {self.customer_data[2]}                       
CNIC: {self.customer_data[3]}
OVERDRAFT_LIMIT:{self.overdraft_limit}
CREDIT_LIMIT:{self.credit_limit}
MONTHLY EARNING : {self.business_earning}
_______________________________________________________________________________________________________________________
                                            ```  Transaction History ```
_______________________________________________________________________________________________________________________            
|      DATE      |    Transaction Type    |    Transaction Amount    |    Overdraft Balance   |     Total Balance     |''')

    # --------------------------------------------------------------------------------------------------------------------------------#
    def Interface(self):
        while True:
            if 'Checking_Account' in os.listdir(f'ADMIN\\{self.customer_data[0]}'):
                self.Main()
                break

            else:
                self.Info()

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Main(self):
        while True:

            os.system('cls')
            print('''
                        CHECKING ACCOUNT

                        MAIN MENU

                        1. DEPOSIT
                        2. WITHDRAW 
                        3. BALANCE ENQUIRY REPORT
                        4. EXIT
                        ''')
            action = input('''
                        Enter your Choice: ''')

            if action == '1':
                os.system('cls')
                self.Deposit()

            elif action == '2':
                os.system('cls')
                self.Withdraw()

            elif action == '3':
                os.system('cls')
                self.Balance_Enquiry(self.customer_data[0], 'Checking Account')

            elif action == '4':
                os.system('cls')
                break  # to break loan interface loop and to reach customer interface from where it was called

            else:
                print('''
                    Invalid Input!!''')

    # --------------------------------------------------------------------------------------------------------------------------------#
    def Withdraw(self):
        self.File_read()  # retrieving data from file
        while True:
            print('''
            WITHDRAW''')
            try:
                self.transaction_amount = input('''
            Enter amount to be withdrawn OR press Enter Key to go back to Main Menu.
            Type Here:  ''')
                if self.transaction_amount == '':
                    break
                else:
                    self.transaction_amount = float(self.transaction_amount)
            except ValueError:
                print('Type in digits')
            else:
                self.transaction_type = 'WITHDRAW'

                if self.transaction_amount <= self.credit_limit:
                    self.balance -= self.transaction_amount

                    if self.balance <= 0:
                        print(
                            f'You have run out of balance. You have Rs.{self.balance+self.transaction_amount}/= only ...')
                        self.overdraft_balance += - self.balance
                        while True:
                            ov = input(
                                '''Do you want overdraft?\nType (y/n) for yes or no  ''').upper()
                            if ov == 'Y':

                                if self.overdraft_balance <= self.overdraft_limit:
                                    self.balance = 0
                                    print(
                                        f'you withdraw {self.transaction_amount} and overdraft is{self.overdraft_balance}\n Balance is {self.balance} ')
                                    self.d = [f'{datetime.now().date()}', self.transaction_type, self.transaction_amount,
                                              self.overdraft_balance, self.balance]
                                    self.File_edit()
                                    input('Enter any key to continue')
                                    break

                                else:
                                    print(
                                        f"you can't withdraw {self.transaction_amount} Rs. as your overdraft balance is{self.overdraft_balance } which is greater than overdraft limit ({self.overdraft_limit})")
                                    self.overdraft_balance -= - self.balance
                                    self.balance += self.transaction_amount
                                    input('Enter any key to continue')
                                    break
                            elif ov == 'N':
                                break
                            else:
                                print('Invalid Input')
                    else:
                        print(
                            f'Amount withdrawn successfully!!\nCurrent Balance is {self.balance}')
                        self.overdraft_balance = 0
                        self.d = [f'{datetime.now().date()}', self.transaction_type, self.transaction_amount,
                                  self.overdraft_balance, self.balance]
                        self.File_edit()  # write variables in files
                        input('Enter any key to continue')
                        break

                elif self.transaction_amount > self.credit_limit:
                    print(
                        f'Cannot withraw Rs. {self.transaction_amount} as your credit limit is {self.credit_limit} which is less than this amount !')
                    input('Enter any key to continue')
                else:
                    print('Invalid Input !')

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Deposit(self):
        self.File_read()
        print('''
            DEPOSIT''')
        self.transaction_type = 'DEPOSIT'  # retrieving data from file
        while True:
            try:
                self.transaction_amount = input('''
                Enter amount to be deposited OR press Enter Key to go back to Main Menu.
                Type Here:  ''')
                if self.transaction_amount == '':
                    break
                else:
                    self.transaction_amount = float(self.transaction_amount)
            except ValueError:
                print('Type in digits')
            else:
                amount = self.transaction_amount

                if self.balance == 0:
                    amount -= self.overdraft_balance

                    if amount < 0:
                        print('your remaining overdraft balance is ', -amount,
                              'all money you deposit is deducted from your account to pay overdraft balance'
                              f'Your Balance is {self.balance}')
                        self.overdraft_balance = - amount
                        self.d = [f'{datetime.now().date()}', self.transaction_type, self.transaction_amount,
                                  self.overdraft_balance, self.balance]
                        self.File_edit()
                        input('Enter any key to continue')
                        break

                    elif amount == 0:
                        print('all money you deposit is deducted from your acoount your current balance is 0'
                              f'Your Balance is {self.balance}')
                        self.overdraft_balance = 0
                        self.d = [f'{datetime.now().date()}', self.transaction_type, self.transaction_amount,
                                  self.overdraft_balance, self.balance]
                        self.File_edit()
                        input('Enter any key to continue')
                        break

                    else:
                        self.balance = amount
                        print(
                            f'{self.balance} is deposited to your account, {self.overdraft_balance} is deducted as overdraft fee from your account')
                        self.overdraft_balance = 0
                        self.d = [f'{datetime.now().date()}', self.transaction_type, self.transaction_amount,
                                  self.overdraft_balance, self.balance]
                        self.File_edit()
                        input('Enter any key to continue')
                        break
                else:
                    self.balance += amount

                    print(f'''
                {self.transaction_amount} is deposited to your account 
                Your Balance : {self.balance}''')
                    self.d = [f'{datetime.now().date()}', self.transaction_type,
                              self.transaction_amount, self.overdraft_balance, self.balance]
                    self.File_edit()
                    input('Enter any key to continue')
                    break

        # --------------------------------------------------------------------------------------------------------------------------------#

    def File_read(self):
        with open(f'ADMIN\\{self.customer_data[0]}\\Checking_Account ', '+r') as f:
            # All the lines of the file will be loaded
            contents = f.readlines()
        self.overdraft_limit = contents[9].split(':')
        self.overdraft_limit = float(self.overdraft_limit[1].strip())
        self.credit_limit = contents[10].split(':')
        self.credit_limit = float(self.credit_limit[1].strip())
        self.last = contents[-1].strip('|').split('|')

        try:
            self.transaction_amount = float(self.last[2].strip(' '))
            self.balance = float(self.last[4].strip(" "))
            self.overdraft_balance = float(self.last[3].strip(' '))

        except:
            self.transaction_amount = 0
            self.balance = 0
            self.overdraft_balance = 0

    # --------------------------------------------------------------------------------------------------------------------------------#
    def File_edit(self):
        with open(f'ADMIN\\{self.customer_data[0]}\\Checking_Account ', 'a+') as f:

            f.write(f'''
|{self.d[0]:^16}|{self.d[1]:^24}|{self.d[2]:^26}|{self.d[3]:^24}|{self.d[4]:^23}|''')
   # --------------------------------------------------------------------------------------------------------------------------------#

    def Balance_Enquiry(self, username, report):
        back_to_main_menu = 1
        while back_to_main_menu:
            if report == 'Checking Account':
                with open(f'ADMIN//{username}//Checking_Account', 'r+') as f:
                    print(f.read())
                back_to_main_menu = input('''
        Press any key to go back to Main Menu...''')
                break
# --------------------------------------------------------------------------------------------------------------------------------#
# _______________________________________________________________ CHECKING ACCOUNT CLASS ENDS _______________________________________________________________________ #


class Saving_Account(Account):
   
    def __init__(self, username, saving_duration=0):
        self.saving_duration = saving_duration
        super().__init__(username)
        self.current_date = datetime.now().date()
    # --------------------------------------------------------------------------------------------------------------------------------#

    def Check_Wihtdrawal_Deadline(self):
        '''This method reads the deadline of saving duration from the file an asks user to seta new saving duration if the duration has ended'''
        with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt') as f:
            self.content = f.readlines()
        '''reading the saving duration limit/withdrawal deadline form the file'''
        saving_duration_row = eval(self.content[0])
        # saving_duration = saving_duration_row[1].split()
        date = saving_duration_row[-1]
        self.withdrawal_deadline = datetime.strptime(
            date, '%Y-%m-%d').date()  # Converting date into an object of date
        self.CalculateTimeDifference()
        '''If the saving duration is over than the user will be a choice to enter a new saving duration '''
        if self.withdrawal_deadline <= self.current_date:
            print(f"\nThe saving duration of your account has been ended.")
            time.sleep(0.8)
            choice = input(
                "\nDo you want to enter a new saving duration? [Press 'Enter key' if 'NO' and any other key if 'YES']: ")
            if choice != '':  # Getting and Saving new 'Saving Duration
                saving_duration = self.Take_Saving_Duration()
                self.Save_Saving_Duration(saving_duration)
                text = fontstyle.apply(
                    'Saving Duration has been updated successfully', 'blue')
                print(f'''                     
                {text}''')
                input('\nPress any key to continue...')
                os.system('cls')

            else:
                pass

    ''' --------------------------------Interface of Saving Account------------------------------------------'''

    def interface(self):
        text = fontstyle.apply(
            f"WELCOME TO YOUR SAVING ACCOUNT\n", 'bold/white')
        print(f'\n          {text:^70}')
        print('''WHAT DO YOU WANT TO DO?\n
     1.Deposit
     2.Withdraw
     3.View Balance Enquiry Report
     4.Update Saving Duration
     5.Go To Main Menu      
     6.Logout''')
        time.sleep(0.7)
        choice = input('''
                     Enter your choice: ''')
        if choice == '1':
            os.system('cls')
            self.Deposit()
        elif choice == '2':
            os.system('cls')
            self.Withdraw()
        elif choice == '3':
            os.system('cls')
            self.Balance_Enquiry(self.interface)
        elif choice == '4':
            os.system('cls')
            saving_duration = self.Take_Saving_Duration()
            self.Save_Saving_Duration(saving_duration)
            text = fontstyle.apply(
                'Saving Duration has been updated successfully', 'blue')
            print('''
                  Saving Duration has been updated successfully''')
            self.choose_action(self.interface)
        elif choice == '5':
            os.system('cls')
            return
        elif choice == '6':
            text = fontstyle.apply('Logging out....', 'cyan')
            print('\n', text, '\n')
            time.sleep(0.7)
            exit()
        else:
            print('''
                  Invalid Choice!!!
                  Please Enter a valid choice again''')
            time.sleep(0.8)
            os.system('cls')
            self.interface()
    '''--------------------------------------------------------------------------------------------------------------'''

    def CalculateTimeDifference(self):

        # This function calculate how many days have been passed between last sign in of customer
        date = None
        for i in self.content:
            row = eval(i)
            '''Getting the last date on which interest was debited in the account'''
            if row[0] == 'Interest debited':
                date = row[-3]
                self.time = row[-2]
        '''If now interest is debited till now that 'date' variable will remain None'''
        if date == None:
            '''Getting the date and on which user did his first transaction i.e., Signed up'''
            first_transaction = eval(self.content[1])
            date = first_transaction[-3]
            self.time = first_transaction[-2]
        self.interest_debit_date = datetime.strptime(date, '%Y-%m-%d').date()
        self.time_diff = self.current_date-self.interest_debit_date

        if self.time_diff.days >= 30:  # If one month has passed till the last signup/signin
            self.debit_interest()
    '''--------------------------------------------------------------------------------------------------------------'''

    def get_balance(self):
        '''Gets the total balance of the account'''
        try:
            with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt') as f:
                infile = f.readlines()
                last_transaction = eval(infile[-1])
                self.balance = float(last_transaction[-1])
        except:
            self.balance = 0  # IF user has signed up tha the balance will set to zero
    '''--------------------------------------------------------------------------------------------------------------'''

    def debit_interest(self):
        '''Calculates how many months has passed till the last signin/signup and debits the interest for each month
           No of months passed = No of timesthe interest has to be deposited  '''
        interest_count = self.time_diff.days // 30
        for i in range(interest_count):
            self.interest_debit_date += relativedelta(months=+1)
            if self.interest_debit_date < self.withdrawal_deadline:
                self.get_balance()
                # 0.02 is the interest rate
                interest = round(self.balance * 0.02, 3)
                self.balance += interest
                transaction_entry = ['Interest debited', interest, str(
                    self.interest_debit_date), self.time, round(self.balance, 2)]
                with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt', 'a+') as f:
                    f.write(str(transaction_entry)+'\n')
            else:
                return
    '''--------------------------------------------------------------------------------------------------------------'''

    def Take_Saving_Duration(self):
        '''This method takes the saving duration from the user.Saving duration limit is in between 12-60 months '''
        while True:
            try:
                print(
                    'REMEMBER: Saving duration should not be less than 12 months or grater than 60 months')
                time.sleep(1)
                saving_duration = int(input(
                    '\nFor how many months you want to save your money [Please enter integers like 1,2,3 etc]: '))
                if saving_duration > 60 or saving_duration < 12:
                    print("Your Saving duration must lie between 12-60 months")
                    time.sleep(0.7)
                    print('\nPlease re enter the saving duration')
                    continue
                else:
                    return saving_duration
            except:
                print('Please Enter no of months in integers')
                continue
    '''--------------------------------------------------------------------------------------------------------------'''

    def Save_Saving_Duration(self, saving_duration):
        '''This methods saves the saving duration given by the user in file '''
        self.get_balance()
        if self.balance < 100000:
            print('''
            Sorry we cannot update your Saving duration as your current balance is less than 100000''')
            self.interface()
        self.withdrawal_deadline = datetime.now().date()+relativedelta(months=+saving_duration)
        current_date=str(datetime.now().date())
        durationEntry=[str(saving_duration),current_date,str(self.withdrawal_deadline)]
        with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt', 'a+') as f:
            f.seek(0)
            infile = f.readlines()
            if infile == []:  # If the file is empty than simply write the saving duration
                f.write(str(durationEntry)+'\n')
            elif len(infile)==1:
                f.truncate(0)
                infile.insert(0, str(durationEntry)+'\n')
                [f.write(i) for i in infile]
            else:  # Otherwise,previous saving duration is erased and new is saved in the file
                f.truncate(0)
                del infile[0]
                infile.insert(0, str(durationEntry)+'\n')
                [f.write(i) for i in infile]
    '''--------------------------------------------------------------------------------------------------------------'''

    def Deposit(self, deposit=0):
        '''This method takes the deposit amount entered by the user ans write it in the file'''
        self.get_balance()

        def Deposit_transaction():
            '''This method is used to enter the transaction (deposit amount) of the user '''
            self.balance = round(self.balance+int(deposit), 2)
            time = datetime.strftime(datetime.now(), '%H:%M:%S')
            transaction_entry = ['Deposit', deposit, str( self.current_date), time, round(self.balance, 3)]
            with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt', '+a') as f:
                f.write(str(transaction_entry)+'\n')
            text = fontstyle.apply('Amount deposited successfully!!', 'blue')
            print(f'''
            {text}''')
        if deposit == 0:  # If no deposit amount has passed as an argument
            while True:
                try:
                    deposit = round(
                        float(input('\nEnter amount to be deposited in Rs/_: ')), 3)
                    break
                except:
                    print('Please enter amount in numbers ')
            Deposit_transaction()
            self.choose_action(self.interface)
        else:
            Deposit_transaction()
    '''--------------------------------------------------------------------------------------------------------------'''

    def Withdraw(self):
        '''This method takes the withdraw amount entered by the user (if the saving duration is ended) ans write it in the file'''
        if self.current_date > self.withdrawal_deadline:
            self.get_balance()
            while True:
                try:
                    withdraw = round(
                        float(input('\nEnter amount to be withdrawn in RS/_: ')))
                except:
                    print('Please enter amount in numbers')
                    continue
                account_balance = round(self.balance - withdraw, 2)

                if account_balance < 0:
                    print(
                        f'\nYou have run out of balance. You have Rs.{self.balance}/= only...')
                    choice = input(
                        "\nDo you want to withdraw amount again?[Press 'Enter key' if 'YES' and any other key if 'NO']:")
                    if choice == '':
                        continue
                else:
                    date = str(datetime.now().date())
                    time = datetime.strftime(datetime.now(), '%H:%M:%S')
                    transaction_entry = ['Withdraw', withdraw,
                                         date, time, round(account_balance, 3)]
                    with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt', 'a') as f:
                        f.write(str(transaction_entry) + '\n')
                    text = fontstyle.apply(
                        'Amount withdrawn successfully!!', 'blue')
                    print(f'''
                          {text}''')
                    break
        else:
            print('''                   Sorry!!!
                  
            You cannot withdraw any amount until the saving duration overs''')
        self.choose_action(self.interface)
    '''--------------------------------------------------------------------------------------------------------------'''

    def FirstSignup(self):
        '''This is the First interface showed to the customer on signup
           It will first take saving suration and deposit amount and then creates the account of the user'''
        text = fontstyle.apply('CREATING YOUR ACCOUNT!!!', 'bold/white')
        print(f'\n{text:^70}\n')
        saving_duration = self.Take_Saving_Duration()
        print('''          
                Deposit Some money!
              
            Remeber: You cannot debit less than 100000 on first deposit''')
        while True:
            deposit = int(input('\nENTER AMOUNT TO BE DEPOSITED IN RS/_: '))
            if deposit >= 100000:
                self.Deposit(deposit)
                self.Save_Saving_Duration(saving_duration)
                break
            else:
                print('''
                      Sorry! Amount cannot be less than 1000000 RS/_''')
                choice = input(
                    "Do you want to enter the amount again? [Press 'Enter key' if 'YES' and any other key if 'NO']: ")
                if choice == '':
                    continue
                else:
                    print('Your account is not created! ')
                    break
        text = fontstyle.apply(
            ' Your account has been created Successfully!', 'blue')
        print(f'''
            CONGRATULATIONS🎉🎉🎉 
                     
        {text} ''')
        time.sleep(0.9)
        print('''\n
            Going to Main Menu.....''')
        time.sleep(1)
    '''--------------------------------------------------------------------------------------------------------------'''
    @staticmethod
    def choose_action(func):
        '''This method is created to go back to the previous function'''
        time.sleep(1)
        print('''
    CHOOSE ACTION:   
    Press Enter to go back to previous Interface
    Press any other key to go to  Main Menu''')
        time.sleep(0.1)
        choice = input('\n ')
        if choice == '':
            func()
        else:
            return
    '''--------------------------------------------------------------------------------------------------------------'''

    def Balance_Enquiry(self, func):
        '''This function prints the basic information of the user and the balance/transaction report'''
        text1 = fontstyle.apply('BALANCE ENQUIRY REPORT', 'bold/white')
        text2 = fontstyle.apply('TRANSACTION DETAILS', 'bold/white')
        print(f'\n{text1:^70}\n')
        with open(f'ADMIN\\{self.customer_data}\\Basic_Info.txt') as f:
            content = f.readlines()
            content.pop()
            [print(i) for i in content]
        print("Interest rate: 20%")
        with open(f'ADMIN\\{self.customer_data}\\Saving_Account.txt') as f:
            infile = f.readlines()
        infile = [eval(i) for i in infile]
        saving_duraton_row=infile[0]
        saving_duration=f'{saving_duraton_row[0]} months  (from {saving_duraton_row[1]} to {saving_duraton_row[2]})'
        if len(infile) != 0:
            t = PrettyTable(['Transaction type', 'Amount',
                            'Date', 'Time', 'Total Balance'])
            [t.add_row(infile[i]) for i in range(1, len(infile))]
            print(f'\nSaving duration: {saving_duration}')
            print(f'\n{text2:^70}\n')
            print(t)
        time.sleep(0.5)
        self.choose_action(func)


# ______________________________________________ SAVING ACCOUNT CLASS ENDS _____________________________________________________ #

# _______________________________________________________________ LOAN ACCOUNT CLASS BEGINS _________________________________________________________________________ #


class Loan_Account(Account):

    # INTERFACE
    # --------------------------------------------------------------------------------------------------------------------------------#
    def Interface(self):
        '''CASE 1: If the customer has created loan account very first time; "Pay_loan_amount()" and "Balance_Enquiry()" must not appear.
           CASE 2: If the customer has already taken loan then the "Take_Loan()" option must not appear.
                CASE 2(a): If the customer pays installment timely.
                CASE 2(b): If the customer has not paid the installment of one month then in the next month he has to pay the previous 
                installment and current installment along with penalty.   
                CASE 2(c): If the customer has not paid monthly installment for more than 2 months then his account will be freezed.
        '''

        choice = 1
        while choice:
            # ________________________________________________ CASE 2 BLOCK BEGINS _______________________________________________ #

            if 'Loan_Account' in os.listdir(f'ADMIN\\{self.customer_data[0]}'):
                ''' 
                If the user has taken loan then we'll not allow him to take loan again because our bank provides 
                only one loan at a time. So, this 'if' block checks if the customer's
                loan account file exists, it means the user has already taken loan.
                '''

                # Retrieving data from file so that it can be used in further calculations
                self.File_Reader()
                self.current_date = datetime.now().date()

                # ___________________________________ CASE 2(c) BLOCK BEGINS __________________________________ #

                if self.difference > 90:
                    os.system('cls')
                    print('''ESC[31m
                                    
                          
                                    XXXX ---- ACCOUNT FREEZED! ---- XXXX
                          
        [NOTICE] You haven't paid loan installments, hence, your loan account is freezed and your mortgage has been siezed.
        Please visit the franchise or contact the administative department for more datail.
        ''')
                    back = 1
                    while back:
                        back = input('''
        Press any key to back''')
                        break  # to reach customer's interface

                # ___________________________________ CASE 2(c) BLOCK ENDS __________________________________ #

                else:

                    # ___________________________________ CASE 2(b) BLOCK BEGINS __________________________________ #

                    if 60 < self.difference <= 90:
                        os.system('cls')
                        last_installment_check = self.ending_date - self.current_date
                        if last_installment_check <= 30:
                            amount_with_penalty = self.monthly_installment + self.monthly_interest
                        else:
                            amount_with_penalty = self.monthly_installment*2 + self.monthly_interest
                            print(f'''
        LOAN ACCOUNT

        MAIN MENU
                    
        1. PAY LOAN AMOUNT
                                
            [NOTICE] You haven't paid your installment yet!!!
            Now you have to pay Rs.{amount_with_penalty}\= i.e. Previous installement + penalty + current installment. 

        2. BALANCE ENQUIRY
        3. EXIT''')

                            action = input('''
        Enter your Choice: ''')

                            if action == '1':
                                os.system('cls')
                                print('''
        PAY LOAN AMOUNT''')
                                while True:
                                    try:
                                        self.amount = int(input(f'''
        Please pay Rs.{amount_with_penalty}\=
        Input amount :  '''))
                                    except:
                                        print('''
        Invalid Input!!''')
                                    else:

                                        if self.amount == amount_with_penalty:
                                            self.amount_paid = self.amount - self.monthly_interest
                                            self.Pay_loan_amount()
                                            break  # to terminate this loop after payment of installment and to reach to loan interface loop
                                        else:
                                            print('''
        Please enter above mentioned amount before end of this month otherwise your account will be freezed''')
                                break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                            elif action == '2':
                                os.system('cls')
                                self.Balance_Enquiry(
                                    self.customer_data[0], 'Loan Account')

                            elif action == '3':
                                choice = input('''
        Press Enter key to exit...''')
                                os.system('cls')
                                break  # to break loan interface loop to reach customer interface from where it was called

                            else:
                                print('''
        Invalid Input!!''')

                # ___________________________________ CASE 2(b) BLOCK ENDS __________________________________ #

                # ___________________________________ CASE 2(a) BLOCK BEGINS __________________________________ #

                    elif 30 <= self.difference <= 60:
                        os.system('cls')
                        print('''
        LOAN ACCOUNT

        MAIN MENU
                
        1. PAY LOAN AMOUNT
        2. BALANCE ENQUIRY
        3. EXIT''')
                        action = input('''
        Enter your Choice: ''')

                        if action == '1':
                            os.system('cls')
                            print('''
        PAY LOAN AMOUNT''')
                            while True:
                                try:
                                    self.amount = int(input(f'''
        Please pay Rs.{self.monthly_installment}\=
        Input amount : '''))
                                except:
                                    print('''
        Invalid Input!!''')
                                else:
                                    if self.amount == self.monthly_installment:
                                        self.amount_paid = self.amount
                                        self.Pay_loan_amount()
                                        break  # to terminate this loop after payment of installment and to reach to loan interface loop
                                    else:
                                        print('''
        Your transaction has not been made. Please enter above mentioned amount before end of this month otherwise penalty will be charged!''')

                            break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                        elif action == '2':
                            os.system('cls')
                            self.Balance_Enquiry(
                                self.customer_data[0], 'Loan Account')

                        elif action == '3':
                            choice = input('''
        Press any key to exit...''')
                            os.system('cls')
                            break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                        else:
                            print('''
        Invalid Input!!''')

                    else:
                        print('''
        MAIN MENU
        
        [NOTICE] : You don't have to pay any installment now!
        1. BALANCE ENQUIRY
        2. EXIT''')
                        action = input('''
        Enter your Choice: ''')

                        if action == '1':
                            os.system('cls')
                            self.Balance_Enquiry(
                                self.customer_data[0], 'Loan Account')

                        if action == '2':
                            choice = input('''
        Press any key to exit...''')
                            os.system('cls')
                            break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                # ___________________________________ CASE 2(a) BLOCK ENDS __________________________________ #

        # _____________________________________________ CASE 2 BLOCK ENDS _____________________________________________ #

        # _____________________________________________ CASE 1 BLOCK BEGINS _____________________________________________ #
            else:
                os.system('cls')
                print('''
            LOAN ACCOUNT
                
            MAIN MENU
                
            1. TAKE LOAN
            2. EXIT''')
                action = input('''
            Enter your Choice: ''')

                if action == '1':
                    os.system('cls')
                    self.Take_Loan()
                    # break  # to break loan interface loop as loan is taken and to reach customer interface from where it was called

                elif action == '2':
                    choice = input('''
            Press Enter key...''')
                    os.system('cls')
                    # break  # to break loan interface loop and to reach customer interface from where it was called

                else:
                    print('''
            Invalid Input!!''')

        # _____________________________________________ CASE 1 BLOCK ENDS _____________________________________________ #

    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#
    def Balance_Enquiry(self, username, report):
        back_to_main_menu = 1
        while back_to_main_menu:
            if report == 'Checking Account':
                with open(f'ADMIN//{username}//Loan_Account', 'r+') as f:
                    print(f.read())
                back_to_main_menu = input('''
        Press any key to go back to Main Menu...''')
                break
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def File_Reader(self):
        '''This function reads the loan account file and returns the list containing previous date, amount paid, total amount paid,
            ending date, total loan amount, principle amount and loan duration.'''

        with open(f'ADMIN\\{self.customer_data[0]}\\Loan_Account', '+r') as f:
            # All the lines of the file will be loaded
            contents = f.readlines()
        self.principle_amount = contents[17].split(':')
        self.principle_amount = int(self.principle_amount[1].strip())
        self.monthly_interest = contents[18].split(':')
        self.monthly_interest = float(self.monthly_interest[1].strip())
        self.total_loan_amount = contents[19].split(':')
        self.total_loan_amount = float(self.total_loan_amount[1].strip())
        self.loan_duration = contents[20].split(':')
        self.loan_duration = int(self.loan_duration[1].strip())
        self.monthly_installment = contents[21].split(':')
        self.monthly_installment = float(self.monthly_installment[1].strip())
        self.ending_date = contents[23].split(':')
        self.ending_date = self.ending_date[1].strip()
        self.starting_date_ = contents[22].split(':')
        self.starting_date_ = self.starting_date_[1].strip()
        # The last line of the file will be stored in last_record. Strip() will remove '|' from either sides then split() will split the string on '|' and store each item as an element in the list.
        last_record = contents[-1].strip('|').split('|')

        ''' EXCEPTIONAL HANDLING: When the loan payment is being done, at the very first time, the last line of the file will have DATE, AMOUNT PAID etc.
            So, when the previous_total_amount_paid = 'TOTAL AMOUNT PAID' and we type cast it to integer ValueError: invalid literal for int() with base 10: 'TOTAL AMOUNT PAID' occur.
            In this regard exceptional handling is used to make previous_total_amount_paid = 0 as the error is raised.'''
        try:
            self.previous_amount_paid = float(last_record[1].strip(" "))
            self.previous_total_amount_paid = float(last_record[2].strip(" "))
            # previous date is stored without spaces at either sides.
            self.previous_date = last_record[0].strip(" ")

        except:
            self.previous_amount_paid = 0
            self.previous_total_amount_paid = 0
            self.difference = self.calculate_1st_difference()
        else:
            self.difference = self.calculate_date_difference()
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def calculate_1st_difference(self):
        self.current_date = datetime.now().date()
        self.starting_date = datetime.strptime(
            self.starting_date_, '%Y-%m-%d').date()
        return (self.current_date - self.starting_date).days

    def calculate_date_difference(self):
        self.current_date = datetime.now().date()
        self.previous_date = datetime.strptime(
            self.previous_date, '%Y-%m-%d').date()
        return (self.current_date - self.previous_date).days
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Calculate_interest(self):
        ''' principle amount = 10000
            loan duraion = 5 months
            monthly interest = 10000/5*0.04 = 80 '''
        return self.principle_amount / self.loan_duration * 0.04
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Calculate_monthly_installment(self):
        ''' principle amount = 10000
             loan duration = 5
             monthly interest = 80
             monthly installment = 10000/5 + 80 = 2080 '''
        return (self.principle_amount / self.loan_duration) + self.monthly_interest
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Calculate_Total_loan_amount(self):
        '''Eg. loan duration = 5 months
               monthly installment = 2080
               total loan amount = 5 * 2080 = 10400'''
        return self.loan_duration * self.monthly_installment
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def salary_check(self):
        return (self.salary/2) >= self.monthly_installment
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Pay_loan_amount(self):
        self.total_amount_paid = self.previous_total_amount_paid
        self.total_amount_paid += self.amount_paid
        current_record = [f'{datetime.now().date()}',
                          self.amount_paid, self.total_amount_paid]
        with open(f'ADMIN\\{self.customer_data[0]}\\Loan_Account', '+a') as f:
            f.write(f'''
______________________________________________________________________________________________________________________
|{current_record[0]:^32}|{current_record[1]:^41}|{current_record[2]:^43}|''')
        self.check_loan_payment()
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Take_Loan(self):
        choice = 1
        os.system('cls')

        print('''
                                        ```` LOAN APPLICATION ````
        ___________________________________________________________________________________________________''')
        while choice:

            # EXCEPTIONAL HANDLING : If user enter some incorrect input other than integer, our application can handle the errors.
            try:
                self.principle_amount = int(input('''
        Enter your loan amount in digits (example 👉️ 100000 ): '''))
                self.loan_duration = int(input('''
        REMEMBER: Loan duration cannot be greater than 60 months.
        Enter loan duration in months (example 👉️ 6 ): '''))

            except:
                print('Invalid Input!')

            else:  # If no error is raised the else block will execute

                # _______________________________ Take_Loan check 1: Loan Duration must be less than 60 ___________________________ #

                self.monthly_interest = self.Calculate_interest()
                # If loan duration is greater than 60 months
                if self.loan_duration > 60:
                    print('''
        Loan Duration cannot exceed from 60 months.''')
                    continue        # 'continue' will prevent user to proceed further unless the loan duration <= 60 months.

                # If loan duration is less than or equal to 60 months
                elif self.loan_duration <= 60:

                    # __________ Take_Loan check 2: Mortgage must be given such that its worth is greater than the principle amount ___________ #

                    if self.Mortgage():
                        # The monthly installment variable has nothing to do with the user it's just used in salary_check method
                        self.monthly_installment = self.Calculate_monthly_installment()

        # __________ Take_Loan check 3: The half of the Salary must be greater than or equal to monthly installment __________ #

                        self.salary = int(input('''
                                        ```` SALARY ````
        ____________________________________________________________________________________________
            
            Enter your salary: '''))
                        if self.salary_check():
                            self.total_loan_amount = self.Calculate_Total_loan_amount()
                            self.starting_date = datetime.now().date()
                            self.ending_date = self.starting_date + \
                                relativedelta(months=self.loan_duration)
                            self.Create_File()
                            print(f'''
        Congratulations!! Loan granted successfully.''')
                            time.sleep(1)
                            os.system('cls')
                            print(f'''
                                    ``` Loan Details ```
        ________________________________________________________________________________________
                                  
            PRINCIPLE AMOUNT: Rs.{self.principle_amount}\=
            TOTAL LOAN AMOUNT: Rs.{self.total_loan_amount}\=
            MONTHLY INTEREST : Rs.{self.monthly_interest}\=
            MONTHLY INSTALLMENT : Rs.{self.monthly_installment}\=
            LOAN DURATION: {self.loan_duration} Months
            STARTING DATE: {self.starting_date}
            ENDING DATE: {self.ending_date}
        __________________________________________________________________________________________''')
                            choice = input('''
        Press any key to go back to Main Menu...''')

                        else:
                            print('''
        Sorry, Loan cannot be granted! You donot possess sufficient salary.''')
                            choice = input('''
        Press any key to go back to Main Menu...''')
                    else:
                        print('''
        Sorry, Loan cannot be granted! You must need to mortgage anything in order to take loan.''')
                        choice = input('''
        Press any key to go back to Main Menu...''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Mortgage(self):
        choice = 1
        print('''
                                            ```` MORTGAGE ````
        ________________________________________________________________________________________________''')
        while choice:
            mortgage = input('''
        For taking the loan you need to mortgage any of the following things such that its worth must be greater than that of your principle amount:
            
        1. PROPERTY
        2. CAR
        3. GOLD
        4. NONE (Loan Application will be cancelled)

        REMEBER : If the loan is not repaid within the loan period, the bank has the authority to take the chosen item into its own possession.
        Enter the desired option: ''')

            time.sleep(1)
            # It contain mortgage data. All the specific data for the three different inputs will be stored in a common variable so that the MORTGAGE FILE WRITING BLOCK is written only once.
            self.mortgage_data = ''

            if mortgage in ['1', '2', '3']:

                if mortgage == '1':
                    cost = int(input('''
            Enter cost of the property (It must be greater than the principle amount): '''))
                    time.sleep(1)
                    # Cost check
                    if cost < self.principle_amount:
                        print('''
            The mortgage cost must be greater than the principle amount.''')
                        continue  # This statement will not let the code to proceed furter unless the the cost is greater.

                    address = input('''           
            Enter Address: ''')
                    self.mortgage_data = f'MORTGAGE TYPE : PROPERTY\nCOST: {cost}\nADDRESS: {address}'

                elif mortgage == '2':
                    cost = int(input('''
            Enter cost of the car: '''))
                    # Cost check
                    if cost < self.principle_amount:
                        print('''
            The mortgage cost must be greater than the principle amount.''')
                        continue  # This statement will not let the code to proceed furter unless the the cost is greater.

                    car_no = input('''           
            Enter Car Number: ''')
                    self.mortgage_data = f'MORTGAGE TYPE : CAR\nCOST: {cost}\nCAR NO.: {car_no}'

                else:
                    cost = int(input('''
            Enter cost of the gold: '''))
                    # Cost check
                    if cost < self. principle_amount:
                        print('''
            The mortgage cost must be greater than the principle amount.''')
                        continue  # This statement will not let the code to proceed furter unless the the cost is greater.

                    karat = int(input('''
            Enter gold's karat: '''))
                    self.mortgage_data = f'MORTGAGE TYPE : GOLD\nCOST: {cost}\nKARAT: {karat}'

                return True

            # If the user selects 'NONE' the self.Mortgage() will return False and loan will not be granted
            elif mortgage == '4':
                return False

            else:
                print('''
            Invalid Input''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Create_File(self):
        with open(f'ADMIN\\{self.customer_data[0]}\\Loan_Account', '+a') as f:
            f.write(f'''
                                        AMN ONLINE BANKING SYSTEM
_______________________________________________________________________________________________________________________
        
                                         ``` CUSTOMER DETAILS ```
ACCOUNT NAME: LOAN ACCOUNT                              
USERNAME: {self.customer_data[0]}           
CUSTOMER NAME: {self.customer_data[2]}                       
CNIC: {self.customer_data[3]}         
_______________________________________________________________________________________________________________________
        
                                         ``` MORTGAGE DETAILS ```
{self.mortgage_data}        
_______________________________________________________________________________________________________________________
                                         ``` LOAN DETAILS ```
PRINCIPLE AMOUNT: {self.principle_amount}
MONTHLY INTEREST: {self.monthly_interest}
TOTAL LOAN AMOUNT TO BE PAID: {self.total_loan_amount}                                  
LOAN DURATION IN MONTHS: {self.loan_duration}
MONTHLY INSTALLMENT : {self.monthly_installment} 
STARTING DATE: {self.starting_date}                                                  
ENDING DATE: {self.ending_date}
_______________________________________________________________________________________________________________________

                                        ``` LOAN PAYMENT RECORD ```
 ______________________________________________________________________________________________________________________            
|              DATE              |               AMOUNT PAID               |              TOTAL AMOUNT PAID            |''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def check_loan_payment(self):
        current_date = str(datetime.now().date())

        if current_date <= self.ending_date and self.total_amount_paid == self.total_loan_amount:
            print('''
        Congratulations!! Loan has been paid with in the duration. Please recieve your mortgage documents from the franchise.''')
            os.remove(f'ADMIN\\{self.customer_data[0]}\\Loan_Account')

        elif current_date < self.ending_date and self.total_amount_paid != self.total_loan_amount:
            print(f'''
        The monthly installment has been paid successfully. Hope you will pay the remaining amount on time as well.''')
    # --------------------------------------------------------------------------------------------------------------------------------#

# __________________________________________________ LOAN ACCOUNT CLASS ENDS ______________________________________________________ #

    # --------------------------------------------------------------------------------------------------------------------------------#

    def File_Reader(self):
        '''This function reads the loan account file and returns the list containing previous date, amount paid, total amount paid,
            ending date, total loan amount, principle amount and loan duration.'''

        with open(f'ADMIN\\{self.customer_data[0]}\\Loan_Account', '+r') as f:
            # All the lines of the file will be loaded
            contents = f.readlines()
        self.principle_amount = contents[17].split(':')
        self.principle_amount = int(self.principle_amount[1].strip())
        self.monthly_interest = contents[18].split(':')
        self.monthly_interest = float(self.monthly_interest[1].strip())
        self.total_loan_amount = contents[19].split(':')
        self.total_loan_amount = float(self.total_loan_amount[1].strip())
        self.loan_duration = contents[20].split(':')
        self.loan_duration = int(self.loan_duration[1].strip())
        self.monthly_installment = contents[21].split(':')
        self.monthly_installment = float(self.monthly_installment[1].strip())
        self.ending_date = contents[23].split(':')
        self.ending_date = self.ending_date[1].strip()
        self.starting_date_ = contents[22].split(':')
        self.starting_date_ = self.starting_date_[1].strip()
        # The last line of the file will be stored in last_record. Strip() will remove '|' from either sides then split() will split the string on '|' and store each item as an element in the list.
        last_record = contents[-1].strip('|').split('|')

        ''' EXCEPTIONAL HANDLING: When the loan payment is being done, at the very first time, the last line of the file will have DATE, AMOUNT PAID etc.
            So, when the previous_total_amount_paid = 'TOTAL AMOUNT PAID' and we type cast it to integer ValueError: invalid literal for int() with base 10: 'TOTAL AMOUNT PAID' occur.
            In this regard exceptional handling is used to make previous_total_amount_paid = 0 as the error is raised.'''
        try:
            self.previous_amount_paid = float(last_record[1].strip(" "))
            self.previous_total_amount_paid = float(last_record[2].strip(" "))
            # previous date is stored without spaces at either sides.
            self.previous_date = last_record[0].strip(" ")

        except:
            self.previous_amount_paid = 0
            self.previous_total_amount_paid = 0
            self.difference = self.calculate_1st_difference()
        else:
            self.difference = self.calculate_date_difference()
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def calculate_1st_difference(self):
        self.current_date = datetime.now().date()
        self.starting_date = datetime.strptime(
            self.starting_date_, '%Y-%m-%d').date()
        return (self.current_date - self.starting_date).days

    def calculate_date_difference(self):
        self.current_date = datetime.now().date()
        self.previous_date = datetime.strptime(
            self.previous_date, '%Y-%m-%d').date()
        return (self.current_date - self.previous_date).days
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Interface(self):
        '''CASE 1: If the customer has created loan account very first time; "Pay_loan_amount()" must not appear.
           CASE 2: If the customer has already taken loan then the "Take_Loan()" option must not appear.
                CASE 2(a): If the customer pays installment timely.
                CASE 2(b): If the customer has not paid the installment of one month then in the next month he has to pay the previous 
                installment and current installment along with penalty.   
                CASE 2(c): If the customer has not paid monthly installment for more than 2 months then his account will be freezed.
        '''

        choice = 1
        while choice:
            # ________________________________________________ CASE 2 BLOCK BEGINS _______________________________________________ #

            if 'Loan_Account' in os.listdir(f'ADMIN\\{self.customer_data[0]}'):
                ''' 
                If the user has taken loan then we'll not allow him to take loan again because our bank provides one 
                time loan and we can only take only one loan at a time. So, this 'if' block checks if the customer's
                loan account file exists, it means the user has taken loan.
                '''

                # Retrieving data from file so that it can be used in further calculations
                self.File_Reader()
                self.current_date = datetime.now().date()

                # ___________________________________ CASE 2(c) BLOCK BEGINS __________________________________ #

                if self.difference > 90:
                    os.system('cls')
                    print('''
                                    
                          
                                    XXXX ---- ACCOUNT FREEZED! ---- XXXX
                          
        [NOTICE] You haven't paid loan installments, hence, your loan account is freezed and your mortgage has been siezed.
        Please visit the franchise or contact the administative department for more datail.
        ''')
                    back = 1
                    while back:
                        back = input('''
        Press any key to back''')
                        break  # to reach customer's interface

                # ___________________________________ CASE 2(c) BLOCK ENDS __________________________________ #

                else:

                    # ___________________________________ CASE 2(b) BLOCK BEGINS __________________________________ #

                    if 60 < self.difference <= 90:
                        os.system('cls')
                        last_installment_check = self.ending_date - self.current_date
                        if last_installment_check <= 30:
                            amount_with_penalty = self.monthly_installment + self.monthly_interest
                        else:
                            amount_with_penalty = self.monthly_installment*2 + self.monthly_interest
                            print(f'''
        LOAN ACCOUNT

        MAIN MENU
                    
        1. PAY LOAN AMOUNT
                                
            [NOTICE] You haven't paid your installment yet!!!
            Now you have to pay Rs.{amount_with_penalty}\= i.e. Previous installement + penalty + current installment. 

        2. BALANCE ENQUIRY
        3. EXIT''')

                            action = input('''
        Enter your Choice: ''')

                            if action == '1':
                                os.system('cls')
                                print('''
        PAY LOAN AMOUNT''')
                                while True:
                                    try:
                                        self.amount = int(input(f'''
        Please pay Rs.{amount_with_penalty}\=
        Input amount :  '''))
                                    except:
                                        print('''
        Invalid Input!!''')
                                    else:

                                        if self.amount == amount_with_penalty:
                                            self.amount_paid = self.amount - self.monthly_interest
                                            self.Pay_loan_amount()
                                            break  # to terminate this loop after payment of installment and to reach to loan interface loop
                                        else:
                                            print('''
        Please enter above mentioned amount before end of this month otherwise your account will be freezed''')
                                break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                            elif action == '2':
                                os.system('cls')
                                self.Balance_Enquiry(
                                    self.customer_data[0], 'Loan Account')

                            elif action == '3':
                                choice = input('''
        Press Enter key to exit...''')
                                os.system('cls')
                                break  # to break loan interface loop to reach customer interface from where it was called

                            else:
                                print('''
        Invalid Input!!''')

                # ___________________________________ CASE 2(b) BLOCK ENDS __________________________________ #

                # ___________________________________ CASE 2(a) BLOCK BEGINS __________________________________ #

                    elif 30 <= self.difference <= 60:
                        os.system('cls')
                        print('''
        LOAN ACCOUNT

        MAIN MENU
                
        1. PAY LOAN AMOUNT
        2. BALANCE ENQUIRY
        3. EXIT''')
                        action = input('''
        Enter your Choice: ''')

                        if action == '1':
                            os.system('cls')
                            print('''
        PAY LOAN AMOUNT''')
                            while True:
                                try:
                                    self.amount = int(input(f'''
        Please pay Rs.{self.monthly_installment}\=
        Input amount : '''))
                                except:
                                    print('''
        Invalid Input!!''')
                                else:
                                    if self.amount == self.monthly_installment:
                                        self.amount_paid = self.amount
                                        self.Pay_loan_amount()
                                        break  # to terminate this loop after payment of installment and to reach to loan interface loop
                                    else:
                                        print('''
        Your transaction has not been made. Please enter above mentioned amount before end of this month otherwise penalty will be charged!''')

                            break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                        elif action == '2':
                            os.system('cls')
                            self.Balance_Enquiry(
                                self.customer_data[0], 'Loan Account')

                        elif action == '3':
                            choice = input('''
        Press any key to exit...''')
                            os.system('cls')
                            break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                        else:
                            print('''
        Invalid Input!!''')

                    else:
                        print('''
        MAIN MENU
        
        [NOTICE] : You don't have to pay any installment now!
        1. BALANCE ENQUIRY
        2. EXIT''')
                        action = input('''
        Enter your Choice: ''')

                        if action == '1':
                            os.system('cls')
                            self.Balance_Enquiry(
                                self.customer_data[0], 'Loan Account')

                        if action == '2':
                            choice = input('''
        Press any key to exit...''')
                            os.system('cls')
                            break  # to break loan interface loop as payment is done and to reach customer interface from where it was called

                # ___________________________________ CASE 2(a) BLOCK ENDS __________________________________ #

        # _____________________________________________ CASE 2 BLOCK ENDS _____________________________________________ #

        # _____________________________________________ CASE 1 BLOCK BEGINS _____________________________________________ #
            else:
                os.system('cls')
                print('''
            LOAN ACCOUNT
                
            MAIN MENU
                
            1. TAKE LOAN
            2. EXIT''')
                action = input('''
            Enter your Choice: ''')

                if action == '1':
                    os.system('cls')
                    self.Take_Loan()
                    # break  # to break loan interface loop as loan is taken and to reach customer interface from where it was called

                elif action == '2':
                    choice = input('''
            Press Enter key...''')
                    os.system('cls')
                    # break  # to break loan interface loop and to reach customer interface from where it was called

                else:
                    print('''
            Invalid Input!!''')

        # _____________________________________________ CASE 1 BLOCK ENDS _____________________________________________ #

    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Calculate_interest(self):
        ''' principle amount = 10000
            loan duraion = 5 months
            monthly interest = 10000/5*0.04 = 80 '''
        return self.principle_amount / self.loan_duration * 0.04
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Calculate_monthly_installment(self):
        ''' principle amount = 10000
             loan duration = 5
             monthly interest = 80
             monthly installment = 10000/5 + 80 = 2080 '''
        return (self.principle_amount / self.loan_duration) + self.monthly_interest
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Calculate_Total_loan_amount(self):
        '''Eg. loan duration = 5 months
               monthly installment = 2080
               total loan amount = 5 * 2080 = 10400'''
        return self.loan_duration * self.monthly_installment
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def salary_check(self):
        return (self.salary/2) >= self.monthly_installment
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Pay_loan_amount(self):
        self.total_amount_paid = self.previous_total_amount_paid
        self.total_amount_paid += self.amount_paid
        current_record = [f'{datetime.now().date()}',
                          self.amount_paid, self.total_amount_paid]
        with open(f'ADMIN\\{self.customer_data[0]}\\Loan_Account', '+a') as f:
            f.write(f'''
______________________________________________________________________________________________________________________
|{current_record[0]:^32}|{current_record[1]:^41}|{current_record[2]:^43}|''')
        self.check_loan_payment()
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Take_Loan(self):
        choice = 1
        os.system('cls')

        print('''
                                        ```` LOAN APPLICATION ````
        ___________________________________________________________________________________________________''')
        while choice:

            # EXCEPTIONAL HANDLING : If user enter some incorrect input other than integer, our application can handle the errors.
            try:
                self.principle_amount = int(input('''
        Enter your loan amount in digits (example 👉️ 100000 ): '''))
                self.loan_duration = int(input('''
        REMEMBER: Loan duration cannot be greater than 60 months.
        Enter loan duration in months (example 👉️ 6 ): '''))

            except:
                print('Invalid Input!')

            else:  # If no error is raised the else block will execute

                # _______________________________ Take_Loan check 1: Loan Duration must be less than 60 ___________________________ #

                self.monthly_interest = self.Calculate_interest()
                # If loan duration is greater than 60 months
                if self.loan_duration > 60:
                    print('''
        Loan Duration cannot exceed from 60 months.''')
                    continue        # 'continue' will prevent user to proceed further unless the loan duration <= 60 months.

                # If loan duration is less than or equal to 60 months
                elif self.loan_duration <= 60:

                    # __________ Take_Loan check 2: Mortgage must be given such that its worth is greater than the principle amount ___________ #

                    if self.Mortgage():
                        # The monthly installment variable has nothing to do with the user it's just used in salary_check method
                        self.monthly_installment = self.Calculate_monthly_installment()

        # __________ Take_Loan check 3: The half of the Salary must be greater than or equal to monthly installment __________ #

                        self.salary = int(input('''
                                        ```` SALARY ````
        ____________________________________________________________________________________________
            
            Enter your salary: '''))
                        if self.salary_check():
                            self.total_loan_amount = self.Calculate_Total_loan_amount()
                            self.starting_date = datetime.now().date()
                            self.ending_date = self.starting_date + \
                                relativedelta(months=self.loan_duration)
                            self.Create_File()
                            print(f'''
        Congratulations!! Loan granted successfully.''')
                            time.sleep(1)
                            os.system('cls')
                            print(f'''
                                    ``` Loan Details ```
        ________________________________________________________________________________________
                                  
            PRINCIPLE AMOUNT: Rs.{self.principle_amount}\=
            TOTAL LOAN AMOUNT: Rs.{self.total_loan_amount}\=
            MONTHLY INTEREST : Rs.{self.monthly_interest}\=
            MONTHLY INSTALLMENT : Rs.{self.monthly_installment}\=
            LOAN DURATION: {self.loan_duration} Months
            STARTING DATE: {self.starting_date}
            ENDING DATE: {self.ending_date}
        __________________________________________________________________________________________''')
                            choice = input('''
        Press any key to go back to Main Menu...''')

                        else:
                            print('''
        Sorry, Loan cannot be granted! You donot possess sufficient salary.''')
                            choice = input('''
        Press any key to go back to Main Menu...''')
                    else:
                        print('''
        Sorry, Loan cannot be granted! You must need to mortgage anything in order to take loan.''')
                        choice = input('''
        Press any key to go back to Main Menu...''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Mortgage(self):
        choice = 1
        print('''
                                            ```` MORTGAGE ````
        ________________________________________________________________________________________________''')
        while choice:
            mortgage = input('''
        For taking the loan you need to mortgage any of the following things such that its worth must be greater than that of your principle amount:
            
        1. PROPERTY
        2. CAR
        3. GOLD
        4. NONE (Loan Application will be cancelled)

        REMEBER : If the loan is not repaid within the loan period, the bank has the authority to take the chosen item into its own possession.
        Enter the desired option: ''')

            time.sleep(1)
            # It contain mortgage data. All the specific data for the three different inputs will be stored in a common variable so that the MORTGAGE FILE WRITING BLOCK is written only once.
            self.mortgage_data = ''

            if mortgage in ['1', '2', '3']:

                if mortgage == '1':
                    cost = int(input('''
            Enter cost of the property (It must be greater than the principle amount): '''))
                    time.sleep(1)
                    # Cost check
                    if cost < self.principle_amount:
                        print('''
            The mortgage cost must be greater than the principle amount.''')
                        continue  # This statement will not let the code to proceed furter unless the the cost is greater.

                    address = input('''           
            Enter Address: ''')
                    self.mortgage_data = f'MORTGAGE TYPE : PROPERTY\nCOST: {cost}\nADDRESS: {address}'

                elif mortgage == '2':
                    cost = int(input('''
            Enter cost of the car: '''))
                    # Cost check
                    if cost < self.principle_amount:
                        print('''
            The mortgage cost must be greater than the principle amount.''')
                        continue  # This statement will not let the code to proceed furter unless the the cost is greater.

                    car_no = input('''           
            Enter Car Number: ''')
                    self.mortgage_data = f'MORTGAGE TYPE : CAR\nCOST: {cost}\nCAR NO.: {car_no}'

                else:
                    cost = int(input('''
            Enter cost of the gold: '''))
                    # Cost check
                    if cost < self. principle_amount:
                        print('''
            The mortgage cost must be greater than the principle amount.''')
                        continue  # This statement will not let the code to proceed furter unless the the cost is greater.

                    karat = int(input('''
            Enter gold's karat: '''))
                    self.mortgage_data = f'MORTGAGE TYPE : GOLD\nCOST: {cost}\nKARAT: {karat}'

                return True

            # If the user selects 'NONE' the self.Mortgage() will return False and loan will not be granted
            elif mortgage == '4':
                return False

            else:
                print('''
            Invalid Input''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Create_File(self):
        with open(f'ADMIN\\{self.customer_data[0]}\\Loan_Account', '+a') as f:
            f.write(f'''
                                        AMN ONLINE BANKING SYSTEM
_______________________________________________________________________________________________________________________
        
                                         ``` CUSTOMER DETAILS ```
ACCOUNT NAME: LOAN ACCOUNT                              
USERNAME: {self.customer_data[0]}           
CUSTOMER NAME: {self.customer_data[2]}                       
CNIC: {self.customer_data[3]}         
_______________________________________________________________________________________________________________________
        
                                         ``` MORTGAGE DETAILS ```
{self.mortgage_data}        
_______________________________________________________________________________________________________________________
                                         ``` LOAN DETAILS ```
PRINCIPLE AMOUNT: {self.principle_amount}
MONTHLY INTEREST: {self.monthly_interest}
TOTAL LOAN AMOUNT TO BE PAID: {self.total_loan_amount}                                  
LOAN DURATION IN MONTHS: {self.loan_duration}
MONTHLY INSTALLMENT : {self.monthly_installment} 
STARTING DATE: {self.starting_date}                                                  
ENDING DATE: {self.ending_date}
_______________________________________________________________________________________________________________________

                                        ``` LOAN PAYMENT RECORD ```
 ______________________________________________________________________________________________________________________            
|              DATE              |               AMOUNT PAID               |              TOTAL AMOUNT PAID            |''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def check_loan_payment(self):
        current_date = str(datetime.now().date())

        if current_date <= self.ending_date and self.total_amount_paid == self.total_loan_amount:
            print('''
        Congratulations!! Loan has been paid with in the duration. Please recieve your mortgage documents from the franchise.''')
            os.remove(f'ADMIN\\{self.customer_data[0]}\\Loan_Account')

        elif current_date < self.ending_date and self.total_amount_paid != self.total_loan_amount:
            print(f'''
        The monthly installment has been paid successfully. Hope you will pay the remaining amount on time as well.''')
    # --------------------------------------------------------------------------------------------------------------------------------#

# __________________________________________________ LOAN ACCOUNT CLASS ENDS ______________________________________________________ #

# ____________________________________________________ CUSTOMER CLASS BEGINS _______________________________________________________ #


class Customer:
    # --------------------------------------------------------------------------------------------------------------------------------#
    def __init__(self, account_existence):
        # If the account exists login() will be called else signup() will be used to create new account
        self.exist = account_existence
        if self.exist == '1':
            self.login()
        else:
            self.signup()
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def File_Reader(self):
        ''' This function reads the Basic_Info.txt file and return the password and Accounts in a list.'''

        with open(f'ADMIN//{self.username}//Basic_Info.txt', 'r+') as f:
            # All the lines will be stored in a list as separate elements
            content = f.readlines()
            ''' The data strored in content[1] will split on the bases of ":" so we'll obtain another 
            list with two elements in it that are: Password and <password\n>'''
        self.password = content[1].split(':')
        # p[1] is <password\n> and strip will remove "\n"
        self.password = self.password[1].strip()
        self.customer_accounts = content[-1].split(':')
        self.customer_accounts = eval(self.customer_accounts[1])
        self.name = content[2].split(':')
        self.name = self.name[1].strip()
        self.cnic = content[3].split(':')
        self.cnic = self.cnic[1].strip()
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def login(self):
        choice = 1
        while choice:
            print('''
    SIGN IN''')
            self.username = input('''
    Enter Username: ''').upper()
            if self.username in os.listdir('ADMIN'):
                password = input('''
    Enter Password: ''')
                self.File_Reader()  # Retrieving data from Basic_info.txt file
                self.data = [self.username, self.password,
                             self.name, self.cnic, self.customer_accounts]
                if password == self.password:
                    # Loop will terminate at the end of this iteration
                    choice = input('''
    Press Enter to continue...''')
                    self.Interface()
                    break
                else:
                    print('''
    Invalid Password!!
    \n    Please Sign in Again''')
            else:
                time.sleep(0.5)
                os.system('cls')
                print('''
    User of this name do not exits!!
    \n    Please Sign in Again''')

    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def Account_Activation_Fees():
        ''' This method will check if the account activation fees has been paid or not and will prevent 
            the user from creating his account if he has not paid the amount.'''
        choice = 1
        print('''
    The account activation fee is Rs.1000/=''')
        while choice:   # This loop will not terminate until the amount is paid
            try:
                fees = int(input('''
    Please enter the amount: '''))
            except:
                print('Invalid input!')
            else:
                if fees == 1000:
                    print('''
        Congratulation Your account has been created!!!''')
                    choice = input('''
        Press any key to continue...''')    # Loop Termination
                else:
                    print('''
        Please pay the required amount to get your account created.''')

    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#
    def signup(self):

        # Creating New Account
        choice = 1
        while choice:
            print('''
    SIGN UP
    ACCOUNT CREATION
    ''')
            menu = input('''
    1. Create Account
    2. Go Back''')
            if menu == '1':
                self.username = input('''
        Enter Username: ''').upper()
                # Checking whether the username exists or not.
                if self.username in os.listdir('ADMIN'):
                    print('''
        This Username already exists! Try some different username...''')
                else:
                    self.password = input('''
        Enter Password: ''')
                    if self.password == '':
                        print(
                            'This field cannot be empty! Enter your credentials again')
                        continue
                    self.name = input('''
        Enter Name: ''').upper()
                    if self.name == '':
                        print(
                            'This field cannot be empty! Enter your credentials again')
                        continue
                    self.cnic = input('''
        Enter CNIC: ''')
                    if self.cnic == '':
                        print(
                            'This field cannot be empty! Enter your credentials again ')
                        continue
                    self.contact = input('''
        Enter Contact Number: ''')
                    if self.cnic == '':
                        print(
                            'This field cannot be empty! Enter your credentials again')
                        continue
                    self.data = [self.username, self.password,
                                 self.name, self.cnic, self.contact]

                    os.mkdir(f'ADMIN\\{self.username}')

                    while True:
                        print('''
            We have following accounts:
            1. CHECKING ACCOUNT
            2. SAVING ACCOUNT
            3. LOAN ACCOUNT''')
                        time.sleep(1)
                        self.accounts = input('''
            Choose the accounts you want to create by typing the numbers written before the account name.
            REMEMBER: Type the numbers separated by comma('). E.g. 👉️ 1,2,3 .
            Type Here: ''')
                        if self.accounts == '':
                            print('This field cannot be empty!')
                            continue

                        self.accounts_list = [i for i in self.accounts.split(
                            ',')]
                        # List Comprehension (E.g. '1,2,3' 👉️ ['1','2','3'])
                        self.accounts_list = set(self.accounts_list)
                        for i in self.accounts_list:
                            if i not in ['1', '2', '3']:
                                print('You have entered some invalid value')
                                break
                        else:

                            self.customer_accounts = []
                            time.sleep(0.5)
                            os.system('cls')
                            if '1' in self.accounts_list:
                                print('''
                ```` Account Activation fee for Checking Account ````''')
                                self.Account_Activation_Fees()
                                self.checking_account = Checking_Account(
                                    self.data)
                                self.customer_accounts.append(
                                    'Checking Account')
                            if '2' in self.accounts_list:
                                print('''
                ```` Account Activation fee for Saving Account ````''')
                                self.customer_accounts.append('Saving Account')
                                self.saving_account = Saving_Account(
                                    self.data[0])
                                self.saving_account.FirstSignup()

                            if '3' in self.accounts_list:
                                print('''
                ```` Account Activation fee for Loan Account ````''')
                                self.Account_Activation_Fees()
                                self.loan_account = Loan_Account(self.data)
                                self.customer_accounts.append('Loan Account')

                            with open(f'ADMIN\\{self.username}\\Basic_Info.txt', 'a+') as f:
                                f.write(
                                    f"Username: {self.data[0]}\nPassword: {self.data[1]}\nName: {self.data[2]}\nCNIC: {self.data[3]}\nACCOUNTS: {self.customer_accounts}")
                            # On pressing Enter key the value of choice will become "" and so the while loop will terminate at the end of this iteration
                            os.system('cls')
                            # After setting up the credentials signup_interface() will be called to select account type
                            self.Interface()
                            break
            elif menu == '2':
                break
            else:
                print('''
        Invalid Input''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def Interface(self):    # Interface after sign up and sign in
        choice = 1
        os.system('cls')
        print(f'''
    Hi, {self.username}. Welcome To our online banking application :))''')
        time.sleep(1)
        while choice:
            print('''
    MAIN MENU

    1. VIEW PROFILE
    2. MY ACCOUNTS
    3. LOGOUT''')
            time.sleep(1)
            action = input('''
    Enter Your Choice: ''')
            if action == '1':
                os.system('cls')
                self.View_Profile()
            elif action == '2':
                os.system('cls')
                self.My_Accounts()
            elif action == '3':
                os.system('cls')
                text = fontstyle.apply('''
                                                                    LOGGING OUT
                                            
                                                ```` GOOD BYE!! HOPE YOU ENJOYED OUR SERVICES :)) `````''', 'blue/bold')
                print(text, '\n')
                exit()
            else:
                print('''
    Invalid choice!!''')
    # --------------------------------------------------------------------------------------------------------------------------------#

    # --------------------------------------------------------------------------------------------------------------------------------#

    def View_Profile(self):
        with open(f'ADMIN\\{self.username}\\Basic_Info.txt', 'r+') as f:
            print('''
                                ```` MY PROFILE ````
    ______________________________________________________________________________''')
            time.sleep(1)
            print(f'''{f.read()}
            
    _______________________________________________________________________________''')
        back = 1
        while back != '':
            back = input('''
    Press Enter key to go back to Main Menu...''')
            os.system('cls')

    def My_Accounts(self):
        choice = 1
        while choice:
            print('''\033[1;34;40m
        MY ACCOUNTS\033[1;33;40m''')
            dic = {'C': 'Checking Account',
                   'S': 'Saving Account', 'L': 'Loan Account'}
            for i in range(len(self.customer_accounts)):
                print(f'''
        {i+1}. {self.customer_accounts[i]}''')
            print('''
        OR Press Enter to go back to Main Menu''')
            option = input('''\033[1;36;40m
        Please write 'C/c', 'S\s' and 'L/l' to go into  'Checking Account', 'Saving Account' and 'Loan Account' respectively.
        (E.g. 👉️ If you want to open checking account then type c)
        NOTE: You can type only one account at a time.
        Type Here: \033[1;33;40m''').upper()

            if option == '':  # As the user presses Enter key, choice becomes '' and the loop wil terminate
                os.system('cls')
                choice = ''

            elif option in dic:
                if dic[option] not in self.customer_accounts:
                    print(f'''\033[1;31;40m
        You donot have {dic[option]}.''')

                elif option == 'C':
                    os.system('cls')
                    object = Checking_Account(self.data)
                    object.Interface()
                    # to break my accounts interface loop as given account's interface is visited and to reach customer interface from where it was called
                    break
                elif option == 'S':
                    os.system('cls')
                    object = Saving_Account(self.data[0])
                    object.Check_Wihtdrawal_Deadline()
                    object.interface()
                    # to break my accounts interface loop as given account's interface is visited and to reach customer interface from where it was called
                    break
                elif option == 'L':
                    os.system('cls')
                    object = Loan_Account(self.data)
                    object.Interface()
                    # to break my accounts interface loop as given account's interface is visited and to reach customer interface from where it was called
                    break

            else:
                print('''\033[1;31;40m
        Invalid Input!!''')
    # --------------------------------------------------------------------------------------------------------------------------------#

# __________________________________________________________ CUSTOMER CLASS ENDS ________________________________________________________ #


# ___________________________________________________________ DRIVER CODE BEGINS _________________________________________________________ #
choice = 1
while choice:
    with open('HEADING.txt', 'r+') as f:
        heading = f.read()
    print(f'''\033[1;36;40m
    
{heading}''')
    time.sleep(0.9)
    text2 = fontstyle.apply("PROCEED AS:", 'bold')
    print(f'''    {text2}
          
    1.Customer
    2.Admin 
    3.Exit''')
    option = input('''
    Enter your choice [Enter the number written before the options]: ''')

    if option == '1':
        while True:
            print('''
            1. Already have an account ~ SIGN IN
            2. Create new account ~ SIGN UP
            3. Go back ''')
            time.sleep(0.5)
            account_existence = input('''
            Enter your choice: ''')

            if account_existence in ['1', '2']:
                os.system('cls')
                c = Customer(account_existence)

            elif account_existence == '3':
                os.system('cls')
                break
            else:
                print('''
            Invalid Choice!!''')

    elif option == '2':
        user_choice=input('''
            Press 'Enter' to login
            Press any other key to go back:   ''')
        if user_choice!='':
            continue
        admin = Admin()
        admin.Signin()
    elif option == '3':
        os.system('cls')
        text = fontstyle.apply('''
                                                            LOGGING OUT
                                    
                                        ```` GOOD BYE!! HOPE YOU ENJOYED OUR SERVICES :)) `````''', 'blue/bold')
        print(text, '\n')
        exit()

    else:
        print('''
        Please enter a valid choice''')
        time.sleep(0.8)
        os.system('cls')
# _______________________________________________________ DRIVER CODE ENDS _______________________________________________________ #
