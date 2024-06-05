"""The console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """hbnb console class"""
    
    prompt = '(airbnb-e)'

    def do_EOF(self, line):
        """ctrl+D quits the console"""
        return True
    
    def do_quit(self, line):
        """quit exits the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
