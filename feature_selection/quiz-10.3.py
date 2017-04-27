 #################################
    ######## your code below ########
    ### set from_poi to True if #####
    ### the email is from a POI #####
    #################################

    if from_emails:
        if from_emails[0] in poi_email_list: # since from_email is always one
            from_poi = True
        #ctr = 0
        #while not from_poi and ctr < len(from_emails):
        #    if from_emails[ctr] in poi_email_list:
        #        from_poi = True
        #    ctr += 1