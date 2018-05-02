
import verbose

verbose.setLevels(99)                            # vlist can be a str: "2,readcmds,blah" or list [2,"readcmds","blah"]
verbose.openFile("test_verbose.log","w")        # output to a file (open with truncate); default: sys.stderr output
verbose.verbose([2,"loop"],"message")               # output if verbose level >= 2 or one verbose string is "loop"
verbose.verbose(["info"],"message")                 # output if one verbose string is "info"
verbose.verbose([99],"message")                     # output if verbose level >= 99
verbose.verbose("99","message")                     # output if verbose level >= 99
verbose.verbose(99,"message")                       # output if verbose level >= 99
verbose.isLevel("99,blah")                          # True if verbose level >= 99 or verbose str is "blah"
verbose.closeFile()


