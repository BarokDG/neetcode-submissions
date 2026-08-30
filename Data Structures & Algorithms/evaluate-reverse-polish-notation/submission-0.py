class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = []

        for token in tokens:
            if token not in "-+*/":
                out.append(int(token))
                continue

            op2 = out.pop()
            op1 = out.pop()

            if token == '+':
                out.append(op1 + op2)
            elif token == '-':
                out.append(op1 - op2)
            elif token == '*':
                out.append(op1 * op2)
            else:
                out.append(int(op1 / op2))

        return out[0]