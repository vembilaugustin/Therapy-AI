from __future__ import print_function

import boto3


s3 = boto3.client('s3')


client0 = boto3.resource('dynamodb')
table = client0.Table('patient')
client1 = boto3.resource('dynamodb')
table1 = client1.Table('question1')
client2 = boto3.resource('dynamodb')
table2 = client2.Table('question2')
client3 = boto3.resource('dynamodb')
table3 = client3.Table('question3')
client4 = boto3.resource('dynamodb')
table4 = client4.Table('question4')
client5 = boto3.resource('dynamodb')
table5 = client5.Table('question5')
client6 = boto3.resource('dynamodb')
table6 = client6.Table('question6')
client7 = boto3.resource('dynamodb')
table7 = client7.Table('question7')
client8 = boto3.resource('dynamodb')
table8 = client8.Table('question8')
client9 = boto3.resource('dynamodb')
table9 = client9.Table('question9')





# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    
    
    speech_output = "Welcome to Therapy AI " \
                    "Please tell me your name."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your favorite color by saying, " \
                    "my favorite color is red."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_my_name_attributes(my_name):
    return {"myName": my_name}


def set_name_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'MyName' in intent['slots']:
        my_name = intent['slots']['MyName']['value']
        session_attributes = create_my_name_attributes(my_name)
        s3.put_object(Bucket='therapyai',Key='PatientName',Body=my_name)
        var = table.put_item(Item = { 'name': my_name })
        
        speech_output = "Hey " + \
                        my_name + \
                        " It's nice to meet you. We need to get to know each other more" \
                        " If you don't mind I would like to ask you some questions. So let's begin. " \
                        "How would you describe your sleep, you can say you slept good, It is difficult for you to sleep or you did not sleep at all" 
                        
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def set_ansone_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answer' in intent['slots']:
        ans_one = intent['slots']['answer']['value']
        
        #Read the object stored in key 'myList001'
        object = s3.get_object(Bucket='therapyai',Key='PatientName')
        my_name1 = object['Body'].read()
        
        
        var = table1.put_item(Item = { 'answer': ans_one })
        
        speech_output = "How is your Energy compared to before." + my_name1 + \
                        ". You can say less, same, or more "
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
        
def set_anstwo_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answertwo' in intent['slots']:
        ans_two = intent['slots']['answertwo']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerTwo',Body=ans_two)
        
        var = table2.put_item(Item = { 'answer': ans_two })
        
        speech_output = "Do you find pleasure in doing things, little interest, or no interest at all "
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        

def set_ansthree_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answerthree' in intent['slots']:
        ans_three = intent['slots']['answerthree']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerThree',Body=ans_three)
        
        
        var = table3.put_item(Item = { 'answer': ans_three })
        
        speech_output = "I want to know about your appetite, do you overeat or do you have poor appetite."
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def set_ansfour_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answerfour' in intent['slots']:
        ans_four = intent['slots']['answerfour']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerFour',Body=ans_four)
        
        var = table4.put_item(Item = { 'answer': ans_four })
        
        speech_output = "I want to know about your appetite"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def set_ansfive_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answerfive' in intent['slots']:
        ans_five = intent['slots']['answerfive']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerFive',Body=ans_five)
        
        var = table5.put_item(Item = { 'answer': ans_five })
        
        speech_output = "Where do you find most uncomfortable, You can say at home, at work,at school or College"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def set_anssix_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answersix' in intent['slots']:
        ans_six = intent['slots']['answersix']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerSix',Body=ans_six)
        
        var = table6.put_item(Item = { 'answer': ans_six })
        
        speech_output = "Do you prefer staying indoors or outdoors."
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def set_ansseven_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answerseven' in intent['slots']:
        ans_seven = intent['slots']['answerseven']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerSeven',Body=ans_seven)
        
        var = table7.put_item(Item = { 'answer': ans_seven })
        
        speech_output = "Why do you feel like this, can you think of any reason why you are feeling down"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def set_anseight_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answereight' in intent['slots']:
        ans_eight = intent['slots']['answereight']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerEight',Body=ans_eight)
        
        var = table8.put_item(Item = { 'answer': ans_eight })
        
        speech_output = "Have you had any Suicidal thoughts or ever felt like hurting yourself"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def set_ansnine_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'answernine' in intent['slots']:
        ans_nine = intent['slots']['answernine']['value']
        s3.put_object(Bucket='therapyai',Key='AnswerNine',Body=ans_nine)
        
        var = table9.put_item(Item = { 'answer': ans_nine })
        
        speech_output = "Have a nice day. If you want to start the next session just say go ahead or tell me to start session two"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def set_ansten_to_db(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    
    my_name = session['attributes']['myName']
        
    speech_output = "Have a nice day" + my_name + " If you want to start the next session just say go ahead or tell me to start session two"
    reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
   
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyNameIsIntent":
        return set_name_in_session(intent, session)
    elif intent_name == "SessionTwo":
        return set_ansten_to_db(intent, session)
    elif intent_name == "QuestionOne":
        return set_ansone_to_db(intent, session)
    elif intent_name == "QuestionTwo":
        return set_anstwo_to_db(intent, session)
    elif intent_name == "QuestionThree":
        return set_ansthree_to_db(intent, session)
    elif intent_name == "QuestionFour":
        return set_ansfour_to_db(intent, session)
    elif intent_name == "QuestionFive":
        return set_ansfive_to_db(intent, session)
    elif intent_name == "QuestionSix":
        return set_anssix_to_db(intent, session)
    elif intent_name == "QuestionSeven":
        return set_ansseven_to_db(intent, session)
    elif intent_name == "QuestionEight":
        return set_anseight_to_db(intent, session)
    elif intent_name == "QuestionNine":
        return set_ansnine_to_db(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
