import matplotlib.pyplot as plt


def compound_info(): # asks for user compound term type and returns this as a number of terms per year and a term name.
    while True:
        term_length = str(input("Is it Daily, monthly or yearly compounding? ")).strip().lower() #Asks the Q and lets user answer. strip removes any spaces or special characters, lower makes the answer lower case
        if term_length == "monthly": #If user inputs monthly, term_length is set to month and term number is equal to 12 as this will be used to calculate monthly interest rate
            return "month", 12
    
        elif term_length == "yearly": #same as previous if command, when user returns something other than monthly, the prev. step will skip and come to this
            return "year", 1

        elif term_length == "daily": #same again
            return "day", 365

        else: #if user enters anything but monthly, daily or yearly it will come to this step
            print("Invalid input please respond with daily, monthly or yearly") #lets user know input was invalid
            term_length = "" #sets term_length back to empty so loop will run again
def scenario_details(term_type): #This function gathers mroe information from user, including initial value, interest rate and amount of terms calcualting for.
    while True:
        initial_input = float(input("What is your starting value? ")) #allows user to input starting cash value
        interest_annual = float(input("What is your annual interest rate as a percentage? ")) #asks user to input annual interest rate
        term_amount = int(input("How many " + term_type + "s would you like to calculate for? ")) #uses newly defined varaible to ask question of the number of terms to be calculated
        return initial_input, interest_annual, term_amount #returns these values so they can alter be used in calculations
def contribution_info(): #gathers information from user regarding if there is additional contributions and information about these contributions
    while True: #starts a loop for while contribution check is empty to run the following program
        contribution_check = input("Any regular additional contributions? Yes/No ").strip().lower() #asks user to input yes or no, note that contribtutiion_check is no longer empty
        if contribution_check == "yes": #check if user responded 'yes'
            contribution_type = input("Is the contribution daily, weekly, monthly or yearly? ").strip().lower() #if user responded yes they will be asked the contribution frequency
            while contribution_type not in( "daily", "weekly", "monthly", "yearly"): #starts another loop if the input is invalid
                print("Invalid input, please respond daily, weekly, monthly or yearly") #prints message to say input is invalid
                contribution_type = input("Is the contribution daily, weekly, monthly or yearly? ").strip().lower() #repormpts the user to input the contributuion frequency
            if contribution_type in ("daily", "weekly", "monthly", "yearly"): #checks if it is equal to one of 4 types of contribution
                additional_contribution = float(input(contribution_type + " contribution amount: ")) #if so it prompts user for the contribution amount
        elif contribution_check == "no": #if user responds no, this program will run
                additional_contribution = float(0.0) #contribution is set to zero
                contribution_type = "No additional contribution"
        else:
            print("Invalid input. Please respond yes or no") #if user responds anything other than yes or no the next line will run
        return additional_contribution, contribution_type, contribution_check #defines and returns these values to alter be used in calcualtions
def contribution_figs(contribution_type): #similar tot he first function, it just takes the contribution type and gives it a type and number
        while True:
            if contribution_type == "daily": #each of these are used to set the frequency they occur at per year e.g. days is 365 as there are 365 days in the year
                return "day", 365
            elif contribution_type == "weekly":
                return "week", 52
            elif contribution_type == "monthly":
                return "month", 12
            elif contribution_type == "yearly":
                return "year", 1
            else:
                return contribution_term_type, contribution_term_number
def pre_calculations(interest_annual, term_number, contribution_term_number, term_amount): #takes these values and calculates the following...
    while True:
        acting_interest = (interest_annual/term_number) #converts annual interest to monthly or daily interest rate or stays yearly
        acting_interest = ((acting_interest/100) + 1) #converts to a decimal then adds one to give full multiplier value
        contribution_interest = (interest_annual/contribution_term_number) #same calculation as before for acting_interest, but defining contribution interest as different as ther terms are independent
        contribution_interest = ((contribution_interest/100) + 1) #puts it in decimal form +1 e.g. 5% --> 1.05
        contribution_frequency = term_amount*(contribution_term_number/term_number) #used to convert the original compound length in x units to the contribution time length in y units
        return acting_interest, contribution_interest, contribution_frequency
def compound_interest_calculations(additional_contribution, contribution_interest, initial_input, contribution_frequency,
                                    acting_interest, term_amount, term_type): # calculates compound interest including for contributions
   while True: #while True is always equal to true so this loop will always run and only end when a value is returned
       first_term = "" #empty variable called first_term, use this to star tthe next while loop
       while first_term == "": #while the first_term variable is empty
            first_term = str(input("Do you want to appply contribution to the first " + term_type + "? ")).strip().lower()#askes for user input
            if first_term == "yes": #in this case, we will calculate the interest using the standard formula
                    contribution_compound = (additional_contribution * ((contribution_interest**contribution_frequency) - 1))/(contribution_interest - 1) #calculating the new total of all contributions compounded
                    compound_total = (initial_input*(acting_interest**term_amount)) + contribution_compound #calculates the initial input compounded and adds it to the contributions to give new total
                    deposit_total = (initial_input + (contribution_frequency * additional_contribution)) #calculates total deposited by user
            elif first_term == "no": # in this case we will calculate normally, then subtract one contribution form deposit and one compounded input from the compounding total
                    contribution_compound = (additional_contribution * ((contribution_interest**contribution_frequency) - 1))/(contribution_interest - 1) #calculating the new total of all contributions compounded
                    compound_total = ((initial_input*(acting_interest**term_amount)) + contribution_compound) - (additional_contribution * (acting_interest**term_amount)) #calculates the initial input compounded and adds it to the contributions to give new total
                    #we minus the additional contribution times the acting interest to the power of the term amount, since if we contribute on the first term
                    # it will be compounded over all the terms that compounding happens.
                    deposit_total = ((initial_input + (contribution_frequency * additional_contribution)) - additional_contribution) #calculates total deposited by user
            else:
                print("Invalid input, Please respond yes or no.") 
                first_term = ""   
       print("")
       print("Your total deposits are: £" + str(deposit_total)) #prints total deposits
       print("Your new total is: £" + str(round(compound_total, 2))) #prints a message saying your new total is: and gives the total rounded to the nearest 2 decimal places.
       print("You have earned £" + (str(round(compound_total - deposit_total, 2))) + " interest.") #calculates teh difference between beopists and balance
       increase_percentage = (100 * (compound_total/deposit_total)) - 100 #calculates the percentage increase
       print("This is an increase of " + str(round(increase_percentage, 2)) + "%" + " on your total deposits.") #prints the percentage increae
       print("And a increase of " + str(round(((100 * (compound_total/initial_input)) - 100), 2)) + "%" + " on your initial input.")
       effective_annual_rate = ((1 + ((interest_annual/100)/term_number))**term_number) - 1 #calcualtes effective annual rate(EAR)
       print("Your effective annual interest rate is: " + str(round(100 * effective_annual_rate, 5)) + "%") #prints the EAR
       print("")
       print("Please note that the above is an estimate based on idealistic conditions and as such has a deviation of up to 0.5" + " % " + "either side.")
       print("If you want to view the a more acurate estimate based on term-by-term growth, please select 'yes' when asked if you would like to view the table.")
       return first_term
def find_num_terms(contribution_check, contribution_frequency, first_term): #this function creates a list of numbers for the maximum amount of terms
    #where 1 represents a term with a contribution and 0 represents a term without contributions
    while True:
        term_list = [] #creates a new variable and sets it as an empty list
        range_finder = max(contribution_frequency, term_amount) #this finds the highest number out of the term amount and contribution frequency
                                                                #It will help define how long the list should be as we need to ensure list size >= number of contributions
                                                                #For example, if we only have 12 integers in the list, denoting a month each, but we contribute daily or weekly,
                                                                #We would be unable to mark the days that should have contribution as we can only deal with the months
        if first_term != "yes": #if first term is anything other than yes, range_start is set to 2 and term_list starts with a 0 at the first iteration
            range_start = 2
            term_list.append(0)
        else:
            range_start = 1
        if contribution_check == "yes".strip().lower(): #check if there is additional contribution
            for term in range(range_start, (round(range_finder) + 1)): #runs a loop for each number from range_start to the range finder +1 (+1 allows it to also calculate the last term itself) 
                                                    #e.g. if the range is 12 months, this will run from 1 to 12 but not including 12, so we add 1 to include 12
                if term % (round(range_finder/contribution_frequency)) == 0: #range_finder//contribution_frequency gives us the amount of time between each contribution
                                                                        #as an example, if there is 730 day period and we contribute monthly, this is 24 times in total ((730/365) * 12)
                                                                        #so then dividing the period by the amount of contributions give us the time between each contribution
                                                                        #in this example it would be 730/24 = 30.4 . We use // to do floor division which will round down to nearest interger
                                                                        #in this case the nearest integer down is 30
                                                                        #then it checks if each term in the list when divided by 30 gives 0 remainder...
                
                    term_list.append(1) #if there is no remainder, we add a 1 into the list
                else:
                    term_list.append(0) #if there is a remainder, then the if term is not satisfied and we do not contribute this day so we add a 0 in the list.
        else: #if there is no additional contribution...
            for term in range(range_start, (round(range_finder + 1))): #for each term in range
                term_list.append(0) #add a 0 to the list
        return term_list
def print_table(acting_interest, contribution_interest, initial_input, contribution_term_number, term_number, term_type, term_list):
    #Used to print the table with table formatting for printing in terminal
    while True:
        running_interest = min(acting_interest, contribution_interest) #chooses the smaller of the 2 interest rates to determine which one is used for the terms used in our list
        running_total = initial_input #assign new variable that will be used to keep track of our total over time
        running_deposit = initial_input #same but for deposits
        term_counter = 0 #new variable used to count up the amount fo terms over time
        interest_earned = 0 #same but for interest

        acting_term_type = "" #new variable called acting_term_type, will be used to assign the term type based on which is larger
        if contribution_term_number > term_number: #if the contribtuion term nuymber is larger than the term number...
            acting_term_type = contribution_term_type #the acting term type should be equal to the contribution term type
        else:
            acting_term_type = term_type #else it should stay as the term type

        term_table_type = acting_term_type.capitalize() #new variable used in the next for loop to change the term_type so that is is capitalised at the star tof the word

        term_printer = term_table_type + " " + str(term_counter) #New variable term_printer which will print the capitalised term type ad the term cunter e.g. Month 1

        cumulative_total = []
        cumulative_deposit = []
        stored_interest = []
        term_iterations = []

        print("")
        table_checker = ""
        while table_checker == "":
            table_checker = input("Would you like to see term-by-term growth in table format? (yes/no) ").strip().lower()
            if table_checker == "yes":
                print("")
                header = ("| " + "Term Number" + " | " + "Deposit per term" + " | " + "Total Deposited" + " | " + "Interest Earned" + " | " + "New Total Value" + " |") #makes the string for the header
                print(header) # prits header
                underline = "" #new variable called underline
                for char in header: #for loop, so for every character in 'header' this will run
                    if char == "|": #if the character is equal to "|" the it will add a "|" in the underline string
                        underline += "|"
                    else: #if no, it will add a dash instead
                        underline += "-"
                print(underline) #prints underline
            
                for integer in term_list: #checks for each integer in the list for a 1 or a 0
                    if integer == 1: #if the integer is 1
                        running_total = (running_total*(running_interest)) + additional_contribution #running total is equal to the previous running total * the interst rate plus the contribution
                        running_total = round(running_total, 2) #rounds running total to nearest 2 decimal places
                        running_deposit += additional_contribution #running deposit is the pervious running deposit plus the contribution
                        term_counter += 1 #adds one to previousvalue of term counter, ensuring it goes up by 1 each itereation
                        interest_earned = round((running_total - running_deposit), 2) #calcualtes inerest earned and rounds to neares 2 DP
                        term_printer = term_table_type + " " + str(term_counter) #updates term_printer
                        cumulative_total.append(running_total)
                        cumulative_deposit.append(running_deposit)
                        stored_interest.append(interest_earned)
                        term_iterations.append(term_counter)

                        print("|", term_printer + " " * (11 - (len(term_printer))), "|", #prints each item under respective header and tehn is follwoed by an amount of spcaes equal to
                            "£" + str(additional_contribution) + " " * (16 - (len(str(additional_contribution)) + 1)), "|",
                            "£" + str(running_deposit) + " " * (15 - (len(str(running_deposit)) + 1)), "|", #the length og the header minus the total length of the item string plus one for the symbol
                            "£" + str(interest_earned) + " " * (15 - (len(str(interest_earned)) + 1)), "|",#this ensures that the "|" characters are always in the same palce
                            "£" + str(running_total) + " " * (15 - (len(str(running_total)) + 1)), "|")
                    else:                                                                      #when the integer is 0
                        running_total = (running_total*(running_interest)) # running total is equal to previous running total times by the running interest rate
                        running_total = round(running_total, 2)
                        term_counter += 1
                        interest_earned = round((running_total - running_deposit), 2)
                        term_printer = term_table_type + " " + str(term_counter)
                        cumulative_total.append(running_total)
                        cumulative_deposit.append(running_deposit)
                        stored_interest.append(interest_earned)
                        term_iterations.append(term_counter)

                        print("|", term_printer + " " * (11 - (len(term_printer))), "|", #prints each item under respective header and tehn is follwoed by an amount of spcaes equal to
                            " " * 16, "|",
                            "£" + str(running_deposit) + " " * (15 - (len(str(running_deposit)) + 1)), "|", #the length og the header minus the total length of the item string plus one for the symbol
                            "£" + str(interest_earned) + " " * (15 - (len(str(interest_earned)) + 1)), "|",#this ensures that the "|" characters are always in the same palce
                            "£" + str(running_total) + " " * (15 - (len(str(running_total)) + 1)), "|")
            elif table_checker == "no":
                pass
            else:
                print("Invalid input please respond yes or no ")
                table_checker = ""
        return term_iterations, cumulative_total, term_table_type, cumulative_deposit, table_checker
def print_graph(term_iterations, cumulative_total, term_table_type, cumulative_deposit, table_checker):#prints graph
    while table_checker == "yes":
        print("")
        graph_checker = ""
        while graph_checker == "":
            graph_checker = input("Would you like this displayed in graph form? (yes/no) ").strip().lower()
            if graph_checker == "yes":
                plt.figure(figsize=(12, 6))#sets graph to a size of 12 by 6 inches

                plt.plot(term_iterations, cumulative_total, label = 'Total Value Over Time (£)', color = 'green') # plots green line of the total over time
                plt.plot(term_iterations, cumulative_deposit, label = 'Cumulative Deposits Over Time (£)', color = 'blue')#blue line of deposits over time

                plt.title("Compound Interest Growth Over Time") #give graph title
                plt.xlabel(term_table_type + " Number")#labels x axis
                plt.ylabel("Amount (£)")#labels y axis
                plt.legend()#gives info box for line colours meaning
                plt.grid(True)#puts grid lines on graph
                plt.tight_layout()#adjust size so it is better formatted
                plt.show()#prints graph
                pass
            elif graph_checker == "no":
                pass
            else:
                print("Invalid input please respond yes or no ")
                graph_checker = ""
        return

term_type, term_number = compound_info()

initial_input, interest_annual, term_amount = scenario_details(term_type)

additional_contribution, contribution_type, contribution_check = contribution_info()


contribution_term_type, contribution_term_number = contribution_figs(contribution_type)
acting_interest, contribution_interest, contribution_frequency = pre_calculations(interest_annual, term_number, contribution_term_number, term_amount)

first_term = compound_interest_calculations(additional_contribution,
 contribution_interest, initial_input, contribution_frequency, acting_interest, term_amount, term_type)

term_list = find_num_terms(contribution_check, contribution_frequency)

term_iterations, cumulative_total, term_table_type, cumulative_deposit, table_checker = print_table(acting_interest,
                 contribution_interest, initial_input, contribution_term_number, term_number, term_type, term_list)

print_graph(term_iterations, cumulative_total, term_table_type, cumulative_deposit, table_checker)



