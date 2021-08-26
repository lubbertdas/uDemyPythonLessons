import requests
import json
import html

def prepare_object(json):
    import random
    correct_pos = random.randint(0,3)

    trivia_object                   = {}
    trivia_object["correct_answer"] = correct_pos + 1
    trivia_object["answers"]        = json["results"][0]["incorrect_answers"]
    trivia_object["question"]       = json["results"][0]["question"]
    trivia_object["answers"].insert(correct_pos, json["results"][0]["correct_answer"])

    return trivia_object

def print_promt(trivia_object):
    print("Question: ", html.unescape(trivia_object["question"]))
    for option in trivia_object["answers"]:
        print(trivia_object["answers"].index(option)+1, " " + html.unescape(option))

    #print(trivia_object)
    pass

def get_answer(trivia_object):
    correct_answer = trivia_object["correct_answer"]
    user_answer = int(input("Enter answer number: "))

    try:
        if user_answer == correct_answer:
            print("Correct! The correct answer is indeed", trivia_object["answers"][correct_answer - 1])
        else:
            print("Damn, the correct answer was actually", trivia_object["answers"][correct_answer - 1])
    except:
        print('user answer: ', correct_answer)
        print('trivia_object ', trivia_object)

def main():
    try:
        r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple", verify=False)

        json_obj        = json.loads(r.text)

        trivia_object   = prepare_object(json_obj)
        print_promt(trivia_object)
        get_answer(trivia_object)
                
    except requests.exceptions.RequestException as e:
        print('Oh, snap! ', e)

main()
