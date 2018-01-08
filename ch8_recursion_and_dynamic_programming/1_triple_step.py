def triple_step(n_steps):
    steps = []

    for n in range(n_steps):
        if n == 0:
            steps.append(1)
        elif n == 1:
            steps.append(1 + steps[0])
        elif n == 2:
            steps.append(1 + steps[0] + steps[1])
        else:
            steps.append(steps[n-1] + steps[n-2] + steps[n-3])

    return steps[-1]


print('triple', triple_step(4))
