from flask importFlask, request, Response
import random, requests

@app.route('/animal', methods['GET'])
def animal():
    the_animal = ["cow", "dog", "lion", "parrot", "frog"]
    randomanimal = random.choice(the_animal)

    return Response(choice)

@app.route('/noise', methods['GET', 'POST'])
def noise():
    animalchoice = requests.data.decode('utf-8')
    if animalchoice == "cow":
        noise = "woof woof"
    elif animalchoice == "cow":
        noise = "mooooooo"
    elif animalchoice == "lion":
        noise = "roar"
    elif animalchoice == "parrot":
        noise = "stolen voice"
    elif animalchoice == "frog":
        noise = "ribbet"
    else:
        noise = "no noise"
    return Response(noise)
