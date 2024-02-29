def make_title_case(sentence):
    sentence_list=sentence.split()
    for i in range(len(sentence_list)):
        sentence_list[i]=sentence_list[i][0].upper() + sentence_list[i][1:].lower()
    print(sentence_list)
    return " ".join(sentence_list)



print(make_title_case("Hi thEre HelLO"))

