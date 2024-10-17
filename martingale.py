""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np 
import matplotlib.pyplot as plt 		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "tb34"  # replace tb34 with your Georgia Tech username.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 900897987  # replace with your GT ID number  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  

def experiment_1(num_episodes, num_spins, win_prob) : 
    dimension = [num_episodes, num_spins + 1] # add one to num_spins of 0 to the loop correctly
    ep_winning = np.zeros(dimension) #result of gambling 

    ##run the spins and store the spins for each episodes##
    for i in range(num_episodes) :
        spin_counter = 1 # each episodes contain 1000 spins plus the initial value. Skipping the first 0
        while ep_winning[i][spin_counter - 1] < 80 and spin_counter < dimension[1] :
            bet_amount = 1
            won = False
            while not won and spin_counter < dimension[1] : 
                #bet on black
                won = get_spin_result(win_prob)
                if won :
                    ep_winning[i][spin_counter] =  ep_winning[i][spin_counter - 1] + bet_amount
                if not won :
                    ep_winning[i][spin_counter] =  ep_winning[i][spin_counter - 1] - bet_amount
                    bet_amount = bet_amount * 2
                spin_counter += 1

        while ep_winning[i][spin_counter - 1] >=80 and spin_counter < dimension[1] :
            ep_winning[i][spin_counter] = 80
            spin_counter +=1

        
    t_winnings = np.transpose(ep_winning) #transpose to make analysis spin centric

    return t_winnings

# experiment_1(10, 1000, 0.60)


                                ##Experiment 2##
##Pseudo code:
#Episode_winning = $0
#While episode_winning < 80$ and episode_winning > -256$:
    #spin_counter = 1
    #won = False
    #bet_amount = 1
    #while not won:
        #bet_amount on black
        #wont = get_result(win_prob)
        #if won == True:
            #episodes_winnings += bet_amount
        #else :
            #episodes_winnings -= bet_amount
            #if bet_amount > episodes_winning:
                #bet_amount = episodes_winning
            #else :
                #bet_amount *=2 
            
        #spin_counter +=1
    # while episode_winnings[i][spin_counter - 1] >= 80 and spin_counter < dim[1]:
    #         episode_winnings[i][spin_counter] = 80
    #         spin_counter += 1

    # while episode_winnings[i][spin_counter - 1] <= -256 and spin_counter < dim[1]:
    #         episode_winnings[i][spin_counter] = -256
    #         spin_counter += 1


def experiment_2(num_spins, num_episodes, win_prob) :
    dimension = [num_spins + 1, num_episodes] #setting up dimensions
    
    #winnning space
    ep_winnings = np.zeros(dimension)

    ##Running the spins
    for i in range(num_episodes) :
        ep_winnings[0][i] = 256
        spin_counter = 1
        while 0 < ep_winnings[spin_counter - 1][i] < 80 + 256 and spin_counter < dimension[0]:
            #betting
            won = get_spin_result(win_prob)
            while not won and spin_counter < dimension[0]:
                won = False
                bet_amount = 1
                won = get_spin_result(win_prob)
                if won :
                    ep_winnings[spin_counter][i] = ep_winnings[spin_counter - 1][i] + bet_amount
                else :
                    ep_winnings[spin_counter][i] = ep_winnings[spin_counter - 1][i] -  bet_amount
                    if bet_amount * 2 > ep_winnings[spin_counter - 1][i]: 
                        bet_amount = ep_winnings[spin_counter][i] - 1 #only bet total winnings if bet amount exceeds it
                    else :
                        bet_amount *= 2
                spin_counter +=1
        #when it hits -256 or 80
        while ep_winnings[spin_counter - 1][i] >= 80 + 256 and spin_counter < dimension[0]:
                ep_winnings[spin_counter][i] = 80 + 256
        while ep_winnings[spin_counter - 1][i] <= 0 and spin_counter < dimension[0]:
                ep_winnings[spin_counter][i] =0
        spin_counter +=1

    
    
    return ep_winnings - 256


def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = 0.47  # set appropriately to the probability of a win
    print(get_spin_result(win_prob))  # test the roulette spin	  	   		   	 		  		  		    	 		 		   		 		  
    #------------------------------Experiment 1------------------------------#
                                   ##Figure 1##
    episodes = 10
    spins = 1000
    winnings = experiment_1(episodes, spins, win_prob)
    plt.figure(1)
    plt.plot(winnings)
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.legend(["Episode " + str(a) for a in range(1, episodes + 1)])
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 1")
    plt.savefig('Figure 1')
                                    ##Figure 2,3##
    episodes = 1000
    spins = 1000
    winnings = experiment_1(episodes, spins, win_prob)
    #data array
    mean = np.zeros((spins + 1, 1))
    med = np.zeros((spins + 1, 1))
    std = np.zeros((spins + 1, 1))
    #the actual data:
    for i in range (1, spins + 1) :
        mean[i] = np.mean(winnings[i])
        med[i] = np.median(winnings[i])
        std[i] = np.std(winnings[i])
    #adding line :
    upper_bound_mean = mean + std
    lower_bound_mean = mean - std
    upper_bound_med = med + std
    lower_bound_med = med - std
    #plotting

                                    #Figure 2#
    data = np.concatenate((upper_bound_mean, mean,  lower_bound_mean), axis = 1) #plotting data
    plt.figure(2)
    plt.axis([0, 300, -256, 100])
    plt.plot(data)
    #plot legends
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.legend(["Upper Bound", "Mean", "Lower Bound"])
    plt.savefig('Figure 2')

                                        #Figure 3#
    data = np.concatenate((upper_bound_med, med,  lower_bound_med), axis = 1) #plotting data
    plt.figure(3)
    plt.axis([0, 300, -256, 100])
    plt.plot(data)
    #plot legends
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.legend(["Upper Bound", "Med", "Lower Bound"])
    plt.savefig('Figure 3')

                              ###Experiment 2 ###
    #Parameters for this figure
    episodes = 1000
    spins = 1000
    win_prob = 0.47
    winnings = experiment_2(spins, episodes, win_prob)

    #creating data array
    mean = np.zeros((spins + 1 , 1))
    std = np.zeros((spins + 1 , 1))
    med = np.zeros((spins + 1 , 1))

    for i in range (1, spins + 1):
        mean[i] = np.mean(winnings[i])
        med[i] = np.median(winnings[i])
        std[i] = np.std(winnings[i])

    #Line : 
    upper_bound_mean = mean + std
    lower_bound_mean = mean - std
    upper_bound_med = med + std
    lower_bound_med = med - std
    # ### --------------- Figures 4 --------------- ###
    data2 = np.concatenate((upper_bound_mean, mean,  lower_bound_mean), axis = 1)
    plt.axis([0, 1000, -256, 100])
    plt.plot(data2)
    plt.legend(["Upper Bound", "Mean", "Lower Bound"])
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 4")
    plt.savefig('Figure 4')


    # ### --------------- Figures 5 --------------- ###

    data3 = np.concatenate((upper_bound_med, med,  lower_bound_med), axis = 1)
    plt.axis([0, 1000, -256, 100])
    plt.plot(data3)
    plt.legend(["Upper Bound", "Median", "Lower Bound"])
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 5")
    plt.savefig('Figure 5')



   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 	  		    	 		 		   		 		  
test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
