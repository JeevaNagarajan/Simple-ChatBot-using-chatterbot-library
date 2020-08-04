# importing our chatterbot libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# creating instance(object) for our ChatBot and naming our ChatBot as 'Tom'.
my_chatbot = ChatBot('Tom')

# opening the traning data for our ChatBot from the file
# using open function and storing it in identifier named as 'training_data_for_mybot'.
training_data_for_mybot = open('training_data_for_mychatbot/Ques and Anes.txt') . read() . splitlines()

# training the ChatBot using our personal data from the file
trainer = ListTrainer(my_chatbot)
trainer . train(training_data_for_mybot)

# training the ChatBot with english corpus data
trainer = ChatterBotCorpusTrainer(my_chatbot)
trainer . train('chatterbot.corpus.english')

while True:

    # input function is used to get the input from the user
    user_request = input('you - ')

    # get_response() returns the responses for the user_request
    bot_response = my_chatbot . get_response(user_request)
    print('Tom - ' , bot_response)
