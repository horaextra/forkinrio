# *-* coding: utf-8 -*-
import time
import sys
import os

def deploy(args):
    
  if not args[1:]:
    print 'ERROR: No revision given. Cannot deploy.'
    print 'To deploy the current revision, use the following command:'
    print '$ python deploy.py `git rev-parse HEAD`\n'
    sys.exit(1)

  rev = args[1]
  
  #Run tests
  if run_tests():
    #Create a stap based on local time.
    stamp = time.strftime("%Y%m%d-%Hh%Mm%Ss")
   
    #Deploy
    os.system("../google_appengine/appcfg.py update ../src/ ")
    
    #Tag the deployed revision
    os.system("git tag -a deploy/%s %s -m ''" % (stamp, rev))
    os.system("git push --tags")
    
  else:
    print "ERROR: Tests are not passing. Cannot deploy."
    print "Solve problems and run command again.\n"

def run_tests():

  # This tip was used to solve problem on os.system,
  # that return true when it is broke
  broke = os.system("nosetests -v --with-gae --gae-lib-root ../google_appengine")

  if broke:
    return False
  else:
    return True

if __name__ == "__main__":
  deploy(sys.argv)

