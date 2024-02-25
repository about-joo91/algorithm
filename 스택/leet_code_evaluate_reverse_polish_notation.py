class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                second_num, first_num = stack.pop(), stack.pop()
                match token:
                    case '+':
                        stack.append(first_num + second_num)
                    case "-":
                        stack.append(first_num - second_num)
                    case "*":
                        stack.append(first_num * second_num)
                    case "/":
                        stack.append(int(first_num / second_num))
            else:
                stack.append(int(token))
        
        return int(stack[-1])
      
