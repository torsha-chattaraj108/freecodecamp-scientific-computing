#This program arranges the given sums
def arithmetic_arranger(problems,show_answer=False):
    #Checks if the number of problems is not more than 5
    if len(problems)>5:
        return "Error: Too many problems."
    #Assign some empty lists
    top_line=[]
    bottom_line=[]
    dashes=[]
    answers=[]
    #Splits the sum into three parts
    for problem in problems:
        top,operator,bottom=problem.split()
        #Checks that the operator is only "+" and '-'
        if operator!='+' and operator!='-':
            return "Error: Operator must be '+' or '-'."
        #Checks if the sums contain digits only
        if not (top.isdigit() and bottom.isdigit()):
            return "Error: Numbers must only contain digits."
        #Checks that the numbers have only four digits
        if len(top)>4 or len(bottom)>4:
            return "Error: Numbers cannot be more than four digits."
        #Provides the width of the dashes
        width=max(len(top),len(bottom))+2
        #Provides the top line and the bottom line in format needed
        top_line.append(top.rjust(width))
        bottom_line.append(operator+(bottom.rjust(width-1)))
        #Number of dashes to be printed is calculated
        dashes.append('-'*width)
        #Checks if the user wants answers 
        if show_answer:
            if operator=='+':
                current_answer=str(int(top)+int(bottom))
            else:
                current_answer=str(int(top)-int(bottom))
            answers.append(current_answer.rjust(width))
        #The arranged format
    arranged='    '.join(top_line)+'\n'+'    '.join(bottom_line)+'\n'+'    '.join(dashes)
    if show_answer:
        arranged+='\n'+'    '.join(answers)
    return arranged
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2","45 + 43","123 + 49","888 + 40","653 + 87"],True)}')
