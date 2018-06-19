import time
from slackclient import SlackClient

def tailfile(thefile):
        thefile.seek(0, 2)
        while True:
                line = thefile.readline()
                if not line:
                        time.sleep(0.1)
                        continue
                yield line

if __name__ == '__main__':
        logfile = open("/var/log/log_file","r")
        loglines = tailfile(logfile)
        words = ["error","fail","exception","refused","unknown","down","unexpected"]

        token = 'slack_token_number'
        sclient = SlackClient(token)

        for line in loglines:
                if any(s in line for s in words):
                        sclient.api_call('chat.postMessage', channel='channel_name', text=line, username='slack_username')
