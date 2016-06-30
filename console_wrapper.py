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
    #
    # Initializes object with the path, executable name and command line arguments string
    def __init__(self, wdir='', cfile='', args=''):
        self.work_dir=wdir
        self.app_file=cfile
        self.cmd_line_args=args
    #
    # Runs once initialized console with previous arguments or passing new arguments each time
    def run_console(self,args=''): 
            if args!='':
                self.cmd_line_args=args
                self.ret_out=[]
                self.ret_errs=[]
                self.ret_code = None
            self.sub_proc=subprocess.Popen([self.work_dir+'\\'+self.app_file] + shlex.split(self.cmd_line_args), bufsize=-1, executable=None, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=True)
            # Read all the output, errors and return code
            self.ret_out.append(self.sub_proc.stdout.read())
            self.ret_errs.append(self.sub_proc.stderr.read())
            self.ret_code = self.sub_proc.wait()
