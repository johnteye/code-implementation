
stack = []
# add new items to a stack
stack.append("plate1")
stack.append("plate2")
stack.append("plate3")

print(stack)
# remove last item from the stack LIFO
stack.pop()

# view last element in stack - peek
stack[-1]

#########  Queues ################
queue = []

## Enqueue - adding items to the rear of the queue
queue.append("car1")
queue.append("car2")

## Dequeue - removing items from the front ot the queue FIFO
queue.pop(0)


### Deque is a double edged queue where data can be inserted and deleted from both ends

## R- rephrase the question
## E - examples 
## A - approach
## C - code
## T - test
## O - optimize


# example 
stack = []

pair = {
    ")": "(",
    "}": "{",
    "]": "["
}

def isValid(s):
    for c in s:
        if c in pair:
            if stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


print(isValid("{([])}"))




