###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = []
ATTRS.append("ID")
ATTRS.append("radius")
ATTRS.append("texture")
ATTRS.append("perimeter")
ATTRS.append("area")
ATTRS.append("smoothness")
ATTRS.append("compactness")
ATTRS.append("concavity")
ATTRS.append("concave")
ATTRS.append("symmetry")
ATTRS.append("fractal")
ATTRS.append("class")
###############################################################################


def make_training_set(filename):
    """ Read training data from the file whose path is filename.
        Return a list of records, where each record is a dictionary
        containing a value for each of the 12 keys in ATTRS.
    """
    # COMPLETE - DO NOT MODIFY
    training_records = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        line_list = line.split(',')
        
        # Create a dictionary for the line and map the attributes in
        # ATTRS to the corresponding values in the line of the file
        record = {}
        
        # read patient ID as an int:
        record[ATTRS[0]] = int(line_list[0].strip())
        
        # read attributes 1 through 10 as floats:
        for i in range(1,11):
            record[ATTRS[i]] = float(line_list[i])
        
        # read the class (label), which is "M", or "B" as a string:
        record[ATTRS[11]] = line_list[31].strip() 

        # Add the dictionary to a list
        training_records.append(record)        

    return training_records


def make_test_set(filename):
    """ Read test data from the file whose path is filename.
        Return a list with the same form as the training
        set, except that each dictionary has an additional
        key "prediction" initialized to "none" that will be
        used to store the label predicted by the classifier. 
    """
    # COMPLETE - DO NOT MODIFY
    test_records = make_training_set(filename)

    for record in test_records:
        record["prediction"] = "none"

    return test_records


def train_classifier(training_records):
    """ Return a dict containing the midpoint between averages
        among each class (malignant and benign) of each attribute.
        (See the A5 writeup for a more complete description)
        Precondition: training_records is a list of patient record
                      dictionaries, each of which has the keys
                      in the global variable ATTRS
        Postcondition: the returned dict has midpoint values calculated
                       from the training set for all 10 attributes except
                       "ID" and"class".
    """
    # TODO 1 - implement this function
    #for line in 
    classifier_dict = {} #will contain all the averages
    #Bthing =
    #Mthing =
    #if the last index [-1] contains "B":
    # create a new thing where for every index that's the same the value is added
    # divide the total amount contained by the thing by the number of times a value was added
    #average it here
    #if the last index [-1] contains "M" average it here:
    # create a new thing where for every index that's the same the value is added up
    # divide the total amount contained by the thing by the number of times a value was added
    


def classify(test_records, classifier):
    """ Use the given classifier to make a prediction for each record in
        test_records, a list of dictionary patient records with the keys in
        the global variable ATTRS. A record is classified as malignant
        if at least 5 of the attribute values are above the classifier's
        threshold.
        Precondition: classifier is a dict with midpoint values for all
                      keys in ATTRS except "ID" and "class"
        Postcondition: each record in test_records has the "prediction" key
                       filled in with the predicted class, either "M" or "B"
    """
    # TODO 2 - implement this function


def report_accuracy(test_records):
    """ Print the accuracy of the predictions made by the classifier
        on the test set as a percentage of correct predictions.
        Precondition: each record in the test set has a "prediction"
        key that maps to the predicted class label ("M" or "B"), as well
        as a "class" key that maps to the true class label. """
    # TODO 3 - implement this function



def check_patients(test_records, classifier):
    """ Repeatedly prompt the user for a Patient ID until the user
        enters "quit". For each patient ID entered, search the test
        set for the record with that ID, print a message and prompt
        the user again. If the patient is in the test set, print a
        table: for each attribute, list the name, the patient's value,
        the classifier's midpoint value, and the vote cast by the
        classifier. After the table, output the final prediction made
        by the classifier.
        If the patient ID is not in the test set, print a message and
        repeat the prompt. Assume the user enters an integer or quit
        when prompted for the patient ID.
    """
    # TODO 4 - implement this function
    
    # Pseudocode:
    
    # prompt user for an ID
    # while the user has not entered "quit":
        # determine whether the entered patient ID is in the test set
        # if it is,
            # print a table of results (see the handout and sample output)
        # otherwise,
            # print a message saying the patient ID wasn't found

        # prompt the user for anoher ID


if __name__ == "__main__": 
    # Main program - COMPLETE
    # Do not modify except to uncomment each code block as described.
    
    # load the training set
    print("Reading in training data...")
    training_data_file = "cancerTrainingData.txt"
    training_set = make_training_set(training_data_file)
    print("Done reading training data.")
    
    # load the test set 
    print("Reading in test data...")
    test_file = "cancerTestingData.txt"
    test_set = make_test_set(test_file)
    print("Done reading test data.\n")

    # train the classifier: uncomment this block once you've
    # implemented train_classifier
#    print("Training classifier..."    )
#    classifier = train_classifier(training_set)
#    print("Classifier cutoffs:")
#    for key in ATTRS[1:11]:
#        print("    ", key, ": ", classifier[key], sep="")
#    print("Done training classifier.\n")

    # use the classifier to make predictions on the test set:
    # uncomment the following block once you've written classify
    # and report_accuracy
#    print("Making predictions and reporting accuracy")
#    classify(test_set, classifier)
#    report_accuracy(test_set)
#    print("Done classifying.\n")

    # prompt the user for patient IDs and provide details on
    # the diagnosis: uncomment this line when you've
    # implemented check_patients
#    check_patients(test_set, classifier)
