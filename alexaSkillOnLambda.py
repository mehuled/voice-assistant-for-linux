from __future__ import print_function
import time
import paramiko



#---------------- Helps connect to remote system and execute a command------------------------

def run_command_on_remote(command) :
	
	success = True
	port = 22

	
	username = 'mehul'
	hostname = 'mehuled.pagekite.me'
	password = '##########' 	 '''The password is saved on AWS Lambda as an Environment Variable.'''


	# Connect and use paramiko Client to negotiate SSH2 across the connection
	try:
	    client = paramiko.SSHClient()
	    client.set_missing_host_key_policy(paramiko.WarningPolicy())
	    print('*** Connecting...')
	    client.connect(hostname, port, username, password)
	    client.invoke_shell()
	    stdin, stdout, stderr = ssh.exec_command(command)
	    client.close()

	except Exception as e:
	    print('*** Failed ****')
	    success = False 
	    
	    try:
		client.close()
	    except:
		pass
	
	return success 

	




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
    speech_output = "Hi, This is Mehul's Girlfriend. What would you like me to do? " \
    reprompt_text = "Hi again, This is Mehul's Girlfriend. " \
                    "How can I help you?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for talking to Mehul's girlfriend. " \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
    
def unclutter_desktop(intent,session) :
    session_attributes = {} 
    reprompt_text = "Make sure you have pagekite server running on your system, Pagekite server is needed to remotely access systems on a private network."
        
    command ='python ~/innovaccerSummer/unclutter.py'    
    success = run_command_on_remote(command)
    
    if success :    
    	should_end_session = True
    	speech_output = "Your desktop has been successfully unclutterd! Please have a look."
    
    elif 
    	should_end_session = False
    	speech_output = "I was unable to unclutter your desktop. Kindly ensure that that pagekite server is running on your system and try again.
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def top_files_by_size(intent,session) :
    session_attributes = {} 
    command ='python ~/innovaccerSummer/topFilesBySize.py'    
    success = run_command_on_remote(command)
    
    if success :    
    	should_end_session = True
    	speech_output = "I have listed the top 10 files on your system in a file top files dot html on desktop! Please have a look."
    
    else 
    	should_end_session = False
    	speech_output = "I was unable to connect to remote system. Kindly ensure that pagekite server is running on your system and try again.
    
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
    
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to skill's intent handlers
    if intent_name == "TopFilesBySizeIntent":
        return top_files_by_size(intent, session)
    elif intent_name == "UnclutterDesktopIntent" :
        return unclutter_desktop(intent,session)
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



# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

  
    if (event['session']['application']['applicationId'] !="amzn1.ask.skill.2c8ab163-6830-45b1-83e3-c5ee27fd58c5"):
    	raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

