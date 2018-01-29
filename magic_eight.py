def ask_eight():
    question = input("What is your question?")
    return question

def add_questions():

	lst_answers =  ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely","You may rely on it",
	"As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now",
	"Cannot predict now", "Concentrate and ask again","Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
	rand_index = randrange(len(lst_answers))

	return lst_answers[rand_index]
