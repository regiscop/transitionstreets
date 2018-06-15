# Welcome to Transition streets script.
#
# Feel free to collaborate to the script.
# 

STARTCODE
from random import choice, random
# -----------------------------------------------------------------------------------------------------------------

INTERACTION AskAboutRunning

    INPUT user
        
    USEFULLNESS
       if 'like_running' in USERDICT or USER.s_home_location is None:
            # Don't ask about running if the location is not known.
            return 0.0
       else:
           # Here, should be looking into other preferences / user profile to evaluate probability that user is a runner
           try:
               return max(USER.demand_for_info['like_running'] / 1000.0, 0.4)
           except:
               return 0.05

    EXECUTE

        if STATE is None:
            STATE = 'ask'
            return



