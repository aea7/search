# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util
from game import Directions
from util import Stack, Queue, PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
     - (5, 5)
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
     - False
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
     - [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    """

    start = problem.getStartState()
    actions = []
    visited = set()
    stack = Stack()

    start_node = (start, actions, 0)

    stack.push(start_node)

    while not stack.isEmpty():

        current_state = stack.pop()
        actions = current_state[1]

        if current_state[0] not in visited:
            visited.add(current_state[0])

            if problem.isGoalState(current_state[0]):
                return actions

            successors = problem.getSuccessors(current_state[0])
            for action in successors:
                if action[0] not in visited:
                    direction = action[1]

                    temp_actions = actions + direction.split() # split -- converts str to list

                    new_element = (action[0], temp_actions, action[2]) # iterative actions list
                    stack.push(new_element)

    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    start = problem.getStartState()
    actions = []
    visited = set()
    queue = Queue()

    start_node = (start, actions, 0)

    queue.push(start_node)

    while not queue.isEmpty():

        current_state = queue.pop()
        actions = current_state[1]

        if current_state[0] not in visited:
            visited.add(current_state[0])

            if problem.isGoalState(current_state[0]):
                return actions

            successors = problem.getSuccessors(current_state[0])
            for action in successors:
                if action[0] not in visited:
                    direction = action[1]

                    temp_actions = actions + direction.split() # split -- converts str to list

                    new_element = (action[0], temp_actions, action[2])
                    queue.push(new_element)

    return actions




def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    actions = []
    visited = set()
    priority_queue = PriorityQueue()

    start_node = (start, actions, 0)

    priority_queue.push(start_node, 0)

    while not priority_queue.isEmpty():

        current_state = priority_queue.pop()
        actions = current_state[1]

        if current_state[0] not in visited:
            visited.add(current_state[0])

            if problem.isGoalState(current_state[0]):
                return actions

            successors = problem.getSuccessors(current_state[0])
            for action in successors:
                if action[0] not in visited:
                    direction = action[1]

                    temp_actions = actions + direction.split() # split -- converts str to list

                    total_cost = action[2] + current_state[2]

                    new_element = (action[0], temp_actions, total_cost)
                    priority_queue.push(new_element, total_cost)

    return actions



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    actions = []
    visited = set()
    priority_queue = PriorityQueue()

    start_node = (start, actions, 0)

    priority_queue.push(start_node, 0)

    while not priority_queue.isEmpty():

        current_state = priority_queue.pop()
        actions = current_state[1]

        if current_state[0] not in visited:
            visited.add(current_state[0])

            if problem.isGoalState(current_state[0]):
                return actions

            successors = problem.getSuccessors(current_state[0])
            for action in successors:
                if action[0] not in visited:
                    direction = action[1]

                    temp_actions = actions + direction.split()  # split -- converts str to list

                    total_cost = action[2] + current_state[2]
                    heuristic_cost = heuristic(action[0], problem)

                    new_element = (action[0], temp_actions, total_cost)  # iterative actions list
                    priority_queue.push(new_element, total_cost + heuristic_cost)

    return actions




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
