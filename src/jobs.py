from hotqueue import HotQueue
import redis
import uuid
import os
import json

q = HotQueue("plot_queue", host='10.108.182.250', port=6437, db=1)

rd = redis.StrictRedis(host='10.108.182.250', port=6437, db=0)

def generate_jid():
    """
    Create a random identifier for a job.
    """
    return str(uuid.uuid4())


def save_job(jid, jobd):
    """Save job in database."""
    rd.set(jid, json.dumps(jobd))


def queue_job(jid):
    """
    add job to queue
    """
    q.put(jid)


def instantiate_job(jid, substance, status):
    """
    Create the job object as a dictionary.
    :param: jid - unique id for job
    :param: substance - what user wants data about
    :param: status - the status of the job
    """
    if type(jid) == str:
        return {'id': jid,
                'substance': substance,
                'status': status
                }
    return {'id': jid.decode('utf-8'),
            'substance': substance.decode('utf-8'),
            'status': status.decode('utf-8')
            }


def add_job(substance, status="submitted"):
    jid = generate_jid()
    jobd = instantiate_job(jid, substance, status)
    save_job(jid, jobd)
    queue_job(jid)
    return jobd


def update_status(jid, status):
    jobd = json.loads(rd.get(jid))
    if jobd:
        jobd['status'] = status
        save_job(jid, jobd)
    else:
        raise Exception()

def check_status(jid):
    job_dict = json.loads(rd.get(jid))
    return job_dict['status'] + '\n'
