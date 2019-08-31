from database import Database
from models import Result

import random
import time
import signal
import sys

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


def main(results, session):
    killer = GracefulKiller()
    while(1):
        t = results[random.randint(0,1)]
        t.score += random.randint(0,3)
        session.add(t)
        session.commit()
        print("Team %s | New score: %s" % (t.id_team, t.score))
        time.sleep(2)
        if killer.kill_now:
            session.close()
            break

if __name__ == '__main__':
    if (len(sys.argv) != 4) or (sys.argv[1] == sys.argv[2]):
        sys.exit("Usage: python process.py id_team_1 id_team_2 id_match")
    int_id_t1 = int(sys.argv[1])
    int_id_t2 = int(sys.argv[2])
    id_match = int(sys.argv[3])    
    db = Database()
    session = db.get_session()
    results = [ session.query(Result).filter_by(id_match=id_match,id_team=int_id_t1).first(), 
                session.query(Result).filter_by(id_match=id_match,id_team=int_id_t2).first()]
    
    main(results, session)
    