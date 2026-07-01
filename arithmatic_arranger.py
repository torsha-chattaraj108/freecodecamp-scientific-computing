def arithmetic_arranger(problems,show_answer=False):
    if len(problems)>5:
        return "Error: Too many problems."
    top_line=[]
    bottom_line=[]
    dashes=[]
    answers=[]
    for problem in problems:
        top,operator,bottom=problem.split()
        if operator!='+' and operator!='-':
            return "Error: Operator must be '+' or '-'."
        if not (top.isdigit() and bottom.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(top)>4 or len(bottom)>4:
            return "Error: Numbers cannot be more than four digits."
        width=max(len(top),len(bottom))+2
        top_line.append(top.rjust(width))
        bottom_line.append(operator+(bottom.rjust(width-1)))
        dashes.append('-'*width)
        if show_answer:
            if operator=='+':
                current_answer=str(int(top)+int(bottom))
            else:
                current_answer=str(int(top)-int(bottom))
            answers.append(current_answer.rjust(width))
    arranged='    '.join(top_line)+'\n'+'    '.join(bottom_line)+'\n'+'    '.join(dashes)
    if show_answer:
        arranged+='\n'+'    '.join(answers)
    return arranged
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2","45 + 43","123 + 49","888 + 40","653 + 87"],True)}')
