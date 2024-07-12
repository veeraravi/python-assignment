@staticmethod
def verify_description(description):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    
    for char in description:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack


@classmethod
def predict_by_id(cls, function_id, value):
    function = cls.find_by_id(function_id)
    if function:
        return {'result': function.y_intercept + function.slope * value}
    return {'message': 'Function does not exist.'}, 404


@staticmethod
def plot_linear_function(a, b):
    import matplotlib.pyplot as plt
    x = list(range(-10, 11))
    y = [a + b * xi for xi in x]
    
    plt.figure()
    plt.plot(x, y, label=f'y = {b}x + {a}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Function Plot')
    plt.legend()
    plt.grid(True)
    
    return plt


@classmethod
def save_plot_by_id(cls, function_id, output_path):
    import os
    function = cls.find_by_id(function_id)
    if not function:
        raise ValueError("Function does not exist.")
    
    if not os.path.isdir(os.path.dirname(output_path)):
        raise ValueError("Directory does not exist.")
    
    if os.path.exists(output_path):
        raise ValueError("File already exists.")
    
    plot = cls.plot_linear_function(function.y_intercept, function.slope)
    plot.savefig(output_path)
    plt.close()
    
    return {'output_path': output_path}


