import features_extraction, sys
import numpy as np
import joblib

def main():
    url=sys.argv[1]

    features_test=features_extraction.main(url)

    test =  np.array(features_test)
    test = test.reshape(1, -1)

    clf = joblib.load('classifier/model.pkl') ##you may have to mention the whole address of model.pkl from "/home/username/.."##

    pred=clf.predict(test)

    #prob = clf.predict_proba(features_test)

    #print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if int(pred)==1:
        # print "The website is safe to browse"
        print "SAFE"
    elif int(pred)==-1:
        # print "The website has phishing features. DO NOT VISIT!"
        print "MALICIOUS"

    # print 'Error -', features_test

if __name__=="__main__":
    main()