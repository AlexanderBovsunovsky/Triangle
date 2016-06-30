import os, shlex, subprocess

#----------------------
# class console_wrapper
#
# Brief: Wraps console call with subprocess.Popen object.
#        Redirects output and errors in internal string lists for futher usage and analyses
#----------------------
class console_wrapper():
    work_dir=''         # working directory path
    app_file=''         # console executable file name 
    cmd_line_args=''    # command line arguments as a string
    ret_code=None       # console return code
    ret_out=[]          # console output strings
    ret_errs=[]         # console error  strings 
    sub_proc=None       # subprocess.Popen object
    resp_timeout=15     # responce timeout to catch program hangup and stop it forcedly 
    #
    # Initializes object with the path, executable name, command line arguments string and timeout value
    def __init__(self, wdir='', cfile='', args='', timeout=15):
        self.work_dir=wdir
        self.app_file=cfile
        self.cmd_line_args=args
        resp_timeout=timeout
    #
    # Runs once initialized console with previous arguments or passing new arguments each time
    def run_console(self, args='', timeout=15): 
        try:
            if args!='':
                self.cmd_line_args=args
                self.ret_out=[]
                self.ret_errs=[]
                self.ret_code = None
            self.sub_proc=subprocess.Popen([self.work_dir+'\\'+self.app_file] + shlex.split(self.cmd_line_args), bufsize=-1, executable=None, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=True)
            # Read all the output, errors and return code
            if self.sub_proc!=None:
                self.ret_out.append(self.sub_proc.stdout.read())
                self.ret_errs.append(self.sub_proc.stderr.read())
                if timeout!=0:
                    self.resp_timeout=timeout
                    self.ret_code = self.sub_proc.wait(self.resp_timeout)
            else:
                self.ret_code = -1
        except OSError as err:               # Raised when executable path/name is not correct or other execution exception raised
            self.stop_console(True)
            self.ret_errs+='OSError detected:'+str(err)+'\n'
        except ValueError as err:           # Raised when some Popen arguments is not correct
            self.stop_console(True)
            self.ret_errs+='subprocess.Popen ValueError detected:'+str(err)+'\n'
        except subprocess.TimeoutExpired:   # Raised when execution time is expired
            self.stop_console(True)
            self.ret_errs+='Responce timeout detected\n'
        finally:
            if self.sub_proc!=None:
                self.ret_code = self.sub_proc.poll()
            else:
                self.ret_code = -1
    #
    # Stops console forcedly if needed
    def stop_console(self,kill=False):
        if self.sub_proc!=None and self.ret_code==None:
            if self.sub_proc.returncode==None:
                if kill==True: 
                    self.sub_proc.kill()
                    self.sub_proc.communicate()
                    self.ret_errs+='Console process was killed\n'
                else:
                    self.sub_proc.send_signal(CTRL_C_EVENT)
                    self.sub_proc.communicate()
                    self.ret_errs+='CTRL_C_EVENT was passed to console\n'
            self.ret_code=self.sub_proc.poll()
