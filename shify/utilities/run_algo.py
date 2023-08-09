

def run_algo(
    initialize,
    handle_data
):
    context = {}
    context['init_value'] = 123

    state = {}
    state['value'] = context['init_value']

    initialize(context)

    for _ in range(0, 10):
        state['value'] += 1
        handle_data(context, state)

    pass