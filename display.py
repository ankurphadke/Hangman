

# list of hangman stages

def draw(attempts_left):
    stages = [
        """
        _________________
          |            |
          |            O
          |           \\|/ 
          |            |
          |           / \\ 
          |
        __|__
        """,
        """
        _________________
          |            |
          |            O  HELP!!!
          |           \\|/ 
          |            |
          |           /
          |
        __|__
        """,
        """
        _________________
          |            |
          |            O
          |           \\|/ 
          |            |
          |          
          |
        __|__
        """,
        """
        _________________
          |            |
          |            O
          |           \\| 
          |            |
          |           
          |
        __|__
        """,
        """
        _________________
          |            |
          |            O
          |            |
          |            |
          |          
          |
        __|__
        """,
        """
        _________________
          |            |
          |            O
          |          
          |           
          |           
          |
        __|__
        """,
        """
        _________________
          |            |
          |            
          | 
          |            
          |           
          |
        __|__
        """
    ]
    return stages[attempts_left]
