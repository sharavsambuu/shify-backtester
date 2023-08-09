

def initialize(ctx):
    ctx['count'] = 0
    print(f"Init context : {ctx}")

def handle_data(ctx, state):
    ctx['count'] += 1
    print(f"context : {ctx}, state : {state}")
