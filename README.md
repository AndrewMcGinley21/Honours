# Honours
Repository for Honours Project

Hi Xavier

So Test3.py is the main program where the majority of the magic happens, dataManagement is only used for transforming the labels into one hot encoding 

It uses LoadData3.py as the file processor, it has 2 methods one for 2 classification, attack/normal and the other for 5 class where it splits the data into each attack type

LoadData5.py is what i have been experimenting with that i was telling you about via email the other day

I ran Test3.py as is last night on both 2 class and 5 class and got .74995% Accuracy on 2 and 0.7619252% on 5, both of these values were acquired by testing on KDDTest3 which is from the Testing side of the NSL dataset

KDDTrainThree is a subset of NSL i created that only contains 4999 records for testing purposes and this is what the network was trained with last night 
