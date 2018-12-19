def hello(name, language="en"):
    """Say hello to a person.

    :param name: the name of the person
    :type name: str
    :param language: the language in which the person should be greeted
    :type language: str
    GoalKicker.com – Python® Notes for Professionals 39
    :return: a number
    :rtype: int
    """

    print(greeting[language]+" "+name)
    return 4

hello(Ron)
